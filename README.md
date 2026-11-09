# Paket Agen Penulisan Laporan KP (Cursor)

Paket ini berisi rules dan skill Cursor untuk membantu penulisan Laporan Kerja Praktik Teknik Informatika UNPI Cianjur. Strukturnya memisahkan lapisan reusable (dapat dipakai untuk skripsi atau makalah lain) dari lapisan khusus KP.

## Isi paket

```
.cursor/
  rules/                       Aturan yang selalu atau sering aktif
    kp-00-core.mdc             Aturan inti (selalu aktif)
    kp-10-pedoman-format.mdc   Struktur dan format pedoman (aktif di laporan/)
    kp-20-sitasi-apa.mdc       Sitasi dan daftar pustaka (aktif di laporan/)
  skills/                      Skill yang dimuat sesuai tugas
    academic-writing-core/     REUSABLE. Disiplin penulisan akademik umum
    academic-humanize/         REUSABLE. Penghapusan pola mekanis, dengan daftar perubahan
    kp-intent-router/          KP. Titik masuk: baca status, tentukan intent, muat skill
    kp-draft-section/          KP. Menulis atau merevisi satu bab atau subbab
    kp-ideation/               KP. Brainstorm dan adu gagasan, tanpa mengubah naskah
    kp-audit/                  KP. Mode gap (celah improvement), audit, dan validate
    kp-source-learning/        KP. Belajar dari sumber menjadi catatan pola
    kp-docx-sync/              KP. Sinkronisasi Markdown ke DOCX lewat generator
docs/agents/
  progress-laporan.md          Status kemajuan, dibaca pertama oleh agen
```

## Status saat ini

Paket ini bisa dipasang sekarang. Semua rujukan di rules dan skill mengarah ke berkas yang sudah ada di repositori, atau sudah ada di unggahan (`scripts/check_project_markdown.py`, `docs/agents/penulisan-kp-skills.md`, `docs/agents/laporan-naskah.md`, `docs/agents/generate-laporan-docx.md`, `docs/agents/domain.md`).

Yang sudah diuji di repositori tiruan:

- `scripts/check_project_markdown.py` berjalan dan mendeteksi em dash di akar repositori.
- Skrip itu melewati `laporan/archive/`, sehingga `DRAFT_KP.md` tidak terperiksa otomatis (sudah ditangani di `kp-audit` mode validate).
- Nama setiap skill sama dengan nama foldernya, dan setiap rules punya frontmatter.

Yang belum diuji:

- Generator DOCX belum dijalankan, karena template Word resmi tidak ada di unggahan.
- Perilaku Cursor (globs, alwaysApply, pemuatan skill) belum diuji di Cursor sendiri.

## Pemasangan

1. Salin folder `.cursor/` ke root repositori laporan, sejajar dengan `AGENTS.md`. Jika repositori sudah punya `.cursor/`, gabungkan isinya.
2. Salin `docs/agents/progress-laporan.md`, lalu isi bagian status sesuai kondisi sekarang.
3. Buat folder `docs/agents/knowledge/` (kosong) untuk hasil belajar dari sumber.
4. Pastikan rujukan di rules dan skill masih ada: `resources/PEDOMAN-KP-2026.md`, `laporan/ARCHIVE/DRAFT_KP.md`, `scripts/check_project_markdown.py`, `scripts/generate_laporan_docx.py`, `docs/agents/generate-laporan-docx.md`. Jika belum ada, buat atau sesuaikan path.
5. Buka Cursor, lalu mulai sesi baru dengan permintaan seperti: "Cek posisi laporan, lalu ringkas BAB IV."

## Cara kerja agen

1. `kp-00-core.mdc` selalu aktif. Ia menetapkan bahasa, sumber kebenaran, daftar konfirmasi, dan aturan anti-fabrikasi.
2. Tugas dimulai dari `kp-intent-router`. Skill ini membaca `progress-laporan.md`, menentukan intent, lalu memuat skill yang relevan.
3. Untuk menulis atau merevisi, `kp-draft-section` memanggil `academic-writing-core` dan rules format serta sitasi.
4. Setelah draf selesai, pengguna dapat meminta `kp-audit` atau memanggil agen lain untuk `academic-humanize`. Agen lain harus membaca rules proyek dan menerima brief serah terima.
5. Perubahan substantif, sitasi baru, penulisan ke knowledge base, dan pembuatan DOCX selalu menunggu konfirmasi.

## Peta intent

| Intent     | Skill utama                    |
| ---------- | ------------------------------ |
| BRAINSTORM | kp-ideation                    |
| DRAFT      | kp-draft-section               |
| REVISE     | kp-draft-section (mode revisi) |
| AUDIT      | kp-audit (audit)               |
| IMPROVE    | kp-audit (gap)                 |
| VALIDATE   | kp-audit (validate)            |
| LEARN      | kp-source-learning             |
| HUMANIZE   | academic-humanize              |
| SYNC       | kp-docx-sync                   |
| STATUS     | progress-laporan.md            |

Catatan penamaan: di dalam skill, singkatan `kp-10` dan `kp-20` merujuk ke `kp-10-pedoman-format.mdc` dan `kp-20-sitasi-apa.mdc`.

## Memakai ulang di proyek lain

- Salin `academic-writing-core` dan `academic-humanize` apa adanya. Keduanya tidak memuat aturan KP.
- Untuk skripsi atau makalah lain, buat ulang lapisan proyek: rules format dan sitasi sesuai pedoman baru, lalu skill `kp-draft-section` versi baru yang menunjuk ke sumber proyek itu.
- Jangan menyalin `kp-00-core.mdc` tanpa mengganti path sumber kebenaran dan daftar konfirmasi.

## Keputusan atas konflik

Keputusan pengguna sudah diterapkan di rules dan skill:

1. Bab V mengikuti pedoman, tanpa subjudul tersendiri.
2. _Sehingga_ dan _sedangkan_ tidak boleh di awal kalimat. Kemunculannya di draf didaftar, tidak diubah otomatis.
3. Sitasi tiga penulis atau lebih memakai _et al._, tanggal tidak tersedia memakai _n.d._, dan sitasi dua penulis selalu memakai "&".

Migrasi entri _t.t._ di draf ke _n.d._ masih memerlukan konfirmasi per batch. Istilah "Skripsi" pada sampul pedoman dilewati atas permintaan pengguna. Empat berkas di `uploads/` juga ada dalam dua versi dengan akhiran `_1` yang isinya identik, sehingga cukup satu salinan yang dipakai.

## Yang perlu diverifikasi sebelum dipakai

- Versi APA yang berlaku. Saat paket ini dibuat, edisi ke-7 (2019) yang terkonfirmasi. Edisi lebih baru belum terverifikasi dan harus dicek di apastyle.apa.org.
- Perilaku Cursor untuk `globs` dan `alwaysApply` pada versi yang dipakai di tim Anda. Cek dokumentasi Cursor terbaru.
- Path skrip dan dokumentasi generator DOCX yang tidak termuat dalam unggahan ini.
