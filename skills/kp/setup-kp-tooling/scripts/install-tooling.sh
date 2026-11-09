#!/usr/bin/env bash
# Menyalin skrip tooling KP ke scripts/ di repo laporan.
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$SKILL_ROOT/assets/scripts"
TARGET_ROOT="$(cd "${1:-.}" && pwd)"
DEST="$TARGET_ROOT/scripts"

if [ ! -d "$SRC" ]; then
  echo "Missing tooling bundle: $SRC" >&2
  exit 1
fi

mkdir -p "$DEST"
for f in check_project_markdown.py generate_laporan_docx.py requirements-docx.txt; do
  if [ -f "$SRC/$f" ]; then
    cp "$SRC/$f" "$DEST/"
    chmod +x "$DEST/$f" 2>/dev/null || true
  fi
done
echo "Installed KP tooling scripts to $DEST"
