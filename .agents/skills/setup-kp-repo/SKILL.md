---
name: setup-kp-repo
description: Mengorkestrasi bootstrap repo laporan KP baru (rules, scaffold, tooling, verifikasi). Submodule siakad opsional. Dipakai untuk intent SETUP di kp-intent-router.
---

# Setup KP Repo

Skill ini memandu penyiapan repo laporan sebelum `kp-intent-router` produktif untuk DRAFT, AUDIT, atau SYNC.

## Kapan dipakai

- Repo baru atau belum punya `docs/agents/progress-laporan.md`.
- Pengguna meminta "setup repo KP", "bootstrap laporan", atau intent **SETUP**.

## Urutan (setelah konfirmasi pengguna untuk setiap langkah yang menulis berkas)

1. **Skill CLI** (instruksikan pengguna jika belum):

   ```bash
   npx skills@latest add Fahriza253/kp-agent-package -a cursor
   ```

   Repositori: https://github.com/Fahriza253/kp-agent-package

2. **Rules** (`setup-kp-rules`):

   ```bash
   bash .agents/skills/setup-kp-rules/scripts/install-rules.sh .
   ```

   `kp-install-rules` tidak lagi disarankan (alias lama); gunakan `setup-kp-rules`.

3. **Scaffold** (`setup-kp-scaffold`):

   ```bash
   bash .agents/skills/setup-kp-scaffold/scripts/scaffold.sh .
   ```

4. **Tooling** (`setup-kp-tooling`):

   ```bash
   bash .agents/skills/setup-kp-tooling/scripts/install-tooling.sh .
   ```

5. **Verifikasi**:

   ```bash
   bash .agents/skills/setup-kp-repo/scripts/verify-layout.sh .
   python scripts/check_project_markdown.py
   ```

6. **Isian manual (wajib, tidak otomatis)**:
   - Salin pedoman ke `resources/PEDOMAN-KP-2026.md`.
   - Salin DOCX resmi ke `laporan/`; catat path pasti di baris **Naskah Word resmi** pada `docs/agents/progress-laporan.md`.
   - Isi judul KP dan status submodule SIAKAD (`dipakai` / `tidak dipakai`) di progress.
7. **Submodule SIAKAD (opsional, default disarankan untuk proyek implementasi)**:
   - Jika dipakai: `git submodule add <url-siakad> siakad` dan checkout branch `dev` sesuai kebijakan tim.
   - Jika tidak: set **Submodule SIAKAD** ke `tidak dipakai` di progress; agen tidak boleh mengasumsikan path `siakad/` ada.

8. **Tutup bootstrap**: perbarui tabel **Bootstrap repo** di `docs/agents/progress-laporan.md` menjadi `selesai` per langkah yang sudah dilakukan.

## Checklist cepat

| Langkah | Skill / tindakan |
| ------- | ---------------- |
| Rules `.mdc` | `setup-kp-rules` |
| Folder dan progress | `setup-kp-scaffold` |
| `scripts/` | `setup-kp-tooling` |
| Pedoman, DOCX | manual pengguna |
| `siakad/` | opsional git submodule |
| Verifikasi | `verify-layout.sh` |

## Yang tidak dilakukan otomatis

- Mengisi sitasi, judul final, atau isi BAB.
- Menambah kutipan jurnal.
- Menginisialisasi submodule tanpa URL dan konfirmasi.
- Menimpa DOCX atau draf yang sudah berisi teks.

## Kontrak dokumen

Peta dependensi skill dan path: `references/workspace-document-contract.md` (dalam skill ini). Salinan di repo laporan: `docs/agents/workspace-document-contract.md` setelah scaffold.

## Setelah setup

Arahkan pengguna ke `kp-intent-router` dengan intent STATUS atau DRAFT.

Panduan contoh sesi berikutnya (paket): `docs/agents/panduan-penggunaan-skills.md`.
