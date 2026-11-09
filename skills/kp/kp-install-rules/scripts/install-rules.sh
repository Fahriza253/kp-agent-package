#!/usr/bin/env bash
# Memasang rules KP ke .cursor/rules/ di workspace target (biasanya root repo laporan).
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RULES_SRC="$SKILL_ROOT/assets/rules"
TARGET_ROOT="$(cd "${1:-.}" && pwd)"
DEST="$TARGET_ROOT/.cursor/rules"

if [ ! -d "$RULES_SRC" ]; then
  echo "Missing rules bundle: $RULES_SRC" >&2
  exit 1
fi

mkdir -p "$DEST"
cp -R "$RULES_SRC/"* "$DEST/"
echo "Installed KP rules to $DEST"
