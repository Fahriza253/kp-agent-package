---
name: academic-humanize
description: Skill generik untuk menghapus pola tulisan yang terdengar mekanis atau khas keluaran AI dari teks akademik berbahasa Indonesia atau Inggris, sambil mempertahankan makna, fakta, sitasi, struktur, dan tingkat kepastian klaim. Mengeluarkan teks hasil revisi plus daftar perubahan beserta alasannya. Dapat dijalankan oleh agen terpisah; agen itu wajib mengikuti konvensi proyek melalui lapisan proyek.
---

# Academic Humanize

Skill ini adalah lapisan gaya. Ia tidak mengubah isi. Tujuannya adalah teks yang jelas, spesifik, dan natural untuk pembaca akademik.

## 1. Mode

- **Mode aktif** (default saat pengguna meminta humanize, deslop, rewrite gaya, atau memperbaiki kesan AI): teks diubah, lalu daftar perubahan diberikan.
- **Mode pasif** (default saat skill ini dipakai sebagai lapisan dalam skill lain): hanya memeriksa dan menandai pola, tanpa mengubah teks, kecuali diminta.
- Skill ini hanya berjalan atas permintaan eksplisit. Jangan menjalankan rewrite gaya atas inisiatif sendiri pada teks yang sedang direvisi untuk isi.

## 2. Invariant yang tidak boleh berubah

Setiap revisi wajib mempertahankan:

1. fakta, angka, tanggal, nama, dan istilah teknis;
2. sitasi dan kutipan, termasuk urutan dan tahunnya;
3. ruang lingkup yang dinyatakan;
4. pembedaan antara kondisi berjalan, masalah, kebutuhan, rancangan, implementasi, hasil pengujian, manfaat yang diharapkan, dan rencana pengembangan;
5. status implementasi fitur;
6. tingkat kepastian klaim, termasuk kata seperti "diharapkan", "dirancang", "belum diuji", dan "berdasarkan pengamatan penulis".

Jika gaya yang lebih natural bertentangan dengan akurasi, pilih akurasi dan catat konfliknya.

## 3. Pola yang perlu diperiksa

Pola berikut bukan kesalahan. Pola ini menjadi sinyal untuk diperiksa. Revisi hanya bila pola itu benar-benar mengurangi kejelasan atau kepastian.

1. **Kontras formulaik** "tidak hanya ..., tetapi juga ...". Sering bisa diganti dengan pernyataan langsung.
2. **Pembukaan universal** yang bisa ditempel di tulisan lain mana pun. Ganti dengan konteks spesifik kasus.
3. **Klaim besar tanpa bukti**: "sangat penting", "sangat efektif", "menjadi kunci". Turunkan kekuatannya atau tambahkan bukti.
4. **Penutup yang hanya mengulang** kalimat pertama paragraf. Ganti dengan implikasi atau transisi.
5. **"Merupakan" berlebihan**. Sering bisa dihapus: "X merupakan sistem Y" menjadi "X adalah sistem Y".
6. **Nominalisasi berlebihan**: "pengimplementasian", "pengelolaan dilakukan melalui pelaksanaan". Ganti dengan kata kerja bila lebih jelas.
7. **Passive voice tidak otomatis salah**. Pertahankan pasif bila pelaku tidak penting atau bila pedoman mengharuskannya.
8. **Daftar tiga unsur yang dipaksakan**. Pertahankan jika memang tiga; jangan tambahkan untuk ritme.
9. **Pengulangan pembuka** "Berdasarkan ..., ..., ...". Variasikan dengan struktur lain yang sesuai.
10. **Repetisi identitas proyek**: nama sistem diulang di setiap kalimat. Gunakan pronomina atau frasa rujukan bila jelas, atau bentuk pendek setelah rujukan pertama.
11. **Kalimat terlalu penuh**: lebih dari satu gagasan utama dalam satu kalimat. Pecah.
12. **Simetri paragraf berlebihan**: setiap paragraf memiliki panjang dan struktur sama. Biarkan variasi yang wajar.

## 4. Prosedur

1. Tentukan fungsi teks: menjelaskan, membuktikan, membandingkan, menyimpulkan, atau menyatakan batasan.
2. Bekukan fakta dan klaim: tandai semua angka, nama, sitasi, dan klaim yang harus tetap sama.
3. Tandai pola mekanis dari daftar di atas.
4. Revisi per paragraf, dimulai dari gagasan utama.
5. Periksa kehilangan makna: bandingkan versi asli dan revisi pada klaim dan batasan.
6. Baca untuk ritme: pastikan tidak ada pola yang berulang dalam satu halaman.

## 5. Format keluaran

Mode aktif menghasilkan dua bagian.

**Bagian A. Teks hasil revisi.** Teks bersih, siap ditempelkan, dengan struktur dan judul yang sama seperti asli.

**Bagian B. Daftar perubahan.** Tabel dengan kolom: lokasi (bab, subbab, nomor paragraf), versi asli singkat, versi revisi singkat, pola yang diperbaiki, alasan. Hanya tampilkan perubahan yang bermakna. Jangan mencatat setiap perbaikan ejaan kecuali diminta.

Jika ada bagian yang sengaja tidak diubah karena menyangkut invariant, catat itu dalam satu kalimat di akhir daftar.

## 6. Larangan

- Mengarang pengalaman pribadi, observasi, wawancara, atau pengujian agar teks terasa manusiawi.
- Menambahkan atau menghapus sitasi untuk mengubah kesan.
- Menambahkan kesalahan sengaja untuk mengecoh detektor.
- Menjanjikan teks "lolos deteksi AI".
- Mengubah kesimpulan agar lebih meyakinkan dari bukti.

## 7. Lapisan proyek

Sebelum menjalankan skill ini pada naskah proyek, agen wajib membaca rules proyek yang berlaku di `.cursor/rules/` (terutama `kp-00-core.mdc`, `kp-10-pedoman-format.mdc`, dan `kp-20-sitasi-apa.mdc`). Aturan proyek menang atas preferensi gaya umum. Contoh: kata hubung tidak boleh di awal kalimat pada laporan KP, meskipun gaya umum memperbolehkannya.

## 8. Serah terima ke agen lain

Jika skill ini dijalankan oleh agen lain (misalnya setelah agen penulis selesai), sertakan brief berikut:

- lokasi naskah dan bagian yang akan diubah;
- daftar fakta, angka, dan sitasi yang harus dipertahankan;
- rules proyek yang aktif;
- batas perubahan: hanya gaya, tidak boleh isi;
- format keluaran yang diminta (Bagian A dan Bagian B).

Agen penerima wajib mengembalikan hasil dalam format di atas dan tidak boleh menambahkan konten baru.
