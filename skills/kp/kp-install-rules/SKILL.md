---
name: kp-install-rules
description: Memasang rules Cursor untuk penulisan Laporan KP (.mdc) ke workspace pengguna. Gunakan setelah npx skills add, saat pengguna minta pasang rules, bootstrap repo laporan, atau rules kp-00 belum ada.
---

# KP Install Rules

Rules KP tidak ikut instalasi `npx skills`. Skill ini memasang bundle rules dari paket ke `.cursor/rules/` workspace.

## Prasyarat

- Skill lain KP sudah terpasang lewat Skills CLI (opsional, tetapi disarankan).
- Agen dijalankan dari **root repositori laporan** pengguna.

## Langkah

1. Konfirmasi path root workspace (default: direktori kerja saat ini).
2. Jalankan:

   ```bash
   bash .agents/skills/kp-install-rules/scripts/install-rules.sh .
   ```

   Jika skill dipanggil dari repo pemeliharaan paket, path setara: `bash skills/kp/kp-install-rules/scripts/install-rules.sh /path/ke/repo-laporan`

3. Verifikasi berkas ada: `kp-00-core.mdc`, `kp-10-pedoman-format.mdc`, `kp-20-sitasi-apa.mdc`.
4. Ingatkan pengguna: `kp-00-core.mdc` mengasumsikan path naskah di repo laporan (`laporan/`, `docs/agents/progress-laporan.md`, dll.). Sesuaikan tabel sumber kebenaran bila struktur berbeda.

## Template progress (opsional)

Bundle menyertakan `assets/templates/progress-laporan.md`. Salin ke `docs/agents/progress-laporan.md` hanya setelah konfirmasi pengguna. Jangan menimpa berkas yang sudah berisi status.

## Bila rules bentrok

Jika `.cursor/rules/` sudah berisi rules lain, gabungkan manual atau backup dulu. Jangan menghapus rules pengguna tanpa konfirmasi.
