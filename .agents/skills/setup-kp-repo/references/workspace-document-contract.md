# Kontrak dokumen workspace laporan KP

Peta dependensi antara skill KP dan berkas atau folder di **repo laporan pengguna**. Skill `setup-kp-scaffold`, `setup-kp-tooling`, dan `setup-kp-rules` memenuhi baris **otomatis**; baris **manual** tetap tanggung jawab penulis.

## Legenda

| Simbol | Arti |
| ------ | ---- |
| auto | Dibuat skrip setup (`scaffold`, `tooling`, `rules`) |
| manual | Penulis menyalin atau mengisi |
| opsional | Hanya bila dipakai (SIAKAD, jurnal) |

## Tabel sumber kebenaran (`kp-00-core`)

| Path | Status | Skill yang bergantung |
| ---- | ------ | --------------------- |
| `.cursor/rules/kp-00-core.mdc` | auto | Semua intent |
| `.cursor/rules/kp-10-pedoman-format.mdc` | auto | DRAFT, REVISE, VALIDATE, HUMANIZE |
| `.cursor/rules/kp-20-sitasi-apa.mdc` | auto | DRAFT, REVISE, VALIDATE |
| `docs/agents/progress-laporan.md` | auto | Router, draft, audit, docx-sync, ideation (status) |
| `docs/agents/penulisan-kp-skills.md` | auto | `kp-draft-section` |
| `docs/agents/draft-guides/` (4 berkas + README) | auto | `kp-draft-section`, DRAFT, REVISE |
| `docs/agents/laporan-naskah.md` | auto | `kp-docx-sync`, draft (alur naskah) |
| `docs/agents/generate-laporan-docx.md` | auto | `kp-docx-sync` |
| `laporan/ARCHIVE/DRAFT_KP.md` | auto | DRAFT, REVISE, AUDIT, SYNC |
| `scripts/check_project_markdown.py` | auto | `kp-audit` (validate) |
| `scripts/generate_laporan_docx.py` | auto | `kp-docx-sync` |
| `scripts/requirements-docx.txt` | auto | SYNC (venv) |
| `GLOSSARY.md` | auto (stub) | `kp-00`, draft (istilah) |
| `AGENTS.md` | auto (stub) | `kp-20` (konfirmasi jurnal) |
| `resources/README.md` | auto | Indeks pedoman |
| `resources/PEDOMAN-KP-2026.md` | manual | draft, ideation, audit |
| `resources/journal/` | auto (kosong) | LEARN, sitasi (setelah konfirmasi) |
| `docs/agents/knowledge/` | auto (kosong) | `kp-source-learning` |
| `revisi/` | auto (kosong) | REVISE, draft |
| `laporan/GENERATED/` | auto | SYNC |
| DOCX resmi di `laporan/` | manual | progress, SYNC |
| `siakad/` submodule | opsional | BAB III–V bila **Submodule SIAKAD** = dipakai |

## Skill per intent (ringkas)

| Skill | Prasyarat minimum sebelum produktif |
| ----- | ----------------------------------- |
| `kp-intent-router` | `progress-laporan.md` atau intent SETUP |
| `setup-kp-repo` | Skills CLI terpasang; konfirmasi tulis berkas |
| `kp-draft-section` | Scaffold + pedoman + `draft-guides/` + progress |
| `kp-audit` validate | `scripts/check_project_markdown.py` |
| `kp-docx-sync` | Tooling + isi draf + venv deps |
| `kp-source-learning` | Folder `knowledge/` |
| `kp-ideation` | Pedoman disarankan; tidak wajib scaffold penuh |
| `academic-humanize` | Rules KP bila di naskah laporan |

## Verifikasi

```bash
bash .agents/skills/setup-kp-repo/scripts/verify-layout.sh .
```

Setelah bootstrap, isi manual wajib di progress: judul, path DOCX, status submodule SIAKAD, lalu salin pedoman.
