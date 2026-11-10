---
name: research-paper-writing-kp-siakad
summary: Membantu AI menyusun, merevisi, dan meninjau Laporan Kerja Praktek SIAKAD Fakultas Teknik UNPI agar sesuai Pedoman KP 2026, konsisten dengan sistem yang benar-benar dikembangkan, serta memiliki keterlacakan yang jelas dari masalah hingga kesimpulan.
description: Gunakan skill ini ketika menyusun atau merevisi Laporan Kerja Praktek (KP) Program Studi Teknik Informatika S1 Fakultas Teknik Universitas Putra Indonesia (UNPI) Cianjur, khususnya proyek "Pengembangan Sistem Informasi Akademik Berbasis Web pada Fakultas Teknik Universitas Putra Indonesia Cianjur". Skill ini digunakan untuk penulisan BAB I Pendahuluan, BAB II Kajian Pustaka, BAB III Sarana dan Prasarana, BAB IV Analisis dan Pembahasan, BAB V Implementasi dan Pengujian, BAB VI Penutup, penyusunan tabel/gambar, pemeriksaan konsistensi klaim-bukti, dan self-review sebelum bimbingan atau seminar KP.
---

# Penulisan Laporan Kerja Praktek: SIAKAD Fakultas Teknik UNPI

## 1. Tujuan Skill

Gunakan skill ini untuk membantu menghasilkan laporan Kerja Praktek yang:

1. sesuai dengan Pedoman Kerja Praktek Fakultas Teknik Universitas Putra Indonesia revisi 2026;
2. konsisten dengan pekerjaan dan sistem yang benar-benar dikembangkan;
3. membedakan secara tegas tugas rutin penulis sebagai Staf Fakultas Teknik dengan proyek SIAKAD yang menjadi pekerjaan Kerja Praktek;
4. memiliki alur argumentasi akademik yang jelas;
5. menghubungkan masalah, kebutuhan, perancangan, implementasi, pengujian, hasil, dan kesimpulan secara konsisten;
6. tidak membuat klaim yang melampaui bukti observasi, dokumen, implementasi, hasil pengujian, atau sumber ilmiah yang tersedia;
7. mudah dibaca oleh dosen pembimbing, penguji, maupun pembaca eksternal yang tidak mengikuti proses pengembangan sistem sejak awal.

Fokus skill ini bukan sekadar membuat teks terdengar formal, tetapi memastikan laporan dapat dipertanggungjawabkan secara akademik dan teknis.

## Skill pendamping (wajib bersama skill ini)

Agen wajib memakai paket di `docs/agents/draft-guides/`; urutan kerja: `docs/agents/penulisan-kp-skills.md` dan indeks `draft-guides/README.md`.

| Berkas                                | Fungsi                                                                                 |
| ------------------------------------- | -------------------------------------------------------------------------------------- |
| `human-academic-writing-kp-skills.md` | Gaya bahasa Indonesia akademik; mode pasif pada setiap keluaran                        |
| `does-my-writing-flow-skills.md`      | Kejelasan, koherensi, kepaduan, keringkasan; pemeriksaan alur sebelum menyerahkan teks |

## Aturan Tanda Baca

Jangan gunakan karakter U+2014 dalam laporan, contoh, heading, atau teks keluaran. Gunakan koma, titik dua, titik koma, tanda kurung, atau pisahkan kalimat sesuai konteks. Jalankan `python scripts/check_project_markdown.py` sebelum menyelesaikan perubahan Markdown.

---

## 2. Konteks Proyek yang Harus Dipertahankan

AI harus mempertahankan konteks berikut selama membantu penulisan laporan:

- Tempat Kerja Praktek: Universitas Putra Indonesia (UNPI) Cianjur.
- Ruang lingkup organisasi: Fakultas Teknik dan program studi yang dinaunginya.
- Program studi utama penulis: Teknik Informatika S1.
- Proyek KP: pengembangan Sistem Informasi Akademik (SIAKAD) berbasis web.
- Judul kerja laporan saat ini: **"Pengembangan Sistem Informasi Akademik Berbasis Web pada Fakultas Teknik Universitas Putra Indonesia Cianjur"**.
- Sistem dikembangkan untuk mendukung operasional akademik internal tingkat fakultas/program studi.
- SIAKAD bukan pengganti Neofeeder/PDDIKTI. SIAKAD berperan sebagai sistem operasional internal yang memiliki mekanisme pertukaran data dengan Neofeeder sesuai batas integrasi yang telah ditentukan.
- Penulis juga bekerja sebagai Staf Fakultas Teknik. Pekerjaan rutin staf hanya boleh digunakan sebagai sumber observasi/konteks bila relevan; pekerjaan rutin tersebut **bukan otomatis merupakan pekerjaan Kerja Praktek**.
- Analisis kebutuhan, perancangan, implementasi, pengujian, dan dokumentasi SIAKAD adalah kegiatan proyek Kerja Praktek.

Jika terdapat perubahan scope, fitur, arsitektur, atau hasil implementasi, AI wajib mengikuti sumber proyek terbaru dan tidak mempertahankan informasi lama hanya karena pernah ditulis pada versi laporan sebelumnya.

---

## 3. Hierarki Sumber dan Otoritas

Gunakan sumber dengan urutan prioritas berikut ketika terjadi perbedaan atau konflik informasi:

1. **Pedoman Kerja Praktek Fakultas Teknik UNPI revisi 2026**  
   Digunakan untuk struktur laporan, kewajiban akademik, sistematika, tata bahasa, format penulisan, dan aturan formal KP.

2. **Dokumentasi proyek SIAKAD yang menjadi Source of Record/Source of Truth**  
   Digunakan untuk scope sistem, aktor, proses bisnis, aturan bisnis, fitur, integrasi Neofeeder, use case, arsitektur, implementasi, dan status pengembangan.

3. **Artefak implementasi aktual**  
   Repository source code, schema database, migration, API, UI, pengujian, hasil deployment, screenshot, log, atau artefak teknis lain yang menunjukkan apa yang benar-benar telah dibuat.

4. **Draft laporan KP terbaru**  
   Digunakan sebagai baseline narasi dan struktur yang sedang disusun, tetapi bukan sumber kebenaran jika bertentangan dengan pedoman atau implementasi aktual.

5. **Hasil observasi, wawancara, dan dokumen institusi**  
   Digunakan untuk menjelaskan kondisi berjalan, kebutuhan pengguna, proses manual, atau konteks organisasi.

6. **Sumber ilmiah/teknis eksternal**  
   Digunakan untuk landasan teori, definisi akademik, metode pengembangan, basis data, REST API, UML, pengujian perangkat lunak, PDDIKTI/Neofeeder, dan topik pendukung lain.

Jika sumber yang diperlukan tidak tersedia, jangan mengarang. Nyatakan bahwa informasi atau bukti masih diperlukan.

---

## 4. Workflow Utama

Ikuti workflow berikut saat menyusun atau merevisi bagian laporan.

### Tahap 1: Tentukan tujuan bagian

Sebelum menulis, identifikasi:

- bab/subbab yang sedang dikerjakan;
- fungsi akademik bagian tersebut;
- pertanyaan yang harus dijawab bagian tersebut;
- sumber bukti yang tersedia;
- hubungan bagian tersebut dengan bab sebelumnya dan sesudahnya.

Jangan langsung memperbaiki kalimat jika masalah utamanya adalah struktur argumen.

### Tahap 2: Bangun mini-outline

Sebelum menulis paragraf, buat outline ringkas berisi 3–7 poin yang menunjukkan urutan logika.

Contoh untuk Latar Belakang:

1. konteks pengelolaan akademik;
2. kondisi operasional Fakultas Teknik;
3. masalah yang diamati;
4. konsekuensi atau kebutuhan yang muncul;
5. alasan pemilihan tempat/proyek KP;
6. solusi yang dikembangkan;
7. judul dan luaran KP.

### Tahap 3: Tulis satu pesan utama per paragraf

Setiap paragraf harus mempunyai satu fungsi utama.

Kalimat pertama harus sebisa mungkin memperkenalkan pesan utama paragraf. Kalimat berikutnya menjelaskan, membuktikan, memperinci, membandingkan, atau menyimpulkan pesan tersebut.

### Tahap 4: Lakukan reverse outlining

Setelah bagian selesai ditulis:

1. tulis ulang ide utama setiap paragraf dalam satu kalimat;
2. periksa apakah urutannya logis;
3. periksa apakah setiap paragraf mendukung tujuan subbab;
4. hapus atau pindahkan paragraf yang tidak dapat dipetakan secara jelas.

### Tahap 5: Periksa claim–evidence alignment

Untuk setiap klaim penting, tanyakan:

- sumbernya apa?
- apakah klaim berasal dari observasi?
- apakah berasal dari dokumen institusi?
- apakah sudah diimplementasikan?
- apakah sudah diuji?
- apakah hanya rencana/usulan?
- apakah hanya manfaat yang diharapkan?

Jika bukti tidak cukup, lakukan salah satu:

- perlemah klaim;
- ubah menjadi pernyataan kebutuhan/rencana;
- tandai sebagai usulan;
- tambahkan kebutuhan bukti;
- hapus klaim.

### Tahap 6: Uji konsistensi lintas bab

Pastikan alur berikut tidak terputus:

**Masalah → Rumusan Masalah → Tujuan → Kebutuhan Sistem → Perancangan → Implementasi → Pengujian → Hasil → Kesimpulan**

Setiap masalah utama idealnya memiliki jejak sampai kesimpulan.

### Tahap 7: Adversarial self-review

Baca sebagai dosen penguji yang skeptis. Cari:

- klaim berlebihan;
- istilah tidak konsisten;
- fitur disebut di laporan tetapi belum ada di implementasi;
- hasil implementasi tanpa kebutuhan asal;
- pengujian yang tidak membuktikan kebutuhan;
- kesimpulan yang lebih luas daripada hasil;
- penggunaan asumsi sebagai fakta;
- inkonsistensi scope.

---

## 5. Prinsip Global Penulisan

1. Satu paragraf = satu pesan utama.
2. Hindari paragraf yang hanya berisi definisi tanpa fungsi dalam argumen laporan.
3. Gunakan bahasa Indonesia baku dan formal.
4. Hindari kata ganti orang jika tidak diperlukan. Gunakan "penulis" bila penyebutan subjek memang diperlukan.
5. Gunakan istilah teknis asing secara konsisten dan hanya jika lebih tepat daripada padanan Indonesia.
6. Jangan menggunakan gaya promosi produk seperti "sangat efisien", "canggih", "modern", "optimal", atau "meningkatkan produktivitas" tanpa bukti pengukuran.
7. Bedakan secara tegas antara:
   - fakta;
   - hasil observasi;
   - kebutuhan;
   - keputusan desain;
   - hasil implementasi;
   - hasil pengujian;
   - manfaat yang diharapkan;
   - rencana pengembangan.
8. Jangan menulis bahwa suatu fitur "berhasil" jika hanya telah dirancang tetapi belum diuji.
9. Jangan menulis peningkatan kinerja, efisiensi, akurasi, atau kecepatan jika tidak ada metode pembanding atau data pengukuran.
10. Gunakan istilah yang stabil di seluruh laporan. Jika istilah resmi proyek adalah "kelas perkuliahan", jangan berganti menjadi "kelas kuliah" atau "kelas akademik" tanpa alasan.
11. Jangan menyebut fitur di luar scope seolah-olah merupakan deliverable KP.
12. Jangan menggunakan klaim kelembagaan yang tidak berasal dari sumber resmi atau observasi yang dapat dipertanggungjawabkan.
13. Tabel, diagram, screenshot, dan gambar harus membantu pembuktian atau penjelasan, bukan sekadar dekorasi.

---

## 6. Pemisahan Tugas Rutin dan Proyek Kerja Praktek

Karena penulis juga merupakan Staf Fakultas Teknik, AI wajib menjaga pemisahan berikut.

### Tugas rutin staf

Dapat mencakup kegiatan administrasi akademik, pengelolaan dokumen, penyusunan jadwal, pengarsipan, koordinasi, atau pekerjaan fakultas lain yang memang menjadi pekerjaan sehari-hari.

Tugas rutin dapat digunakan sebagai:

- sumber observasi;
- sumber pemahaman proses bisnis;
- konteks masalah;
- sumber kebutuhan pengguna.

### Proyek Kerja Praktek

Harus berupa kegiatan pengembangan SIAKAD yang dapat dibuktikan, seperti:

- analisis kebutuhan;
- pemodelan proses/data;
- perancangan sistem;
- perancangan basis data;
- pengembangan backend/frontend;
- implementasi fitur;
- integrasi Neofeeder;
- pengujian;
- deployment/UAT bila tersedia;
- dokumentasi teknis dan laporan.

Jangan menuliskan pekerjaan rutin sebagai hasil implementasi KP hanya karena dilakukan oleh penulis selama berada di tempat kerja.

---

## 7. Keterlacakan Akademik Wajib

Untuk setiap fitur atau modul utama, usahakan tersedia rantai berikut:

| Tahap        | Pertanyaan yang harus dapat dijawab               |
| ------------ | ------------------------------------------------- |
| Masalah      | Kondisi apa yang menimbulkan kebutuhan?           |
| Kebutuhan    | Apa yang harus dapat dilakukan sistem?            |
| Perancangan  | Bagaimana kebutuhan diterjemahkan menjadi desain? |
| Implementasi | Bagian apa yang benar-benar dibuat?               |
| Pengujian    | Bagaimana implementasi diverifikasi?              |
| Hasil        | Apa yang terbukti dari pengujian?                 |
| Kesimpulan   | Rumusan masalah mana yang telah dijawab?          |

Jika satu tahap tidak memiliki bukti, jangan menutup gap tersebut dengan narasi spekulatif.

---

## 8. Panduan per Bab

### 8.1 BAB I: Pendahuluan

BAB I harus membangun alasan akademik dan praktis mengapa proyek dilakukan.

#### 1.1 Latar Belakang

Latar belakang harus mencakup:

- konteks pengelolaan akademik;
- kondisi aktual yang diamati di Fakultas Teknik;
- masalah yang relevan dengan proyek;
- kebutuhan sistem yang muncul;
- alasan pemilihan lokasi/tempat KP yang dapat diterima secara akademik;
- hubungan proyek dengan kompetensi Teknik Informatika;
- gambaran solusi yang dikembangkan;
- judul dan luaran KP.

Hindari:

- menyatakan memilih lokasi hanya karena penulis bekerja di sana;
- memasukkan fitur terlalu rinci sebelum kebutuhan dijelaskan;
- menyebut hasil yang belum diuji;
- mencampur fakta, harapan, dan usulan tanpa penanda yang jelas.

#### 1.2 Identifikasi Masalah

Setiap poin harus berupa kondisi masalah yang dapat diamati, bukan solusi.

Format konseptual:

> kondisi saat ini + keterbatasan/kendala yang relevan

Jangan menulis "belum ada SIAKAD" sebagai masalah jika inti masalah yang sebenarnya adalah data tersebar, proses pencocokan manual, atau input berulang.

#### 1.3 Rumusan Masalah

Rumusan masalah harus:

- berasal langsung dari identifikasi masalah;
- berbentuk pertanyaan;
- dapat dijawab oleh hasil proyek;
- tidak terlalu luas dibanding scope implementasi.

Gunakan pola "Bagaimana ...?" bila sesuai.

#### 1.4 Batasan Masalah

Batasan harus menjelaskan:

- organisasi/prodi yang dicakup;
- fungsi yang termasuk;
- aktor dan capability utama;
- batas integrasi Neofeeder;
- fitur yang tidak termasuk;
- batas implementasi/pengujian jika ada.

Batasan bukan tempat menjelaskan detail desain yang tidak diperlukan.

#### 1.5 Tujuan dan Manfaat

Tujuan harus menjawab rumusan masalah dalam bentuk tindakan yang dapat diverifikasi.

Gunakan verba seperti:

- menganalisis;
- merancang;
- mengimplementasikan;
- mengembangkan;
- menguji.

Manfaat harus dibedakan dari hasil. Jika belum ada pengukuran dampak, gunakan frasa seperti "diharapkan dapat" atau "menyediakan luaran berupa".

#### 1.6 Metode Pengumpulan Data

Jelaskan metode yang benar-benar dilakukan, misalnya:

- observasi;
- wawancara tidak terstruktur;
- studi dokumen;
- dokumentasi teknis.

Untuk setiap metode, jelaskan:

- siapa/sumber apa;
- informasi apa yang dikumpulkan;
- bagaimana hasilnya digunakan dalam pengembangan sistem.

#### 1.7 Lokasi

Jika pedoman atau struktur laporan memisahkan lokasi sebagai subbab tersendiri, jelaskan tempat KP dan ruang lingkup unit secara ringkas.

#### 1.8 Sistematika Penulisan

Jelaskan isi setiap bab sesuai struktur laporan aktual. Jangan menulis subbab yang pada dokumen akhir tidak ada.

---

### 8.2 BAB II: Kajian Pustaka

BAB II menyediakan konteks institusi dan teori yang benar-benar dipakai dalam analisis, perancangan, implementasi, atau pengujian.

#### Profil Tempat KP

Gunakan sumber institusi yang dapat dipertanggungjawabkan untuk:

- sejarah;
- visi/misi;
- struktur organisasi;
- posisi Fakultas Teknik;
- informasi lain yang relevan dengan proyek.

Jangan memasukkan detail organisasi yang tidak berkaitan dengan konteks sistem hanya untuk menambah panjang laporan.

#### Landasan Teori

Teori harus berfungsi sebagai dasar pembahasan bab berikutnya.

Topik yang relevan untuk proyek ini dapat mencakup:

- pengembangan perangkat lunak;
- sistem informasi dan sistem informasi akademik;
- analisis kebutuhan perangkat lunak;
- UML/pemodelan sistem;
- basis data relasional dan ERD;
- aplikasi web dan REST API;
- PDDIKTI dan Neofeeder;
- integrasi/sinkronisasi data;
- pengujian perangkat lunak.

Setiap teori sebaiknya mempunyai hubungan eksplisit dengan penggunaan pada proyek.

Hindari "kamus definisi" yang hanya menumpuk kutipan.

---

### 8.3 BAB III: Sarana dan Prasarana

Jelaskan sarana yang benar-benar digunakan untuk mendukung pelaksanaan proyek.

Kelompok yang dapat digunakan:

- perangkat keras pengembangan;
- sistem operasi;
- perangkat lunak pengembangan;
- framework/library utama;
- database;
- repository/version control;
- lingkungan deployment/testing;
- jaringan/infrastruktur yang relevan.

Untuk setiap item, jelaskan fungsi terhadap proyek. Hindari daftar spesifikasi panjang yang tidak mempunyai pengaruh terhadap pekerjaan KP.

---

### 8.4 BAB IV: Analisis dan Pembahasan

BAB IV harus menjelaskan cara masalah diterjemahkan menjadi solusi yang dirancang.

Struktur yang disarankan dapat meliputi:

1. analisis sistem/proses berjalan;
2. identifikasi kebutuhan pengguna;
3. kebutuhan fungsional;
4. kebutuhan nonfungsional;
5. aktor dan hak akses;
6. proses bisnis usulan;
7. use case;
8. perancangan data/ERD;
9. arsitektur sistem;
10. rancangan antarmuka atau alur pengguna bila relevan;
11. desain integrasi Neofeeder.

Setiap keputusan desain harus dapat ditelusuri ke kebutuhan atau constraint.

Jangan menjadikan BAB IV sebagai dokumentasi source code.

---

### 8.5 BAB V: Implementasi dan Pengujian

BAB V harus menjelaskan apa yang benar-benar diterapkan dan bagaimana hasilnya diverifikasi.

#### Implementasi

Untuk setiap modul utama:

- sebutkan kebutuhan atau desain asal;
- jelaskan bagian yang diimplementasikan;
- tampilkan bukti seperlunya, seperti screenshot UI, endpoint, tabel database, atau alur kerja;
- hindari menyalin source code panjang ke badan laporan;
- jelaskan status fitur: selesai, sebagian, atau belum diimplementasikan.

#### Pengujian

Setiap pengujian harus mempunyai:

- tujuan;
- objek yang diuji;
- skenario/input;
- hasil yang diharapkan;
- hasil aktual;
- status lulus/gagal;
- catatan bila ada.

Gunakan tabel pengujian bila membantu keterbacaan.

Untuk fitur yang belum diuji di lingkungan nyata, jangan menyebutnya telah terbukti secara operasional.

#### Pengujian Integrasi Neofeeder

Bedakan dengan jelas:

- mock/stub di development;
- pengujian staging;
- pengujian production;
- fitur yang baru sampai tahap desain.

Jangan mengklaim integrasi production-ready bila pengujian hanya dilakukan dengan mock.

---

### 8.6 BAB VI: Penutup

#### Kesimpulan

Kesimpulan harus menjawab rumusan masalah, bukan mengulang isi laporan secara umum.

Setiap poin kesimpulan harus:

- berasal dari hasil implementasi/pengujian;
- proporsional terhadap bukti;
- tidak memperkenalkan informasi baru;
- tidak menyatakan dampak yang belum diukur.

#### Saran

Saran harus berasal dari:

- keterbatasan implementasi;
- fitur yang sengaja berada di luar scope;
- temuan selama pengujian;
- kebutuhan pengembangan lanjutan.

Jangan menyamarkan fitur yang gagal diselesaikan sebagai "saran" tanpa menjelaskan status sebenarnya bila fitur tersebut sebelumnya termasuk scope wajib.

---

## 9. Pemeriksaan Kejelasan Paragraf

Gunakan pemeriksaan berikut setiap kali pengguna meminta penilaian apakah paragraf "mengalir", "jelas", atau "akademik".

### Pemeriksaan pembaca eksternal

Tanyakan:

- Apakah paragraf memiliki satu pesan utama?
- Apakah kalimat pertama menunjukkan fungsi paragraf?
- Apakah istilah utama dapat dipahami tanpa konteks tersembunyi?
- Apakah setiap kalimat memiliki hubungan yang jelas dengan kalimat sebelumnya?
- Apakah ada lompatan logika?
- Apakah fakta dan interpretasi dapat dibedakan?

### Hubungan antarkalimat

Setiap kalimat sebaiknya memiliki salah satu hubungan berikut:

- sebab;
- akibat;
- penjelasan;
- perincian;
- contoh;
- perbandingan;
- kontras;
- pembatasan;
- konsekuensi;
- transisi menuju ide berikutnya.

Jika hubungan tidak jelas, revisi urutan atau tambahkan transisi yang benar-benar diperlukan.

### Reverse outline bagian

Catat:

- tesis/pesan utama subbab;
- topic sentence tiap paragraf;
- bukti/penjelasan tiap paragraf.

Periksa pemetaan:

**bukti → topic sentence → tujuan subbab → tujuan bab**

---

## 10. Claim–Evidence Map

Untuk klaim penting, gunakan format internal berikut:

`Claim: ... | Evidence: ... | Status: supported / partial / needs evidence / proposed`

Definisi status:

- **supported**: ada bukti langsung yang memadai;
- **partial**: ada bukti, tetapi klaim masih lebih luas dari bukti;
- **needs evidence**: belum ada sumber yang cukup;
- **proposed**: merupakan rancangan/usulan, bukan kondisi atau hasil yang telah terjadi.

Contoh:

`Claim: Data yang diinput pada SIAKAD dapat dikirim ke Neofeeder tanpa input ulang manual. | Evidence: implementasi adapter + hasil pengujian staging. | Status: supported`

Jika baru dirancang:

`Claim: Data yang diinput pada SIAKAD dapat dikirim ke Neofeeder tanpa input ulang manual. | Evidence: desain integrasi dan use case, belum ada pengujian staging. | Status: proposed`

---

## 11. Matriks Konsistensi Lintas Bab

Gunakan matriks berikut saat melakukan review besar.

| ID  | Identifikasi Masalah | Rumusan Masalah | Tujuan | Kebutuhan/Desain | Implementasi | Pengujian | Kesimpulan |
| --- | -------------------- | --------------- | ------ | ---------------- | ------------ | --------- | ---------- |
| M1  | ...                  | ...             | ...    | ...              | ...          | ...       | ...        |
| M2  | ...                  | ...             | ...    | ...              | ...          | ...       | ...        |
| M3  | ...                  | ...             | ...    | ...              | ...          | ...       | ...        |

Tandai gap dengan jelas. Jangan memaksa semua elemen dianggap selesai bila belum ada implementasi atau pengujian.

---

## 12. Aturan Khusus SIAKAD dan Neofeeder

AI harus menjaga beberapa distinction penting:

1. SIAKAD adalah sistem operasional internal; Neofeeder/PDDIKTI merupakan sistem eksternal untuk pelaporan resmi sesuai konteks proyek.
2. Jangan menyebut SIAKAD menggantikan Neofeeder.
3. Integrasi harus dijelaskan sesuai scope aktual proyek, termasuk arah Pull/Push dan entitas yang benar-benar masuk scope.
4. Jangan menyatakan seluruh data PDDIKTI dapat disinkronkan jika implementasi hanya mencakup entitas tertentu.
5. Bedakan "input ulang manual" sebagai masalah proses dengan klaim "proses lambat". Jangan menyatakan lambat bila tidak memiliki data pengukuran atau sumber resmi.
6. Jika alur BAAK masih berupa usulan atau memerlukan validasi, beri label eksplisit sebagai usulan dan jangan menulisnya sebagai proses existing yang telah berlaku.
7. Sinkronisasi batch manual, real-time, staging, mock, dan production adalah istilah yang berbeda dan tidak boleh dipertukarkan.

---

## 13. Gaya Bahasa Akademik

Gunakan bahasa Indonesia baku dan objektif.

Preferensi gaya:

- "Berdasarkan hasil observasi..." dibanding "Terlihat bahwa..."
- "Sistem dirancang untuk..." dibanding "Sistem ini tentunya akan..."
- "Hasil pengujian menunjukkan..." hanya jika memang ada hasil pengujian.
- "Diharapkan dapat..." untuk manfaat yang belum diukur.
- "Di luar ruang lingkup pengembangan..." untuk fitur out-of-scope.
- "Belum diimplementasikan" lebih baik daripada mengaburkan status fitur.

Hindari:

- "tentunya";
- "sangat" tanpa ukuran;
- "optimal" tanpa benchmark;
- "efektif" tanpa evaluasi;
- "efisien" tanpa pengukuran;
- "canggih";
- "sempurna";
- "berhasil meningkatkan" tanpa data pembanding.

---

## 14. Penggunaan Kutipan dan Referensi

1. Gunakan sumber ilmiah untuk definisi, teori, metode, dan konsep teknis.
2. Gunakan sumber institusi resmi untuk profil organisasi dan kebijakan.
3. Gunakan observasi/wawancara untuk kondisi lokal yang memang diamati.
4. Jangan menggunakan sumber blog umum jika tersedia buku, jurnal, dokumentasi resmi, atau regulasi yang lebih kuat.
5. Kutipan harus mendukung klaim yang tepat, bukan ditempel hanya untuk menambah jumlah referensi.
6. Jangan menulis teori yang tidak digunakan lagi pada BAB IV atau BAB V kecuali memang diperlukan sebagai konteks.

---

## 15. Visual, Tabel, dan Gambar

Anggap visual sebagai bagian dari argumen ilmiah.

Gunakan gambar/tabel untuk:

- proses bisnis berjalan;
- proses bisnis usulan;
- use case;
- ERD;
- arsitektur sistem;
- user flow;
- screenshot implementasi;
- hasil pengujian;
- perbandingan expected vs actual;
- rekap kebutuhan.

Setiap visual harus:

- dirujuk di dalam narasi;
- mempunyai judul yang jelas;
- dijelaskan fungsi atau temuan utamanya;
- konsisten dengan implementasi aktual.

Jangan menampilkan diagram yang lebih kompleks daripada pembahasan yang mendukungnya.

---

## 16. Self-Review Lima Dimensi

Sebelum menyatakan suatu bab siap untuk bimbingan, lakukan review lima dimensi berikut.

### A. Kontribusi dan relevansi

- Apa masalah yang benar-benar diselesaikan?
- Apakah pekerjaan ini jelas berbeda dari pekerjaan rutin staf?
- Apakah kontribusi proyek sesuai tingkat Kerja Praktek Teknik Informatika?

### B. Kejelasan penulisan

- Apakah alur paragraf logis?
- Apakah istilah konsisten?
- Apakah setiap subbab mempunyai fungsi yang jelas?
- Apakah pembaca eksternal dapat memahami konteks tanpa asumsi tersembunyi?

### C. Kekuatan bukti

- Apakah setiap klaim utama memiliki sumber atau bukti?
- Apakah observasi dibedakan dari opini?
- Apakah implementasi dibedakan dari rencana?
- Apakah manfaat dibedakan dari hasil pengukuran?

### D. Kelengkapan evaluasi

- Apakah fitur utama telah diuji?
- Apakah skenario gagal/exception diuji?
- Apakah hasil pengujian dapat ditelusuri ke kebutuhan?
- Apakah keterbatasan pengujian dinyatakan?

### E. Kesesuaian desain

- Apakah desain menjawab kebutuhan?
- Apakah implementasi sesuai desain?
- Apakah ada perubahan desain yang belum diperbarui di laporan?
- Apakah scope laporan sama dengan scope proyek aktual?

Semua pertanyaan berisiko tinggi harus diselesaikan atau dinyatakan secara transparan sebelum finalisasi.

---

## 17. Execution Rules untuk AI

1. Selalu pahami target bab/subbab sebelum menulis.
2. Jika tersedia file pedoman, draft laporan, dan dokumentasi proyek, baca hanya bagian yang relevan untuk target edit.
3. Jangan memuat seluruh referensi sekaligus bila tidak diperlukan.
4. Jangan mengarang proses bisnis, requirement, fitur, hasil pengujian, atau kebijakan kampus.
5. Jika ada konflik antara draft laporan dan dokumentasi proyek terbaru, tunjukkan konflik tersebut sebelum merevisi.
6. Jika ada konflik antara pedoman dan draft laporan, pedoman menjadi acuan struktur/formal.
7. Pertahankan istilah domain yang digunakan proyek kecuali memang perlu disederhanakan untuk pembaca akademik.
8. Jika sebuah klaim tidak memiliki bukti, jangan memperkuatnya dengan bahasa retoris.
9. Jika pengguna meminta revisi, pertahankan bagian yang sudah benar dan ubah hanya bagian yang diperlukan agar tidak menciptakan inkonsistensi baru.
10. Saat memperbaiki satu subbab, periksa minimal satu tingkat keterkaitan ke subbab sebelum dan sesudahnya.
11. Saat mengubah Identifikasi Masalah, periksa Rumusan Masalah, Tujuan, Batasan, BAB IV, BAB V, dan Kesimpulan yang berkaitan.
12. Saat mengubah scope sistem, periksa dokumentasi proyek dan seluruh klaim laporan yang terpengaruh.
13. Jangan menggunakan istilah "MVP" dalam laporan akhir apabila konteks akademik lebih tepat menggunakan "ruang lingkup pengembangan awal", "cakupan pengembangan", atau istilah lain yang disetujui pengguna/pembimbing. Istilah MVP masih boleh digunakan pada dokumentasi internal proyek bila memang menjadi terminologi resmi repository.
14. Jangan memindahkan keputusan teknis repository ke laporan tanpa menilai relevansi akademiknya.
15. Jangan menyatakan semua detail implementasi; pilih detail yang membuktikan bagaimana solusi menjawab kebutuhan.

---

## 18. Output Contract

Ketika diminta menyusun atau merevisi suatu bagian laporan, keluaran default harus berisi:

1. **Outline ringkas bagian**: 3–7 poin.
2. **Draft/revisi teks**: paragraf siap ditempatkan pada laporan.
3. **Peran paragraf**: misalnya konteks, masalah, kebutuhan, solusi, bukti, batasan, transisi; dapat disertakan saat pengguna sedang melakukan review, tetapi boleh dihilangkan jika pengguna meminta teks final bersih.
4. **Catatan konsistensi**: bagian laporan lain yang mungkin ikut terdampak oleh revisi.
5. **Self-review singkat**: kejelasan, alur, terminologi, klaim tanpa bukti, dan bukti yang masih kurang.
6. **Claim–evidence map** untuk klaim besar, bila bagian yang dikerjakan memuat fakta atau hasil penting.

Jika pengguna meminta hanya teks final, berikan teks final tanpa penjelasan tambahan, tetapi tetap lakukan pemeriksaan internal di atas sebelum menghasilkan jawaban.

---

## 19. Format Review Cepat

Jika pengguna meminta "review bagian ini", gunakan format:

### Temuan

- masalah struktur;
- masalah argumentasi;
- masalah akademik;
- masalah konsistensi proyek;
- masalah klaim/bukti;
- masalah bahasa jika signifikan.

### Prioritas Revisi

- **Kritis**: dapat menimbulkan pertanyaan penguji atau kontradiksi.
- **Penting**: memperlemah argumentasi atau keterlacakan.
- **Minor**: gaya, diksi, atau kerapian.

### Revisi yang Disarankan

Berikan perubahan yang langsung dapat diterapkan.

---

## 20. Checklist Final Sebelum Bimbingan/Seminar

Sebelum bab atau laporan dinyatakan siap:

- [ ] Struktur mengikuti Pedoman KP 2026.
- [ ] Judul konsisten pada seluruh laporan.
- [ ] Tempat dan ruang lingkup KP konsisten.
- [ ] Tugas rutin staf dan proyek KP dibedakan dengan jelas.
- [ ] Identifikasi masalah berasal dari kondisi yang dapat dipertanggungjawabkan.
- [ ] Rumusan masalah berasal dari identifikasi masalah.
- [ ] Tujuan menjawab rumusan masalah.
- [ ] Batasan masalah sama dengan scope pengembangan aktual.
- [ ] Landasan teori digunakan dalam analisis/pembahasan.
- [ ] Kebutuhan sistem dapat ditelusuri ke masalah.
- [ ] Perancangan dapat ditelusuri ke kebutuhan.
- [ ] Implementasi dapat ditelusuri ke perancangan.
- [ ] Pengujian memverifikasi implementasi/kebutuhan.
- [ ] Kesimpulan hanya menyatakan hal yang didukung hasil.
- [ ] Tidak ada klaim peningkatan kinerja tanpa data.
- [ ] Tidak ada fitur yang diklaim selesai tetapi belum diimplementasikan.
- [ ] Tidak ada fitur out-of-scope yang muncul sebagai deliverable utama.
- [ ] Status integrasi Neofeeder dijelaskan sesuai bukti aktual.
- [ ] Tabel/gambar dirujuk dan dijelaskan dalam narasi.
- [ ] Istilah domain konsisten.
- [ ] Bahasa baku, objektif, dan tidak promosi.
- [ ] Semua sumber yang dikutip benar-benar digunakan.
- [ ] Bagian yang masih berupa usulan diberi penanda yang jelas.

---

## 21. Referensi Skill yang Disarankan

Muat hanya referensi yang diperlukan untuk target pekerjaan saat ini.

- `PEDOMAN-KP-2026.md`: ringkasan struktur dan aturan formal Pedoman KP UNPI.
- `research-paper-writing-skills.md` Cek alur paragraf.

Jangan memuat seluruh reference file sekaligus. Pilih hanya yang diperlukan untuk tugas yang sedang dikerjakan.
