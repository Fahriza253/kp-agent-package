---
name: kp-draft-section
description: Menulis atau merevisi satu bab atau subbab Laporan Kerja Praktik Teknik Informatika UNPI Cianjur. Dibangun di atas academic-writing-core, mengikuti pedoman KP 2026, dan memakai draf, sumber proyek, serta masukan pembimbing. Gunakan untuk intent DRAFT dan REVISE.
---

# KP Draft Section

Skill ini menulis atau merevisi satu bagian laporan. Prinsip penulisan umum ada di `academic-writing-core`. Skill ini hanya menambahkan konteks dan aturan KP.

## 1. Prasyarat

Sebelum menulis, pastikan sudah membaca:

1. `docs/agents/progress-laporan.md` (status dan keputusan terbuka);
   `docs/agents/penulisan-kp-skills.md` (prosedur wajib penulisan draft KP);
2. `kp-00-core.mdc` dan `kp-10-pedoman-format.mdc` (dimuat otomatis, periksa kembali bila perlu);
3. bagian pedoman yang relevan dengan bab itu;
4. bagian draf yang akan diubah, beserta satu bagian sebelum dan sesudahnya;
5. `revisi/` bila ada catatan pembimbing yang menyentuh bagian ini;
6. sumber proyek yang relevan dengan bagian itu (lihat tabel di bagian 3).

Sesuai `docs/agents/penulisan-kp-skills.md`, tiga berkas di `.custom-skills/my-research-paper-writing/` adalah skill wajib untuk menulis draft. Berkas itu berisi rincian per bab, yang tidak perlu disalin ke skill ini. Urutannya: `research-paper-writing-skills.md` (bagian relevan, hierarki sumber §3, workflow §4), `human-academic-writing-kp-skills.md` (§2.2 dan §3), lalu `does-my-writing-flow-skills.md` (§2 sampai §3) untuk paragraf naratif. Skill `academic-writing-core` di paket ini melengkapi, bukan menggantikan, ketiga berkas itu.

Jangan membaca seluruh draf atau seluruh dokumentasi sekaligus kecuali diminta.

## 2. Alur

**Langkah 1. Tentukan fungsi bagian.** Tulis satu kalimat: bagian ini harus membuat pembaca tahu atau percaya apa, dan bagaimana posisinya dalam alur bab.

**Langkah 2. Periksa keterkaitan.** Pastikan bagian ini mendukung rumusan masalah, tujuan, dan bagian berikutnya. Jika tidak, catat sebagai isu konsistensi.

**Langkah 3. Outline 3 sampai 7 poin.** Tampilkan outline ke pengguna sebelum menulis panjang.

**Langkah 4. Peta klaim-bukti.** Untuk setiap klaim yang bersifat fakta tentang sistem, perusahaan, atau hasil, tulis sumbernya. Jika sumbernya belum ada, tandai `[KONFIRMASI: ...]` atau `[PERLU SUMBER: ...]`.

**Langkah 5. Tulis draf.** Tulis hanya setelah outline disetujui atau bila pengguna meminta langsung. Ikuti aturan di `kp-10` dan `academic-writing-core`.

**Langkah 6. Periksa.** Reverse outline, konsistensi istilah dan angka, dan keberadaan penanda konfirmasi.

**Langkah 7. Serahkan.** Tampilkan teks, peta klaim-bukti, catatan konsistensi, dan daftar penanda konfirmasi. Tanyakan apakah teks boleh dimasukkan ke `DRAFT_KP.md`.

## 3. Sumber per bagian

| Bagian                       | Sumber utama                                                                 | Catatan                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| BAB I Pendahuluan            | `resources/PEDOMAN-KP-2026.md` (BAB III.B.1.1 sampai 1.8), draf, `revisi/`  | Latar belakang tidak boleh menyatakan kondisi lembaga yang tidak didukung catatan penulis. Revisi dari pembimbing di `revisi/` harus diperiksa lebih dulu |
| BAB II Kajian Pustaka        | Profil lembaga: sumber resmi lembaga. Landasan teori: jurnal dan buku terverifikasi | Bagian profil dan landasan teori harus dapat ditelusuri ke sumber                       |
| BAB III Sarana dan Prasarana | Dokumentasi teknis proyek, `siakad/` (branch `dev`), `package.json` atau sejenis | Verifikasi versi dan perangkat dengan berkas nyata, bukan catatan developer              |
| BAB IV Analisis dan Pembahasan | Dokumentasi domain di `siakad/docs/siakad/`, aturan bisnis, `revisi/`        | Scope integrasi Neofeeder harus sesuai dokumentasi, bukan asumsi                         |
| BAB V Implementasi dan Pengujian | Kode, migrasi, skenario uji, hasil uji aktual                             | Jangan menyatakan uji yang belum dijalankan sebagai hasil                                |
| BAB VI Penutup               | Bab I sampai V yang sudah final                                              | Kesimpulan hanya dari pembahasan. Saran berangkat dari keterbatasan yang dinyatakan     |

Keterangan: draf per Bab IV saat ini memuat bagian 4.1 sampai 4.7, dan belum memuat bagian awal (prakata, daftar isi, pengesahan) maupun lampiran. BAB V dan BAB VI belum ada di draf `DRAFT_KP.md`. Untuk BAB V, ikuti pedoman: satu bab terpadu tanpa subjudul tersendiri. Untuk BAB VI, ikuti 6.1 Kesimpulan dan 6.2 Saran.

## 4. Aturan khusus KP

- **Pemisahan tugas.** Pekerjaan rutin penulis sebagai staf hanya boleh menjadi sumber pengamatan. Pekerjaan itu bukan luaran KP kecuali dinyatakan sebaliknya oleh pengguna.
- **Scope SIAKAD.** SIAKAD adalah sistem operasional internal. Ia bukan pengganti Neofeeder atau PDDIKTI. Sebutkan batas integrasi sesuai dokumentasi.
- **Istilah.** Jangan memakai "MVP" dalam naskah akhir. Gunakan "cakupan pengembangan awal" atau istilah lain yang disetujui pengguna.
- **Keputusan teknis.** Jangan memindahkan keputusan teknis ke laporan tanpa menilai relevansi akademiknya. Pilih detail yang membuktikan bagaimana solusi menjawab kebutuhan, bukan semua detail implementasi.
- **Daftar pustaka.** Setiap sumber baru mengikuti `kp-20`, dan penambahan sumber memerlukan konfirmasi.

## 5. Mode revisi

Dalam mode revisi:

1. Pertahankan bagian yang sudah benar. Ubah hanya bagian yang diperlukan.
2. Tampilkan perbandingan singkat: versi asli dan revisi, untuk setiap perubahan yang substantif.
3. Jika perubahan memengaruhi bagian lain, daftar bagian itu dan tanyakan apakah perlu ikut diubah.
4. Jika mengubah identifikasi masalah, periksa rumusan masalah, tujuan, batasan, BAB IV, BAB V, dan kesimpulan.
5. Jika mengubah scope sistem, periksa dokumentasi proyek dan semua klaim yang terpengaruh.

## 6. Yang tidak boleh dilakukan

- Menulis hasil pengujian, angka kinerja, atau tanggal tanpa sumber.
- Menambah fitur atau kemampuan sistem yang tidak tercantum dalam dokumentasi atau kode.
- Menggunakan "berhasil", "mampu", atau "terbukti" untuk fitur yang belum diuji.
- Mengganti kata "diharapkan dapat" menjadi pernyataan pasti.
- Menambahkan pengalaman pribadi atau observasi yang tidak dilakukan.
