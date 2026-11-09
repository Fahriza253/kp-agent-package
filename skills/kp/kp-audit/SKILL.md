---
name: kp-audit
description: Audit untuk Laporan Kerja Praktik Teknik Informatika UNPI Cianjur dalam empat mode. Mode gap mencari celah improvement (argumen, bukti, konsistensi, kelengkapan) dan menyusunnya menjadi daftar prioritas tanpa mengubah naskah. Mode audit memeriksa menyeluruh. Mode validate menjalankan pemeriksaan mekanis. Dipakai untuk intent IMPROVE, AUDIT, dan VALIDATE.
---

# KP Audit

Skill ini memeriksa naskah. Mode `gap`, `audit`, dan `validate` tidak mengubah berkas. Setiap temuan menunjuk lokasi yang bisa diperiksa ulang.

## 1. Mode

| Mode       | Tujuan                                                                 | Keluaran                                              | Mengubah berkas |
| ---------- | ---------------------------------------------------------------------- | ----------------------------------------------------- | --------------- |
| `gap`      | Menemukan celah improvement: apa yang lemah, kurang, atau bisa diperkuat | Daftar celah berprioritas dengan usulan perbaikan    | Tidak           |
| `audit`    | Pemeriksaan menyeluruh sebelum bimbingan atau sebelum dianggap final   | Laporan temuan per kategori dengan tingkat keparahan  | Tidak           |
| `validate` | Pemeriksaan mekanis format, sitasi, tanda baca, dan penanda            | Daftar pelanggaran mekanis                            | Tidak           |

Mode `gap` adalah mode utama untuk mencari celah improvement. Mode ini bersifat mencari dan menilai, bukan menulis ulang. Perbaikan dikerjakan lewat intent REVISE setelah pengguna memilih celah mana yang akan diperbaiki.

## 2. Mode gap (celah improvement)

Tujuan mode ini adalah menjawab: di mana laporan bisa menjadi lebih kuat secara akademik, dan apa langkah perbaikan terkecil yang paling berdampak.

### 2.1 Kategori yang diperiksa

**A. Argumen.** Apakah rumusan masalah dijawab oleh pembahasan? Apakah kesimpulan mengikuti dari bab IV dan V? Apakah ada lompatan logika antarparagraf atau antarbagian? Gunakan reverse outline (lihat `academic-writing-core` bagian 2) untuk setiap bab.

**B. Bukti.** Di mana klaim belum punya sumber atau bukti? Di mana kata kerja melebihi kekuatan bukti? Apakah landasan teori di BAB II mendukung pembahasan di BAB IV? Apakah sumber sudah cukup mutakhir dan relevan?

**C. Keterlacakan.** Apakah setiap masalah dapat ditelusuri ke tujuan, kebutuhan, rancangan, implementasi, dan pengujian? Di mana rantai putus?

**D. Konsistensi.** Istilah, angka, nama, dan scope sama di semua bab. Batas integrasi Neofeeder konsisten dengan dokumentasi. Pekerjaan rutin staf dan proyek KP tidak tercampur.

**E. Kelengkapan.** Apakah isi wajib pedoman tiap bab terpenuhi (lihat `kp-10`)? Apakah batasan masalah dan keterbatasan penelitian dinyatakan? Apakah saran di BAB VI berangkat dari keterbatasan yang tertulis?

**F. Kejelasan.** Apakah paragraf punya satu gagasan utama? Apakah ada kalimat yang terlalu panjang atau istilah yang didefinisikan belakangan? Apakah subbab punya fungsi yang jelas?

**G. Nilai akademik KP.** Apakah kontribusi laporan jelas: penerapan yang benar, kebutuhan nyata, dan bukti pelaksanaan? Apakah klaim kebaruan memiliki dasar telaah pustaka? Jika tidak, usulkan untuk ditelusuri, jangan dinyatakan sebagai fakta.

### 2.2 Cara menilai

Untuk setiap celah, tentukan:

- **Dampak akademik**: tinggi, sedang, atau rendah, berdasarkan seberapa besar celah ini memengaruhi kesimpulan atau penilaian pembimbing.
- **Upaya**: kecil (kalimat atau paragraf), sedang (satu subbab), atau besar (perlu sumber baru, data baru, atau perubahan struktur).
- **Ketergantungan**: apakah perbaikan butuh data, sumber, atau keputusan pengguna. Jika ya, tandai `butuh konfirmasi`.

Prioritaskan celah dengan dampak tinggi dan upaya kecil. Celah yang butuh data atau sumber baru tidak boleh diusulkan dengan cara mengarang bukti.

### 2.3 Format keluaran

Tabel dengan kolom: nomor, kategori, lokasi, celah, dampak, upaya, usulan perbaikan, butuh konfirmasi.

Setelah tabel, tampilkan:

1. Tiga celah prioritas teratas dengan alasan singkat.
2. Celah yang perlu data atau sumber dari pengguna, dengan pertanyaan spesifik yang harus dijawab.
3. Saran urutan pengerjaan dalam tiga langkah.

Jika pengguna meminta rentang yang lebih sempit (misalnya hanya BAB IV), batasi pemeriksaan pada bagian itu dan sebutkan batasannya di awal.

### 2.4 Batasan mode gap

- Usulan perbaikan berupa arah atau kalimat contoh singkat, bukan paragraf final. Penulisan final dikerjakan lewat `kp-draft-section`.
- Jangan menyatakan bahwa klaim salah jika bukti yang ada hanya belum dicantumkan di naskah. Bedakan "tidak ada bukti" dari "bukti ada tetapi belum ditulis".
- Jangan menilai kualitas sistem dari naskah saja. Jika pertanyaan menyangkut implementasi dan **Submodule SIAKAD** = dipakai di `progress-laporan.md`, periksa dokumentasi dan kode di submodule `siakad/` (branch `dev`) sesuai `AGENTS.md`.

## 3. Mode audit (menyeluruh)

Jalankan semua pemeriksaan `validate` dan `gap`, lalu tambahkan pemeriksaan kepatuhan pedoman:

- Urutan dan judul bab sesuai pedoman, termasuk BAB III.A untuk bagian awal dan akhir.
- Bab V tidak memiliki subjudul tersendiri (keputusan pengguna, lihat `kp-10`).
- Isi wajib BAB IV dan BAB VI terpenuhi.
- Sitasi sesuai `kp-20`, termasuk penggunaan *et al.* untuk tiga penulis atau lebih dan *n.d.* untuk tanggal tidak tersedia. Entri *t.t.* dan *dkk.* di draf ditandai sebagai pelanggaran untuk migrasi.
- Klaim tentang hasil uji hanya muncul jika ada bukti pelaksanaan.

Keluaran dibagi per kategori dengan tingkat **Kritis**, **Mayor**, atau **Minor**:

- **Kritis**: melanggar pedoman wajib, klaim tidak benar, atau bukti tidak dapat ditelusuri.
- **Mayor**: inkonsistensi antarbagian, klaim tanpa bukti, sitasi tidak cocok.
- **Minor**: ejaan, format, penomoran, gaya.

## 4. Mode validate (mekanis)

1. Jalankan `python scripts/check_project_markdown.py` dan laporkan hasilnya apa adanya.
2. Karena skrip mengecualikan `laporan/archive/`, periksa `laporan/ARCHIVE/DRAFT_KP.md` secara terpisah untuk karakter U+2014. Ini celah yang sudah diketahui. Laporkan hasilnya meskipun skrip lulus.
3. Cari penanda `[KONFIRMASI:`, `[PERLU SUMBER:`, dan `[PERLU VERIFIKASI SUMBER]`. Laporkan sebagai daftar yang harus diselesaikan.
4. Cari *sehingga* dan *sedangkan* di awal kalimat. Laporkan sebagai pelanggaran mayor dan daftar lokasinya.
5. Cari "di mana" dan "dari" sebagai terjemahan langsung dari *where* dan *of*.
6. Cari istilah "MVP" dalam naskah akhir.
7. Cari tanda hubung di depan rincian yang tidak diberi nomor atau huruf.
8. Periksa penomoran tabel dan gambar serta penempatan judul tabel dan gambar. Dalam draf saat ini belum ada tabel atau gambar, jadi pemeriksaan ini dilewati sampai ada.
9. Periksa daftar sitasi terhadap `kp-20`.

## 5. Aturan umum

- Jangan mengubah naskah dalam mode `gap`, `audit`, atau `validate`. Jika pengguna meminta perbaikan, gunakan intent REVISE.
- Jangan melaporkan sebagai temuan hal yang sudah diputuskan pengguna. Periksa `docs/agents/progress-laporan.md` terlebih dahulu.
- Jika tidak ada temuan di satu kategori, tulis "tidak ada temuan" untuk kategori itu.
