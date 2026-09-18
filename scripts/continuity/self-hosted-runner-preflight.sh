#!/usr/bin/env bash
set -u

# H-010 / Issue #192 — self-hosted runner preflight.
# Read-only preflight: it does not install, register, authenticate, or modify the host.

failures=0

check() {
  local name="$1"
  shift
  if "$@"; then
    printf 'PASS | %s\n' "$name"
  else
    printf 'FAIL | %s\n' "$name"
    failures=$((failures + 1))
  fi
}

printf '%s\n' '=== SETA-EXPRESO self-hosted runner preflight ==='
printf 'UTC: %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || printf 'unknown')"

check "non-root execution" test "$(id -u)" -ne 0
check "Git available" command -v git
check "Git version >= 2.24.3" bash -c '
  v="$(git --version | awk "{print \$3}")"
  [ "$(printf "%s\n%s\n" "2.24.3" "$v" | sort -V | head -n1)" = "2.24.3" ] ||
  [ "$v" != "2.24.3" ] && [ "$(printf "%s\n%s\n" "2.24.3" "$v" | sort -V | head -n1)" = "2.24.3" ]
'

if command -v uname >/dev/null 2>&1; then
  printf 'INFO | kernel: %s\n' "$(uname -sr 2>/dev/null || printf 'unknown')"
  printf 'INFO | architecture: %s\n' "$(uname -m 2>/dev/null || printf 'unknown')"
fi

if command -v getconf >/dev/null 2>&1; then
  printf 'INFO | CPUs: %s\n' "$(getconf _NPROCESSORS_ONLN 2>/dev/null || printf 'unknown')"
fi

if command -v free >/dev/null 2>&1; then
  printf 'INFO | memory: %s\n' "$(free -h 2>/dev/null | awk '/^Mem:/ {print $2 " total, " $7 " available"}')"
fi

if command -v df >/dev/null 2>&1; then
  printf 'INFO | disk (/): %s\n' "$(df -h / 2>/dev/null | awk 'NR==2 {print $4 " available"}')"
fi

if command -v docker >/dev/null 2>&1; then
  printf 'INFO | Docker: %s\n' "$(docker --version 2>/dev/null || printf 'unavailable')"
  if docker info >/dev/null 2>&1; then
    printf '%s\n' 'PASS | Docker daemon accessible'
  else
    printf '%s\n' 'INFO | Docker daemon not accessible (not a failure; host/Podman execution may be selected later)'
  fi
else
  printf '%s\n' 'INFO | Docker not installed (not a failure; runner execution mode is not selected by this preflight)'
fi

check "runner workspace is not a GitHub credential store" bash -c '
  ! find "$PWD" -maxdepth 3 -type f \( -name ".env" -o -name "*token*" -o -name "*credential*" -o -name "*secret*" \) -print -quit 2>/dev/null | grep -q .
'

if [ "$failures" -eq 0 ]; then
  printf '%s\n' 'RESULT | PREFLIGHT-PASS'
else
  printf 'RESULT | PREFLIGHT-FAIL (%s failed checks)\n' "$failures"
fi

exit "$failures"
