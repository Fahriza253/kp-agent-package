---
name: human-academic-writing-kp
description: |
  Membantu agent menulis dan merevisi laporan Kerja Praktek dalam bahasa Indonesia agar tetap akademik, natural, spesifik, dan terasa ditulis manusia tanpa mengubah fakta, bukti, scope, atau tingkat kepastian klaim. Gunakan secara aktif ketika pengguna meminta humanize/rewrite/perbaikan gaya, dan secara pasif sebagai quality gate saat agent menghasilkan atau merevisi naskah laporan KP.
metadata:
  version: "1.0.0"
---

# Human Academic Writing: Laporan Kerja Praktek

## 1. Tujuan

Skill ini menjaga naskah laporan Kerja Praktek agar:

- tetap menggunakan bahasa Indonesia baku dan layak untuk laporan akademik;
- terdengar natural dan spesifik terhadap kasus yang dibahas, bukan seperti keluaran template AI;
- mempertahankan fakta, data, istilah, kutipan, sitasi, dan tingkat kepastian klaim;
- tidak menambahkan bukti, hasil observasi, hasil pengujian, angka, tanggal, atau sumber yang tidak tersedia;
- tidak mengorbankan ketepatan akademik hanya demi membuat tulisan terasa lebih santai atau lebih "manusia";
- mempertahankan gaya penulis bila tersedia contoh tulisan yang representatif.

Skill ini adalah lapisan gaya. Ia tidak menggantikan skill yang mengatur struktur laporan, hierarki sumber, keterlacakan masalah sampai kesimpulan, atau aturan akademik proyek.

## 2. Dua mode penggunaan

### 2.1 Mode aktif

Aktifkan secara eksplisit ketika pengguna meminta hal seperti:

- "buat lebih human";
- "humanize paragraf ini";
- "jangan terdengar seperti AI";
- "buat lebih natural";
- "perbaiki gaya penulisan";
- "buat tulisan lebih enak dibaca";
- "kurangi gaya template/robotik";
- "sesuaikan dengan gaya tulisan saya".

Dalam mode aktif:

1. baca seluruh unit teks sebelum mengubah kalimat;
2. identifikasi pola yang membuat tulisan terasa generik, terlalu simetris, terlalu abstrak, atau terlalu "rapi";
3. tentukan fungsi setiap paragraf;
4. revisi pada tingkat paragraf, bukan sekadar mengganti sinonim;
5. pertahankan semua klaim yang didukung sumber;
6. lakukan pemeriksaan akhir agar revisi tidak mengubah makna atau status bukti.

Jika pengguna memberikan contoh tulisan sendiri, contoh tersebut menjadi acuan utama untuk ritme kalimat, pilihan kata, kepadatan, transisi, dan cara menyebut subjek.

### 2.2 Mode pasif

Mode pasif berjalan sebagai quality gate saat agent menulis atau merevisi laporan KP, walaupun pengguna tidak meminta "humanize".

Mode pasif tidak boleh melakukan rewrite agresif. Gunakan untuk mencegah keluaran baru menjadi terlalu AI-like sejak awal.

Dalam mode pasif, agent harus:

- menghindari pola generik yang tercantum pada skill ini;
- menjaga variasi panjang kalimat yang wajar;
- memilih transisi berdasarkan hubungan makna, bukan pola template;
- menghindari pengulangan penjelasan yang sudah diketahui pembaca;
- menulis sespesifik bukti yang tersedia;
- melakukan satu pemeriksaan singkat sebelum mengembalikan naskah.

Mode pasif tidak boleh:

- mengubah struktur akademik yang sudah ditentukan;
- menurunkan formalitas secara berlebihan;
- memasukkan opini personal;
- menghilangkan istilah teknis yang memang diperlukan;
- mengubah klaim hanya karena kalimatnya terasa formal;
- melakukan "humanization" yang membuat naskah kurang presisi.

## 3. Invariant yang tidak boleh berubah

Setiap revisi wajib mempertahankan:

1. fakta dan informasi yang didukung sumber;
2. angka, tanggal, nama, istilah teknis, dan nomenklatur resmi;
3. kutipan dan sitasi;
4. ruang lingkup proyek;
5. distinction antara:
   - kondisi berjalan;
   - hasil observasi;
   - masalah;
   - kebutuhan;
   - rancangan;
   - implementasi;
   - hasil pengujian;
   - manfaat yang diharapkan;
   - rencana pengembangan;
6. status implementasi fitur;
7. tingkat kepastian klaim.

Contoh:

- "dirancang untuk" tidak boleh berubah menjadi "mampu";
- "diharapkan dapat" tidak boleh berubah menjadi "berhasil";
- "berdasarkan pengamatan penulis" tidak boleh berubah menjadi fakta kelembagaan umum;
- "belum diuji" tidak boleh dihilangkan untuk membuat kalimat terdengar lebih tegas.

Jika gaya yang lebih natural bertentangan dengan akurasi, prioritaskan akurasi.

## 4. Prinsip utama gaya manusia dalam laporan akademik

### 4.1 Tulis untuk satu konteks, bukan untuk semua konteks

Kalimat generik terasa seperti AI karena dapat ditempel pada hampir semua laporan.

Kurang spesifik:

> Sistem informasi memiliki peranan yang sangat penting dalam mendukung proses administrasi yang efektif dan efisien.

Lebih natural dan relevan:

> Pada Fakultas Teknik, pengelolaan data mahasiswa, dosen, mata kuliah, jadwal, dan nilai digunakan dalam beberapa proses akademik yang saling berkaitan.

Gunakan detail yang memang tersedia dalam konteks. Jangan menambahkan detail hanya untuk membuat tulisan tampak lebih spesifik.

### 4.2 Utamakan hubungan logis daripada transisi dekoratif

Jangan menambahkan "selain itu", "dengan demikian", "oleh karena itu", atau "sejalan dengan hal tersebut" hanya agar paragraf terasa formal.

Gunakan transisi jika hubungan antargagasan memang memerlukannya.

Jika dua kalimat sudah berhubungan secara jelas melalui subjek atau objek yang sama, transisi eksplisit mungkin tidak diperlukan.

### 4.3 Variasikan ritme secara wajar

Hindari pola seluruh paragraf yang memiliki:

- jumlah kalimat hampir sama;
- panjang kalimat hampir sama;
- pembukaan yang sama;
- struktur "pernyataan → penjelasan → penegasan" secara berulang.

Tidak perlu memaksakan variasi. Variasi harus mengikuti kebutuhan isi.

### 4.4 Pilih kata yang biasa dipakai dalam tulisan akademik Indonesia

Gunakan bentuk sederhana bila tidak mengurangi ketepatan.

Preferensi umum:

- "digunakan untuk" dibanding "berfungsi sebagai sarana untuk";
- "menunjukkan" hanya jika memang ada bukti yang menunjukkan;
- "menjadi dasar" hanya jika hubungan dasar tersebut dapat dijelaskan;
- "mencakup" dibanding "meliputi berbagai aspek yang terdiri atas" bila maknanya sama;
- "memerlukan" dibanding "membutuhkan adanya";
- "dibuat" atau "dikembangkan" dibanding "dihadirkan" untuk perangkat lunak.

Jangan mengganti istilah teknis baku hanya karena terdengar formal.

## 5. Pola AI-like yang perlu diperiksa

Pola berikut bukan larangan mutlak. Nilai berdasarkan konteks dan frekuensinya.

### 5.1 Kontras formulaik "tidak hanya..., tetapi juga..."

Pola ini sering digunakan untuk memberi bobot tanpa menambah informasi.

Kurang natural:

> Sistem tidak hanya digunakan untuk menyimpan data, tetapi juga menjadi solusi dalam meningkatkan kualitas pengelolaan akademik.

Lebih tepat:

> Sistem digunakan untuk mengelola data akademik dan mendukung proses yang menggunakan data tersebut.

Pertahankan kontras hanya jika dua sisi memang diperlukan.

### 5.2 Pembukaan abstrak dan universal

Waspadai:

- "Di era digital saat ini...";
- "Perkembangan teknologi yang semakin pesat...";
- "Teknologi informasi memiliki peranan yang sangat penting...";
- "Seiring dengan perkembangan zaman...";
- "Dalam dunia pendidikan modern...".

Gunakan konteks aktual objek KP sebagai pembuka jika memungkinkan.

### 5.3 Klaim besar tanpa bukti

Waspadai:

- sangat efektif;
- sangat efisien;
- optimal;
- signifikan;
- meningkatkan produktivitas;
- meminimalkan kesalahan;
- mempercepat proses;
- meningkatkan kualitas layanan.

Jika tidak ada pengukuran, ubah ke fungsi atau tujuan yang dapat dibuktikan.

Contoh:

> Sistem dirancang untuk mengurangi input ulang data.

lebih aman daripada:

> Sistem meningkatkan efisiensi kerja staf secara signifikan.

### 5.4 Penutup paragraf yang hanya mengulang

Waspadai:

- "Hal ini menunjukkan pentingnya...";
- "Dengan demikian, sistem ini sangat diperlukan...";
- "Oleh karena itu, hal tersebut menjadi sangat penting...";
- "Kondisi ini menegaskan bahwa...".

Jika kalimat hanya mengulang isi sebelumnya, hapus atau gabungkan.

### 5.5 Penggunaan "merupakan" secara berlebihan

"Merupakan" sah dalam bahasa akademik, tetapi pengulangan membuat teks terasa template.

Variasikan secara natural:

- "X adalah...";
- "X digunakan untuk...";
- "X mencakup...";
- "X mengacu pada...";
- "X didefinisikan sebagai..." bila ada dasar definisi.

Jangan mengganti "merupakan" jika bentuk tersebut memang paling tepat.

### 5.6 Nominalisasi berlebihan

Kurang natural:

> Pelaksanaan pengelolaan data dilakukan melalui penggunaan beberapa berkas.

Lebih langsung:

> Staf mengelola data melalui beberapa berkas.

Namun, laporan akademik Indonesia tetap dapat menggunakan bentuk pasif jika aktor tidak penting atau fokus kalimat berada pada proses/objek.

### 5.7 Passive voice bukan otomatis kesalahan

Jangan menerapkan aturan "selalu ubah ke aktif".

Gunakan aktif ketika aktor penting:

> Staff Prodi menginput data mahasiswa baru.

Gunakan pasif ketika objek/proses lebih penting:

> Data mahasiswa disimpan pada basis data setelah validasi.

Pilih berdasarkan fokus informasi.

### 5.8 Daftar tiga unsur yang dipaksakan

Jangan menambah item ketiga hanya agar kalimat terasa lengkap.

Jika data memiliki dua unsur, tulis dua. Jika memiliki lima, tulis lima atau kelompokkan secara logis.

### 5.9 Pengulangan struktur "Berdasarkan..."

Waspadai beberapa paragraf berturut-turut yang diawali:

- "Berdasarkan hasil observasi...";
- "Berdasarkan kondisi tersebut...";
- "Berdasarkan uraian tersebut...".

Pertahankan "Berdasarkan..." ketika asal bukti memang perlu ditandai. Pada bagian lain, gunakan struktur langsung.

### 5.10 Repetisi identitas proyek

Setelah konteks jelas, hindari mengulang frasa lengkap seperti:

> Sistem Informasi Akademik berbasis web pada Fakultas Teknik Universitas Putra Indonesia Cianjur

di setiap paragraf.

Gunakan "SIAKAD", "sistem", atau referen lain yang tidak ambigu.

### 5.11 Kalimat yang terlalu penuh

Waspadai satu kalimat yang sekaligus memuat:

- konteks;
- sebab;
- solusi;
- manfaat;
- ruang lingkup;
- hasil.

Pecah ketika relasi antargagasan menjadi sulit dibaca.

### 5.12 Simetri paragraf yang berlebihan

Jika seluruh subbab terdiri atas paragraf yang panjangnya seragam dan memiliki pola retoris yang sama, periksa apakah struktur tersebut muncul karena isi atau karena template.

Jangan sengaja membuat paragraf "acak". Cukup biarkan kebutuhan isi menentukan panjang dan bentuknya.

## 6. Gaya khusus laporan Kerja Praktek

### 6.1 Formal tetapi tidak kaku

Target gaya:

- objektif;
- jelas;
- spesifik;
- tidak promosi;
- tidak percakapan;
- tidak penuh frasa seremonial.

Hindari:

- "tentunya";
- "pada dasarnya" jika tidak diperlukan;
- "dapat dikatakan bahwa";
- "sebagaimana kita ketahui";
- "perlu diketahui bahwa";
- "sangatlah";
- "guna untuk";
- "agar supaya".

### 6.2 Jangan memaksakan orang pertama

Gunakan "penulis" hanya ketika subjek penulis memang penting, misalnya:

> Berdasarkan pengamatan penulis selama menjalankan tugas sebagai Staf Fakultas Teknik, ...

Untuk penjelasan sistem, utamakan subjek yang konkret:

> Sistem memvalidasi kode mata kuliah sebelum data disimpan.

### 6.3 Pertahankan ketidaksempurnaan yang wajar

Tulisan manusia yang baik tidak berarti harus memiliki "quirks" buatan, typo, atau inkonsistensi.

Jangan sengaja:

- menambah kesalahan gramatikal;
- memasukkan slang;
- membuat kalimat bertele-tele;
- mengubah tanda baca secara acak;
- menambahkan pendapat pribadi.

"Human" berarti keputusan bahasa terasa sesuai konteks, bukan dibuat kurang rapi.

### 6.4 Gunakan tanda baca yang sesuai konteks

Jangan gunakan karakter U+2014 pada naskah, heading, contoh, maupun teks keluaran. Gunakan koma, titik dua, titik koma, tanda kurung, atau pisahkan kalimat sesuai hubungan gagasan. Sebelum mengembalikan naskah, jalankan `python scripts/check_project_markdown.py` untuk memeriksa dokumen Markdown proyek.

## 7. Workflow revisi aktif

Gunakan langkah berikut secara internal.

### Langkah 1: Tentukan fungsi teks

Identifikasi apakah teks berfungsi sebagai:

`konteks | kondisi berjalan | masalah | kebutuhan | teori | perancangan | implementasi | pengujian | hasil | kesimpulan`

Gaya harus mengikuti fungsi tersebut.

### Langkah 2: Bekukan fakta dan klaim

Catat elemen yang tidak boleh berubah:

- fakta;
- angka;
- nama;
- istilah;
- sitasi;
- status implementasi;
- tingkat kepastian.

### Langkah 3: Tandai pola mekanis

Cari pola pada §5. Prioritaskan masalah struktural sebelum diksi.

### Langkah 4: Revisi berdasarkan pesan utama paragraf

Jangan melakukan penggantian kata satu per satu.

Tentukan pesan utama paragraf, lalu tulis ulang kalimat di sekitarnya agar:

- urutan informasinya alami;
- subjeknya jelas;
- transisinya memiliki fungsi;
- detail yang relevan tetap ada.

### Langkah 5: Cek kehilangan makna

Bandingkan draft dengan sumber.

Pastikan tidak ada:

- fakta hilang;
- klaim menguat;
- klaim melemah tanpa alasan;
- perubahan status rencana menjadi hasil;
- perubahan istilah resmi.

### Langkah 6: Baca untuk ritme

Periksa:

- pembukaan kalimat berulang;
- panjang kalimat terlalu seragam;
- paragraf terlalu simetris;
- penutup repetitif;
- transisi berlebihan.

Perbaiki hanya jika benar-benar mengganggu.

## 8. Quality gate pasif

Sebelum mengembalikan naskah laporan yang baru ditulis, cek cepat:

1. Apakah kalimat pembuka bersifat spesifik terhadap topik?
2. Apakah ada frasa template yang tidak menambah informasi?
3. Apakah klaim manfaat melampaui bukti?
4. Apakah beberapa kalimat/paragraf memiliki struktur yang terlalu seragam?
5. Apakah "merupakan", "berdasarkan", "dengan demikian", atau "selain itu" dipakai berulang tanpa kebutuhan?
6. Apakah ada kalimat penutup yang hanya mengulang?
7. Apakah istilah proyek tetap konsisten?
8. Apakah status fakta/rencana/implementasi/pengujian tetap benar?
9. Apakah gaya tetap sesuai bahasa laporan ilmiah?
10. Apakah revisi masih terdengar seperti penulis manusia yang memahami objek yang dibahas, bukan template generik?
11. Apakah naskah bebas dari karakter U+2014?

Jika jawabannya sudah baik, jangan melakukan rewrite tambahan.

## 9. Interaksi dengan skill akademik lain

Jika skill ini digunakan bersama skill penulisan laporan KP:

1. skill akademik menentukan:
   - struktur;
   - sumber kebenaran;
   - claim-evidence alignment;
   - traceability;
   - batas scope;
   - aturan bab;
2. skill ini menentukan:
   - keluwesan bahasa;
   - naturalness;
   - ritme;
   - pengurangan pola AI-like;
   - preservasi voice penulis.

Jika terjadi konflik, urutan prioritas:

`ketepatan fakta > bukti > aturan akademik > konsistensi istilah > kejelasan > gaya human`

## 10. Format keluaran

### Permintaan rewrite/humanize eksplisit

Berikan:

1. versi revisi siap digunakan;
2. catatan singkat hanya jika ada perubahan substantif atau klaim yang perlu perhatian.

Jangan menampilkan seluruh checklist internal kecuali diminta.

### Permintaan review gaya

Berikan:

- penilaian singkat;
- 2–5 pola utama yang ditemukan;
- contoh revisi pada bagian paling bermasalah;
- jangan menyimpulkan teks "AI-generated". Nilai hanya karakteristik gaya yang tampak.

### Digunakan secara embedded oleh agent lain

Kembalikan hanya naskah akhir kecuali agent pemanggil meminta diagnostik.

## 11. Larangan

Skill ini tidak boleh digunakan untuk:

- mengarang pengalaman pribadi agar teks terasa manusia;
- menambahkan observasi yang tidak dilakukan;
- membuat kutipan palsu;
- membuat hasil pengujian palsu;
- mengubah kesimpulan agar lebih meyakinkan dari bukti;
- sengaja menambahkan kesalahan untuk mengecoh AI detector;
- menjanjikan bahwa teks akan "lolos AI detector".

Tujuan skill ini adalah kualitas tulisan akademik yang natural dan dapat dipertanggungjawabkan, bukan manipulasi alat deteksi.
