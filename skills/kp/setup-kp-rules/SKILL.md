---
name: setup-kp-rules
description: Memasang rules Cursor untuk penulisan Laporan KP (.mdc) ke workspace pengguna. Gunakan setelah npx skills add atau sebagai bagian setup-kp-repo. Pengganti operasional untuk kp-install-rules.
---

# Setup KP Rules

Rules KP tidak ikut instalasi `npx skills`. Skill ini memasang bundle rules dari paket ke `.cursor/rules/` workspace.

## Prasyarat

- Skill KP terpasang lewat Skills CLI (disarankan).
- Agen dijalankan dari **root repositori laporan** pengguna.

## Langkah

1. Konfirmasi path root workspace (default: direktori kerja saat ini).
2. Jalankan:

   ```bash
   bash .agents/skills/setup-kp-rules/scripts/install-rules.sh .
   ```

   Dari repo pemeliharaan paket:

   ```bash
   bash skills/kp/setup-kp-rules/scripts/install-rules.sh /path/ke/repo-laporan
   ```

3. Verifikasi berkas ada: `kp-00-core.mdc`, `kp-10-pedoman-format.mdc`, `kp-20-sitasi-apa.mdc`.
4. Ingatkan: tabel sumber kebenaran di `kp-00-core.mdc` mengasumsikan kontrak layout setelah `setup-kp-scaffold`. Path DOCX resmi mengacu ke `docs/agents/progress-laporan.md`, bukan nama berkas tetap.

## Alias

Skill `kp-install-rules` memanggil bundle yang sama. Untuk bootstrap baru, utamakan `setup-kp-rules` atau orchestrator `setup-kp-repo`.

## Bila rules bentrok

Jika `.cursor/rules/` sudah berisi rules lain, gabungkan manual atau backup dulu. Jangan menghapus rules pengguna tanpa konfirmasi.
