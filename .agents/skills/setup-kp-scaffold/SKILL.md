---
name: setup-kp-scaffold
description: Membuat kerangka folder dan berkas minimum repo laporan KP (progress, draf kosong, docs/agents, resources). Tidak menimpa berkas yang sudah ada. Bagian dari keluarga setup-kp-*.
---

# Setup KP Scaffold

Skill ini memenuhi **kontrak layout** yang direferensikan `kp-00-core.mdc` tanpa mengisi pedoman kampus, DOCX resmi, atau submodule.

## Prasyarat

- Root workspace adalah repo laporan (boleh repo kosong atau baru di-init git).
- Jalankan dari direktori yang akan menjadi akar repo.

## Langkah

1. Konfirmasi path root workspace.
2. Jalankan:

   ```bash
   bash .agents/skills/setup-kp-scaffold/scripts/scaffold.sh .
   ```

3. Minta pengguna mengisi di `docs/agents/progress-laporan.md`: judul, path DOCX resmi, dan apakah submodule `siakad/` dipakai.
4. Ingatkan: salin `resources/PEDOMAN-KP-2026.md`; salin DOCX resmi ke `laporan/`. Panduan draft sudah di `docs/agents/draft-guides/` (sesuaikan konteks proyek di progress).

## Yang dibuat

| Path | Keterangan |
| ---- | ---------- |
| `docs/agents/progress-laporan.md` | Template dengan tabel bootstrap |
| `laporan/ARCHIVE/DRAFT_KP.md` | Stub naskah |
| `docs/agents/penulisan-kp-skills.md`, `laporan-naskah.md`, `generate-laporan-docx.md` | Panduan minimum |
| `GLOSSARY.md`, `AGENTS.md` (akar repo) | Stub glosarium proyek dan konfirmasi jurnal |
| `docs/agents/draft-guides/` | Panduan modular penulisan per bab |
| `resources/README.md` | Petunjuk pedoman |
| `revisi/`, `docs/agents/knowledge/`, `resources/journal/`, `laporan/GENERATED/` | Folder kosong |

Skrip **tidak** menimpa berkas yang sudah ada.

## Yang tidak dibuat otomatis

- `resources/PEDOMAN-KP-2026.md`
- Naskah Word resmi di `laporan/`
- Submodule `siakad/` (lihat `setup-kp-repo` langkah opsional)
