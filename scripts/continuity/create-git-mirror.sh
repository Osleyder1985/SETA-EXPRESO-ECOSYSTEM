#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Uso: $0 <SOURCE_REPOSITORY> <MIRROR_DIRECTORY>" >&2
  exit 2
}

[[ $# -eq 2 ]] || usage
SOURCE_REPOSITORY="$1"
MIRROR_DIRECTORY="$2"

command -v git >/dev/null 2>&1 || { echo "ERROR: git no está disponible." >&2; exit 1; }

if [[ -e "$MIRROR_DIRECTORY" && ! -d "$MIRROR_DIRECTORY" ]]; then
  echo "ERROR: el destino existe y no es un directorio: $MIRROR_DIRECTORY" >&2
  exit 1
fi

if [[ ! -e "$MIRROR_DIRECTORY" ]]; then
  echo "[mirror] Creando mirror Git: $MIRROR_DIRECTORY"
  git clone --mirror "$SOURCE_REPOSITORY" "$MIRROR_DIRECTORY"
else
  [[ -d "$MIRROR_DIRECTORY/objects" && -f "$MIRROR_DIRECTORY/config" ]] || {
    echo "ERROR: el destino existe pero no parece un repositorio bare/mirror." >&2
    exit 1
  }
  echo "[mirror] Actualizando mirror existente"
  git -C "$MIRROR_DIRECTORY" remote update --prune
fi

echo "[mirror] Verificando integridad"
git -C "$MIRROR_DIRECTORY" fsck --full

echo "[mirror] HEAD: $(git -C "$MIRROR_DIRECTORY" symbolic-ref -q HEAD || git -C "$MIRROR_DIRECTORY" rev-parse HEAD)"
echo "[mirror] Refs:"
git -C "$MIRROR_DIRECTORY" show-ref --head
echo "[mirror] PASS — mirror creado/actualizado y verificado localmente."
