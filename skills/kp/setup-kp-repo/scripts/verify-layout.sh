#!/usr/bin/env bash
# Memeriksa kontrak layout minimum repo laporan KP.
set -euo pipefail

TARGET_ROOT="$(cd "${1:-.}" && pwd)"
FAIL=0

check_path() {
  local label="$1"
  local rel="$2"
  local full="$TARGET_ROOT/$rel"
  if [ -e "$full" ]; then
    echo "OK  $label ($rel)"
  else
    echo "MISS $label ($rel)" >&2
    FAIL=1
  fi
}

check_path "Rules inti" ".cursor/rules/kp-00-core.mdc"
check_path "Rules format" ".cursor/rules/kp-10-pedoman-format.mdc"
check_path "Rules sitasi" ".cursor/rules/kp-20-sitasi-apa.mdc"
check_path "Progress" "docs/agents/progress-laporan.md"
check_path "Draf Markdown" "laporan/ARCHIVE/DRAFT_KP.md"
check_path "Skrip validasi" "scripts/check_project_markdown.py"
check_path "Skrip DOCX" "scripts/generate_laporan_docx.py"
check_path "Deps DOCX" "scripts/requirements-docx.txt"
check_path "Panduan draft" "docs/agents/penulisan-kp-skills.md"
check_path "Indeks draft-guides" "docs/agents/draft-guides/README.md"
check_path "Alur naskah" "docs/agents/laporan-naskah.md"
check_path "Panduan DOCX" "docs/agents/generate-laporan-docx.md"
check_path "Glosarium proyek" "GLOSSARY.md"
check_path "AGENTS laporan" "AGENTS.md"
check_path "Resources README" "resources/README.md"
check_path "Folder knowledge" "docs/agents/knowledge/.gitkeep"
check_path "Folder revisi" "revisi/.gitkeep"
check_path "Folder GENERATED" "laporan/GENERATED/.gitkeep"

warn_path() {
  local label="$1"
  local rel="$2"
  local full="$TARGET_ROOT/$rel"
  if [ -e "$full" ]; then
    echo "OK  $label ($rel)"
  else
    echo "WARN $label ($rel) belum ada (manual atau opsional)" >&2
  fi
}

warn_path "Pedoman kampus" "resources/PEDOMAN-KP-2026.md"

if [ -f "$TARGET_ROOT/docs/agents/progress-laporan.md" ]; then
  if grep -q '\[KONFIRMASI:' "$TARGET_ROOT/docs/agents/progress-laporan.md"; then
    echo "WARN: progress masih memuat penanda [KONFIRMASI:]" >&2
  fi
fi

if [ "$FAIL" -eq 0 ]; then
  echo "Kontrak layout minimum terpenuhi."
  exit 0
fi
echo "Kontrak layout belum lengkap. Jalankan setup-kp-repo atau langkah setup terpisah." >&2
exit 1
