# SV-002 — Minimum Privilege Governance

## Purpose

Define the security policy for GitHub Actions permissions using minimum privilege principles.

## Policy

Workflow permissions must be explicit.

Allowed:

- `contents: read`
- Controlled write permissions when the automation purpose requires it.

Forbidden:

- `permissions: write-all`
- Unjustified write permissions.

## Controlled Write Requirements

A workflow requiring write access must provide:

- business/engineering justification;
- related governance control reference;
- minimum required scope.

Example:

```yaml
permissions:
  contents: read
  pull-requests: write
```

## Rationale

Security validation must prevent excessive privileges without blocking legitimate automation governed by evidence and traceability.
