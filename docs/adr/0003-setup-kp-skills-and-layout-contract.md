# ADR-0003: Skill setup-kp-* dan kontrak layout repo laporan

## Status

Accepted (2026-11-09).

## Context

Skill KP (`kp-intent-router`, `kp-audit`, `kp-docx-sync`, dan lain-lain) mengasumsikan path tetap di repo laporan pengguna (`docs/agents/`, `laporan/ARCHIVE/`, `scripts/`, `resources/`, dan sejenisnya). Hanya `kp-install-rules` yang memasang rules; tidak ada langkah terpusat untuk scaffold, skrip, atau verifikasi. Beberapa artefak (misalnya `check_project_markdown.py`) dirujuk di `kp-00` tetapi tidak ada di paket agen. Nama DOCX resmi ter-hardcode untuk satu contoh mahasiswa.

## Decision

1. **Keluarga skill bootstrap**: `setup-kp-repo` (orchestrator), `setup-kp-scaffold`, `setup-kp-rules`, `setup-kp-tooling`. `kp-install-rules` tetap sebagai alias bundle rules yang sama.
2. **Bundle tooling**: skrip minimum disimpan di `setup-kp-tooling/assets/scripts/` dan disalin ke `scripts/` repo laporan lewat `install-tooling.sh`.
3. **Kontrak layout**: folder kanonik tidak dikonfigurasi per path; hanya field `[KONFIRMASI:]` di `progress-laporan.md` (judul, path DOCX, status submodule).
4. **DOCX resmi**: otoritas path pindah ke kolom **Naskah Word resmi** di progress; `kp-00` dan `kp-docx-sync` tidak memakai nama berkas mahasiswa tertentu.
5. **Submodule `siakad/`**: opsional; progress memuat **Submodule SIAKAD** (`dipakai` / `tidak dipakai`).
6. **Intent SETUP**: `kp-intent-router` memuat keluarga setup bila progress atau draf belum ada.
7. **Artefak manual**: pedoman kampus, DOCX resmi, dan `.custom-skills/my-research-paper-writing/` tetap tanggung jawab pengguna (sumber per mahasiswa atau kampus).

## Consequences

- README dan onboarding menjelaskan urutan `npx skills add` lalu `setup-kp-repo` (atau langkah terpisah).
- Maintainer menyinkronkan rules ke `kp-install-rules` dan `setup-kp-rules` lewat `sync_catalog_to_agents.sh`.
- Generator DOCX di bundle bersifat minimal; repo referensi boleh mengganti skrip setelah konfirmasi.
