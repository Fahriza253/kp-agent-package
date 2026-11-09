#!/usr/bin/env bash
# Salin katalog skills/ ke .agents/skills/ (hanya skill paket KP, bukan engineering pihak ketiga).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

sync_category() {
  local category="$1"
  local dir
  for dir in "$ROOT/skills/$category"/*/; do
    [ -d "$dir" ] || continue
    local name
    name="$(basename "$dir")"
    rm -rf "$ROOT/.agents/skills/$name"
    cp -R "$dir" "$ROOT/.agents/skills/$name"
    echo "synced: skills/$category/$name -> .agents/skills/$name"
  done
}

sync_category academic
sync_category kp

RULES_ASSETS="$ROOT/skills/kp/kp-install-rules/assets/rules"
if [ -d "$RULES_ASSETS" ]; then
  mkdir -p "$RULES_ASSETS"
  cp "$ROOT/.cursor/rules/"*.mdc "$RULES_ASSETS/"
  echo "updated: kp-install-rules/assets/rules from .cursor/rules"
fi

echo "Done."
