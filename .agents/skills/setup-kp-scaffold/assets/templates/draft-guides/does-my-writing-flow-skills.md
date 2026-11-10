# Apakah Alur Penulisan Saya Sudah Runtut?

> **Jenis dokumen:** Referensi pendukung untuk skill `research-paper-writing-kp-siakad`  
> **Fokus:** Kejelasan, koherensi, kepaduan, dan keringkasan tulisan laporan Kerja Praktek (KP)  
> **Konteks:** Pengembangan Sistem Informasi Akademik (SIAKAD) Berbasis Web pada Fakultas Teknik Universitas Putra Indonesia Cianjur  
> **Penggunaan:** Saat menyusun, merevisi, atau menilai paragraf, subbab, bab, dan hubungan antarbab.

## 1. Tujuan dan Ruang Lingkup

Pertanyaan *“Apakah tulisan ini mengalir dengan baik?”* berarti memeriksa apakah pembaca dapat mengikuti gagasan secara logis tanpa harus menebak hubungan antarpernyataan.

Dalam laporan KP SIAKAD, **alur penulisan yang baik** harus memenuhi empat aspek:

1. **Kejelasan (clarity):** istilah, pelaku, aktivitas, objek data, dan maksud kalimat dapat dipahami.
2. **Koherensi (coherence):** setiap gagasan berkaitan secara logis dengan topik paragraf, subbab, dan tujuan laporan.
3. **Kepaduan (cohesion):** hubungan antarkalimat dan antarparagraf tampak melalui rujukan istilah, urutan informasi, serta transisi yang tepat.
4. **Keringkasan (conciseness):** tidak ada pengulangan, kalimat berputar, atau detail yang tidak mendukung pembahasan.

Kejelasan bahasa tidak boleh menggantikan ketepatan isi. Paragraf yang terdengar lancar tetap harus direvisi apabila menyatakan hasil yang belum terbukti, mencampur kondisi berjalan dengan solusi usulan, atau bertentangan dengan ruang lingkup proyek.

Dokumen ini **bukan** pengganti Pedoman KP Fakultas Teknik UNPI revisi 2026 maupun dokumentasi sumber kebenaran proyek SIAKAD. Gunakan pedoman untuk aturan struktur dan pengetikan; gunakan dokumen proyek dan artefak implementasi untuk ketepatan teknis.

---

## 2. Prinsip Utama: Satu Paragraf, Satu Gagasan

Setiap paragraf harus memiliki satu pesan utama yang dapat diringkas dalam satu kalimat.

Susunan yang dianjurkan:

1. **Kalimat topik:** memperkenalkan pokok pembahasan secara eksplisit.
2. **Kalimat penjelas:** menguraikan konteks, proses, alasan, atau hubungan antarkonsep.
3. **Kalimat pendukung:** memuat fakta observasi, dokumen, rancangan, atau bukti lain yang relevan.
4. **Kalimat penutup atau penghubung (jika diperlukan):** menegaskan makna paragraf atau mengantar ke gagasan berikutnya.

Tidak setiap paragraf harus memiliki empat kalimat atau empat bagian secara kaku. Yang wajib adalah fungsi setiap kalimat jelas dan tidak menyimpang dari pesan utamanya.

**Aturan untuk AI:**

- Identifikasi peran paragraf sebelum mengedit: `konteks`, `kondisi berjalan`, `masalah`, `dampak`, `kebutuhan`, `solusi`, `perancangan`, `implementasi`, `pengujian`, `hasil`, atau `keterbatasan`.
- Jangan menggabungkan dua pesan utama hanya demi mempersingkat teks.
- Jangan memecah satu gagasan menjadi beberapa paragraf pendek tanpa alasan struktural.
- Hindari pengulangan identitas institusi atau judul proyek di setiap paragraf apabila rujukannya sudah jelas.
- Gunakan istilah yang stabil: misalnya *SIAKAD*, *Neofeeder*, *PDDIKTI*, *data akademik*, *kelas perkuliahan*, dan *nilai akhir* sesuai konteks.

---

## 3. Strategi 1: Membaca dari Perspektif Pembaca Eksternal

Penulis memahami sistem karena terlibat langsung dalam pekerjaan operasional maupun pengembangan perangkat lunak. Pembimbing dan penguji belum tentu mengetahui proses administratif Fakultas Teknik, istilah domain SIAKAD, atau status implementasi setiap fitur.

Saat menilai tulisan, AI harus membaca seolah-olah menjadi dosen penguji yang **tidak ikut mengamati kegiatan fakultas dan tidak mengikuti pengembangan source code**.

### 3.1 Pertanyaan pemeriksaan

Untuk setiap paragraf, periksa:

1. Apakah gagasan utama langsung dapat dikenali?
2. Apakah istilah teknis atau singkatan diperkenalkan saat pertama kali digunakan?
3. Apakah subjek, pelaku, objek data, dan aktivitas dapat diidentifikasi dengan jelas?
4. Apakah pembaca bisa membedakan **kondisi yang diamati**, **masalah yang diidentifikasi**, **kebutuhan**, **solusi yang direncanakan**, dan **hasil yang telah diuji**?
5. Apakah kalimat kedua dan seterusnya menjelaskan kalimat topik, bukan membuka topik baru tanpa penghubung?
6. Apakah paragraf mendukung fungsi subbab tempatnya berada?
7. Apakah ada pernyataan yang memerlukan bukti tetapi belum memiliki dasar yang tersedia?

### 3.2 Pemeriksaan konteks khusus KP SIAKAD

- **Tugas rutin staf ≠ proyek KP.** Pengamatan ketika bekerja sebagai Staf Fakultas Teknik dapat menjadi sumber informasi; analisis, perancangan, implementasi, dan pengujian SIAKAD adalah pekerjaan proyek KP.
- **SIAKAD ≠ pengganti Neofeeder.** SIAKAD ditujukan untuk operasional internal; pertukaran data dengan Neofeeder mengikuti batas dan mekanisme yang ditetapkan dalam dokumentasi proyek.
- **Rencana ≠ implementasi.** Kata “dirancang”, “diusulkan”, dan “ditargetkan” tidak boleh diganti menjadi “telah diterapkan”, “berhasil”, atau “terbukti” tanpa bukti.
- **Pengamatan ≠ pengukuran.** Jangan menyatakan proses “lebih cepat”, “lebih efektif”, atau “mengurangi kesalahan sebesar …” tanpa pengukuran atau pengujian yang relevan.
- **Usulan alur nilai ≠ integrasi BAAK yang telah dikembangkan.** Jika alur penerusan nilai kepada BAAK masih perlu divalidasi, tulis sebagai usulan, bukan kapabilitas yang telah tersedia.

### 3.3 Contoh perbaikan

**Kurang jelas:**

> Sistem ini akan membuat proses menjadi lebih mudah dan cepat sehingga semuanya terintegrasi.

**Lebih tepat:**

> SIAKAD dirancang untuk mengelola data akademik dalam satu sistem operasional internal Fakultas Teknik. Data yang tercatat kemudian dapat menjadi sumber bagi proses akademik lain dan mekanisme sinkronisasi dengan Neofeeder sesuai ruang lingkup integrasi yang ditetapkan.

**Alasan:** versi revisi menyebut sistem, jenis data, hubungan antarfungsi, dan batas cakupan, tanpa mengklaim peningkatan kecepatan yang belum diukur.

---

## 4. Strategi 2: Membuat Kerangka Balik (*Reverse Outlining*)

*Reverse outlining* adalah teknik membongkar tulisan yang sudah jadi menjadi kerangka gagasan. Tujuannya untuk memeriksa apakah urutan paragraf mendukung argumen utama dan apakah penjelasannya memang relevan.

### 4.1 Prosedur untuk satu subbab

1. Tentukan **tujuan subbab** dalam satu kalimat.
2. Tuliskan **pesan utama** dari setiap paragraf berdasarkan teks yang benar-benar tertulis, bukan niat penulis.
3. Catat **fakta, bukti, contoh, atau penjelasan** yang mendukung setiap pesan.
4. Periksa apakah tiap pesan terkait langsung dengan tujuan subbab.
5. Periksa apakah bukti benar-benar mendukung pesan paragraf.
6. Telusuri hubungan antarparagraf: `umum → khusus`, `kondisi → masalah`, `masalah → kebutuhan`, `kebutuhan → solusi`, atau `rancangan → penerapan → hasil`.
7. Tandai paragraf yang berulang, melompat topik, kehilangan bukti, atau berada di subbab yang salah.
8. Ubah urutan, pecah, gabungkan, perbaiki, atau hapus bagian yang tidak diperlukan tanpa menghilangkan informasi penting.

### 4.2 Contoh *reverse outline* untuk 1.1 Latar Belakang

| Urutan | Fungsi paragraf | Gagasan utama | Hubungan |
|---|---|---|---|
| 1 | Konteks | Pengelolaan akademik melibatkan data yang saling berkaitan | Membuka kebutuhan umum |
| 2 | Konteks lokal | Fakultas Teknik UNPI mengelola data dan proses akademik pada tingkat fakultas/prodi | Mempersempit konteks |
| 3 | Kondisi berjalan | Sebagian data masih dikelola melalui berkas perkantoran dan arsip tersebar | Menunjukkan kondisi observasi |
| 4 | Masalah operasional | Penugasan dosen dan penyusunan jadwal memerlukan pencocokan manual | Memperinci kendala |
| 5 | Masalah integrasi | Data untuk operasional internal perlu dimasukkan kembali ke Neofeeder | Memperluas masalah ke pelaporan |
| 6 | Kebutuhan solusi | Diperlukan pengelolaan data terpusat dan mekanisme pertukaran data | Menurunkan kebutuhan dari masalah |
| 7 | Alasan pemilihan lokasi | Proses akademik fakultas menjadi konteks penerapan kompetensi Teknik Informatika | Menjelaskan relevansi KP |
| 8 | Proyek yang diusulkan | Pengembangan SIAKAD berbasis web menjadi objek KP | Menyebut respons terhadap kebutuhan |
| 9 | Judul dan luaran | Laporan dan aplikasi mendokumentasikan analisis hingga pengujian | Menutup argumentasi |

Ini adalah **contoh peta argumen**, bukan jumlah paragraf wajib. Sesuaikan dengan draft terbaru dan hindari memaksakan urutan bila menyebabkan pengulangan.

### 4.3 Kriteria hasil pemeriksaan

- **Runtut:** tiap paragraf memiliki peran yang jelas dan urutannya membentuk argumentasi.
- **Perlu revisi:** peran paragraf jelas, tetapi ada transisi lemah, pengulangan, atau urutan kurang tepat.
- **Tidak runtut:** pembaca sulit menentukan hubungan paragraf dengan fokus subbab atau bukti pendukungnya.

Jika *reverse outline* sulit dibuat, periksa kembali kalimat topik, tujuan subbab, dan pembagian gagasan.

---

## 5. Strategi 3: Memanfaatkan Judul dan Subbagian

Judul dan subjudul membantu pembaca memahami struktur tulisan, tetapi **struktur final harus mengikuti Pedoman KP 2026**. AI tidak boleh menambah atau mengubah sistematika resmi hanya untuk memperbaiki alur.

Gunakan judul sementara selama analisis, misalnya:

- `[Konteks akademik]`
- `[Kondisi operasional]`
- `[Masalah pencocokan data]`
- `[Kebutuhan integrasi]`
- `[Solusi SIAKAD]`

Label tersebut digunakan **di luar naskah final** untuk memeriksa organisasi isi. Hapus label analisis apabila subbab resmi tidak memerlukannya.

### 5.1 Pemetaan fungsi bab

| Bab | Pertanyaan utama yang harus dijawab |
|---|---|
| BAB I: Pendahuluan | Mengapa KP dan proyek ini dilakukan, masalah apa yang diangkat, serta apa tujuan dan batasannya? |
| BAB II: Kajian Pustaka | Apa profil tempat KP dan dasar teori yang diperlukan untuk memahami pendekatan penyelesaian masalah? |
| BAB III: Sarana dan Prasarana | Sarana, perangkat, dan lingkungan apa yang mendukung pekerjaan KP? |
| BAB IV: Analisis dan Pembahasan | Bagaimana kondisi berjalan dianalisis dan bagaimana penyelesaian masalah dirancang? |
| BAB V: Implementasi dan Pengujian | Apa yang benar-benar diterapkan, bagaimana diuji, serta apa hasil dan keterbatasannya? |
| BAB VI: Penutup | Kesimpulan apa yang didukung hasil pembahasan/pengujian dan saran apa yang dapat diturunkan? |

Periksa agar teori tidak menggantikan analisis kasus, rencana tidak disajikan sebagai hasil, serta kesimpulan tidak memperkenalkan klaim baru.

---

## 6. Strategi 4: Memakai Transisi Secara Tepat

Kata penghubung dapat memperjelas relasi, tetapi tidak memperbaiki hubungan logis yang memang belum ada. Pilih transisi berdasarkan **hubungan makna**, bukan karena paragraf dianggap membutuhkan penghubung secara otomatis.

| Hubungan | Pilihan ungkapan dalam bahasa Indonesia | Contoh konteks |
|---|---|---|
| Sebab | karena, berdasarkan kondisi tersebut, hal ini berkaitan dengan | Menjelaskan asal kebutuhan |
| Akibat atau konsekuensi | akibatnya, sebagai konsekuensinya, kondisi tersebut menyebabkan *(jika didukung bukti)* | Menjelaskan dampak proses |
| Penambahan | selain itu, di samping itu, aspek lainnya | Menambah persoalan berbeda |
| Perbandingan | serupa dengan, sebagaimana, sejalan dengan | Membandingkan proses atau konsep |
| Pertentangan atau pembatasan | namun, meskipun demikian, berbeda dengan, sementara itu | Memisahkan usulan dan kondisi berjalan |
| Perincian | antara lain, meliputi, secara khusus, pada bagian ini | Memperjelas cakupan |
| Contoh | sebagai contoh, misalnya | Menunjukkan ilustrasi |
| Urutan proses | pada tahap awal, selanjutnya, setelah itu, pada tahap akhir | Menguraikan alur kerja |
| Dasar observasi | berdasarkan pengamatan, berdasarkan dokumen, merujuk pada hasil wawancara | Menandai asal informasi |
| Hasil pengujian | berdasarkan hasil pengujian, pada skenario yang diuji, hasil tersebut menunjukkan | Menginterpretasi bukti uji |
| Simpulan terbatas | dengan demikian, berdasarkan pembahasan tersebut, dapat disimpulkan bahwa | Mengakhiri argumen yang telah ditopang bukti |

**Catatan kebahasaan:** Pedoman KP 2026 meminta bahasa Indonesia baku dan mencantumkan larangan memulai kalimat dengan kata hubung seperti “sehingga” dan “sedangkan”. Hindari kedua bentuk tersebut pada awal kalimat dalam naskah final. Utamakan perumusan hubungan antarkalimat yang eksplisit, bukan sekadar menambahkan “namun” atau “oleh karena itu”.

### 6.1 Contoh transisi antargagasan

**Tanpa hubungan yang jelas:**

> Pengelolaan data akademik dilakukan melalui sejumlah berkas. SIAKAD menggunakan basis data relasional.

**Dengan hubungan yang dijelaskan:**

> Pengelolaan data akademik melalui sejumlah berkas mengharuskan staf menelusuri sumber data yang berbeda. Kondisi tersebut menjadi salah satu dasar kebutuhan penyimpanan data yang terpusat. Oleh karena itu, rancangan SIAKAD menggunakan basis data relasional untuk mengelola keterkaitan antardata akademik.

**Catatan:** kalimat terakhir harus tetap diverifikasi terhadap rancangan atau implementasi yang tersedia.

---

## 7. Pemeriksaan Alur pada Tingkat yang Berbeda

### 7.1 Antarkalimat

Periksa apakah kalimat baru:

- memperinci kalimat sebelumnya;
- menunjukkan sebab, akibat, pembatasan, atau contoh;
- memperkenalkan informasi baru yang memang dibutuhkan;
- tidak mengubah topik tanpa penjelasan.

### 7.2 Antarparagraf

Periksa apakah paragraf berikutnya:

- melanjutkan topik sebelumnya secara logis;
- mempersempit atau memperluas pembahasan dengan alasan jelas;
- tidak mengulang informasi sebelumnya dengan susunan kata lain;
- tetap sesuai dengan fungsi subbab.

### 7.3 Antarsubbab

Periksa urutan argumentasi BAB I, terutama:

`Latar Belakang → Identifikasi Masalah → Rumusan Masalah → Batasan Masalah → Tujuan dan Manfaat`

Setiap masalah utama yang dirumuskan harus dapat ditelusuri ke kondisi yang dijelaskan dalam latar belakang. Batasan membatasi jawaban yang akan dikembangkan, sedangkan tujuan menyatakan pekerjaan yang diperlukan untuk menjawab rumusan masalah.

### 7.4 Antarbab

Gunakan pola keterlacakan:

`Masalah → Kebutuhan Sistem → Rancangan → Implementasi → Pengujian → Hasil → Kesimpulan`

Bila ada kebutuhan yang belum diimplementasikan, tandai sebagai belum selesai atau di luar cakupan hasil, bukan menyembunyikannya demi menjaga kesan tulisan yang utuh.

---

## 8. Pemeriksaan Ketepatan Klaim dan Bukti

Alur tulisan yang runtut belum cukup apabila klaimnya tidak dapat dipertanggungjawabkan.

| Jenis pernyataan | Dasar yang diharapkan | Redaksi bila bukti terbatas |
|---|---|---|
| Kondisi operasional fakultas | Observasi atau dokumen proses | “Berdasarkan pengamatan penulis, …” |
| Kebutuhan pengguna | Observasi, wawancara, atau hasil analisis kebutuhan | “Kebutuhan yang diidentifikasi adalah …” |
| Fitur yang direncanakan | Dokumen scope, rancangan, atau use case | “Sistem dirancang untuk …” |
| Fitur yang sudah dibuat | Kode, UI, API, basis data, atau demonstrasi implementasi | “Fungsi … telah diimplementasikan …” |
| Fitur yang berfungsi sesuai skenario | Bukti pengujian beserta hasil | “Pada skenario pengujian …, sistem …” |
| Peningkatan kinerja | Data pembanding yang diukur dengan metode sesuai | Jangan gunakan klaim peningkatan tanpa data |
| Integrasi Neofeeder berhasil | Log, respons, atau hasil pengujian integrasi | Sebut environment dan entitas yang benar-benar diuji |

Jangan mengarang kutipan, hasil wawancara, tanggal, statistik, waktu pemrosesan, hasil *user acceptance test*, atau status integrasi.

---

## 9. Prosedur Revisi untuk AI

Ketika pengguna meminta **“periksa flow”**, **“buat lebih terpadu”**, **“perbaiki alur paragraf”**, atau **“apakah bagian ini sudah runtut?”**, lakukan langkah berikut:

1. **Tetapkan objek evaluasi:** paragraf, subbab, bab, atau hubungan antarbab.
2. **Pahami tujuannya:** identifikasi fungsi akademik bagian tersebut sesuai Pedoman KP.
3. **Buat *reverse outline* ringkas:** tulis pesan utama tiap paragraf dan relasi antargagasannya.
4. **Diagnostik masalah:** klasifikasikan sebagai `kejelasan`, `koherensi`, `kepaduan`, `keringkasan`, `ketepatan istilah`, `ketepatan posisi bagian`, atau `klaim tanpa bukti`.
5. **Tentukan tingkat revisi:** diksi, kalimat, paragraf, urutan paragraf, atau struktur subbab. Jangan melakukan perubahan besar jika tidak dibutuhkan.
6. **Revisi dengan perubahan minimum yang efektif:** pertahankan fakta, maksud penulis, ruang lingkup, dan pernyataan yang telah disetujui pembimbing.
7. **Cek ulang sumber:** cocokkan klaim dengan observasi, dokumen proyek, artefak implementasi, atau pengujian yang benar-benar tersedia.
8. **Uji sebagai pembaca eksternal:** baca hasil revisi tanpa mengandalkan konteks percakapan.
9. **Laporkan perubahan substantif:** jelaskan penggabungan/pemindahan paragraf, perubahan kadar klaim, dan bukti yang masih kurang.

Jika pengguna meminta **analisis terlebih dahulu**, berikan temuan dan usulan tanpa langsung mengubah dokumen. Lakukan pengeditan setelah pengguna menyetujuinya.

---

## 10. Format Keluaran yang Dianjurkan

Jangan menampilkan semua checklist internal untuk setiap permintaan kecil. Sesuaikan keluaran dengan cakupan pekerjaan.

### Untuk satu paragraf

1. **Penilaian singkat:** runtut / perlu revisi / tidak runtut.
2. **Masalah utama:** sebutkan bagian spesifik yang mengganggu pembacaan.
3. **Paragraf revisi:** teks siap dimasukkan ke laporan.
4. **Catatan bukti:** hanya jika ada klaim yang belum dapat diverifikasi.

### Untuk satu subbab atau lebih

1. **Tujuan bagian dan *reverse outline*.**
2. **Temuan utama:** urutan, pengulangan, transisi, posisi argumen, ketepatan bukti.
3. **Naskah revisi:** pertahankan nomor subbab resmi.
4. **Ringkasan perubahan dan alasan.**
5. **Peta klaim–bukti** untuk pernyataan berisiko atau substantif.

Format peta klaim–bukti:

`Klaim: ... | Dasar: ... | Status: didukung / perlu bukti / masih berupa usulan`

---

## 11. Daftar Periksa Akhir

Sebelum menyatakan alur tulisan sudah baik, pastikan:

- [ ] Setiap paragraf memiliki satu gagasan utama.
- [ ] Kalimat pertama memperkenalkan fokus paragraf dengan jelas.
- [ ] Istilah dan referennya dapat dipahami tanpa konteks tersembunyi.
- [ ] Hubungan antarkalimat dan antarparagraf logis.
- [ ] Tiap paragraf berkontribusi pada tujuan subbab.
- [ ] Tidak ada pengulangan yang tidak diperlukan.
- [ ] Alur antarsubbab dan antarbab konsisten.
- [ ] Kondisi berjalan, usulan, rancangan, implementasi, dan hasil pengujian dibedakan.
- [ ] Klaim penting memiliki dasar yang sesuai.
- [ ] Konteks Fakultas Teknik UNPI dan batas proyek SIAKAD dipertahankan.
- [ ] Pekerjaan rutin staf tidak dicampur dengan luaran proyek KP.
- [ ] Penomoran dan sistematika resmi laporan tidak diubah tanpa alasan dan persetujuan.
- [ ] Redaksi menggunakan bahasa Indonesia baku sesuai Pedoman KP 2026.

**Prinsip penutup:** Tulisan dikatakan runtut apabila pembaca dapat memahami *apa yang dibahas, mengapa hal itu dibahas, bagaimana gagasan tersebut berkaitan dengan bagian sebelumnya, dan bukti apa yang mendukungnya*, tanpa harus menebak maksud penulis.
