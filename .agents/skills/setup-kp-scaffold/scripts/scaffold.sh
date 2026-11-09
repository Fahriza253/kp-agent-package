#!/usr/bin/env bash
# Membuat kerangka folder dan berkas minimum repo laporan KP.
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATES="$SKILL_ROOT/assets/templates"
TARGET_ROOT="$(cd "${1:-.}" && pwd)"

mkdir -p \
  "$TARGET_ROOT/laporan/ARCHIVE" \
  "$TARGET_ROOT/laporan/GENERATED" \
  "$TARGET_ROOT/docs/agents/knowledge" \
  "$TARGET_ROOT/revisi" \
  "$TARGET_ROOT/resources/journal"

copy_if_missing() {
  local src="$1"
  local dest="$2"
  if [ -f "$dest" ]; then
    echo "skip (exists): $dest"
    return 0
  fi
  cp "$src" "$dest"
  echo "created: $dest"
}

copy_if_missing "$TEMPLATES/progress-laporan.md" "$TARGET_ROOT/docs/agents/progress-laporan.md"
copy_if_missing "$TEMPLATES/DRAFT_KP.md" "$TARGET_ROOT/laporan/ARCHIVE/DRAFT_KP.md"
copy_if_missing "$TEMPLATES/penulisan-kp-skills.md" "$TARGET_ROOT/docs/agents/penulisan-kp-skills.md"
copy_if_missing "$TEMPLATES/laporan-naskah.md" "$TARGET_ROOT/docs/agents/laporan-naskah.md"
copy_if_missing "$TEMPLATES/generate-laporan-docx.md" "$TARGET_ROOT/docs/agents/generate-laporan-docx.md"
copy_if_missing "$TEMPLATES/resources-README.md" "$TARGET_ROOT/resources/README.md"

for d in "$TARGET_ROOT/docs/agents/knowledge" "$TARGET_ROOT/revisi" "$TARGET_ROOT/resources/journal" "$TARGET_ROOT/laporan/GENERATED"; do
  touch "$d/.gitkeep"
done

echo "Scaffold selesai di $TARGET_ROOT"
