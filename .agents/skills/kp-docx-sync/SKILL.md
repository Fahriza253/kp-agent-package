---
name: kp-docx-sync
description: Menyinkronkan perubahan dari naskah Markdown kerja (laporan/ARCHIVE/DRAFT_KP.md) ke DOCX lewat scripts/generate_laporan_docx.py. Hasil selalu berkas baru di laporan/GENERATED/, naskah Word resmi tidak pernah ditimpa. Dipakai untuk intent SYNC. Setiap langkah yang membuat berkas memerlukan konfirmasi.
---

# KP DOCX Sync

Skill ini mengatur cara perubahan teks dibawa ke DOCX. Naskah Word resmi adalah acuan format final. Markdown tidak menggantikan paginasi, gaya institusi, atau penyerahan.

Dokumentasi rinci untuk generator ada di `docs/agents/generate-laporan-docx.md`. Alur naskah ada di `docs/agents/laporan-naskah.md`. Skill ini hanya merangkum yang dibutuhkan untuk menjalankannya.

## 1. Aturan

- Naskah Word resmi `laporan/DRAFT LAPORAN KP - SIAKAD FT - DAFA FAWAZ.docx` tidak boleh ditimpa. Generator menjaga ini dengan menolak `--out` yang sudah ada.
- Jangan jalankan generator dengan `--out` yang mengarah ke naskah Word resmi, kecuali pengguna meminta dan memahami risikonya.
- Template di `laporan/` tidak diubah.
- Setiap pembuatan DOCX memerlukan konfirmasi pengguna: sumber, output, dan bagian yang berubah.
- Gambar dari Markdown tidak di-embed. Generator menulis catatan kuning untuk sisip manual.

## 2. Alur

1. **Pastikan Markdown sudah final untuk bagian yang disinkronkan.** Jalankan `kp-audit` mode validate. Jangan sinkronkan jika masih ada penanda `[KONFIRMASI:]` atau `[PERLU SUMBER:]` tanpa persetujuan pengguna.
2. **Tampilkan rencana.** Sumber, output yang diusulkan (default `laporan/GENERATED/`), dan daftar gambar yang perlu sisip manual.
3. **Tunggu konfirmasi.**
4. **Jalankan generator** dari akar repositori:

   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -r scripts/requirements-docx.txt
   .venv/bin/python scripts/generate_laporan_docx.py
   ```

   Untuk uji tanpa menyentuh folder output resmi, gunakan `--out /tmp/naskah-uji.docx`.

5. **Verifikasi** hasil. Laporkan sebagai daftar: nomor bab dan subbab, urutan bagian, daftar pustaka, dan jumlah catatan gambar yang tercetak oleh skrip.
6. **Serahkan** jalur berkas hasil. Jika lingkungan mendukung `present_files`, gunakan itu.
7. **Catat** di `docs/agents/progress-laporan.md` bila pengguna meminta.

## 3. Batasan Markdown ke Word

Dari dokumentasi generator dan pemeriksaan draf:

- **Didukung**: heading BAB dan subbab, paragraf, daftar bernomor, daftar pustaka, tebal, miring, kode inline, tautan.
- **Tidak direplikasi persis**: tabel (baris diawali `|` diperlakukan sebagai teks dengan peringatan), blok kode fence, blockquote, heading level 5 dan 6.
- **Tidak di-embed**: gambar. Diganti catatan kuning.
- **Di luar cakupan skrip**: daftar isi otomatis, daftar gambar dan tabel, nomor halaman, margin khusus bagian awal.

Saat ini draf `DRAFT_KP.md` tidak memuat tabel, gambar, atau blok kode, sehingga keterbatasan ini belum berdampak. Jika bagian baru memuatnya, periksa hasil generate secara manual lebih ketat.

## 4. Checklist setelah generate

1. Buka output di Word. Periksa nomor bab dan subbab, spasi, dan daftar pustaka.
2. Sisipkan semua gambar menggantikan catatan kuning.
3. Perbarui daftar isi, daftar gambar, dan daftar tabel jika template memakainya.
4. Jika naskah resmi perlu ikut terbarui, salin bagian yang disetujui ke naskah Word resmi atau ikuti prosedur penyerahan yang ditetapkan pengguna.

## 5. Yang tidak boleh dilakukan

- Menimpa atau menghapus naskah Word resmi.
- Mengubah template untuk memperbaiki hasil generator tanpa persetujuan.
- Menyatakan DOCX final tanpa pemeriksaan manual oleh pengguna.
- Mengandalkan `pandoc` atau konverter lain tanpa permintaan eksplisit. Skrip ini dipilih karena memetakan gaya template KP.
