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

for rules_skill in kp-install-rules setup-kp-rules; do
  RULES_ASSETS="$ROOT/skills/kp/$rules_skill/assets/rules"
  if [ -d "$(dirname "$RULES_ASSETS")" ]; then
    mkdir -p "$RULES_ASSETS"
    cp "$ROOT/.cursor/rules/"*.mdc "$RULES_ASSETS/"
    echo "updated: skills/kp/$rules_skill/assets/rules from .cursor/rules"
  fi
done

echo "Done."
