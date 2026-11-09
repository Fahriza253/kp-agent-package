---
name: kp-source-learning
description: Mempelajari sumber yang diberikan pengguna (contoh laporan KP, pedoman institusi lain, panduan gaya, artikel, atau dokumentasi) dan mengubahnya menjadi catatan pengetahuan terstruktur di docs/agents/knowledge/. Menyimpan pola, bukan teks. Dipakai untuk intent LEARN. Penulisan berkas memerlukan konfirmasi.
---

# KP Source Learning

Skill ini membuat agen dapat belajar dari sumber yang diberikan. Hasil belajar disimpan sebagai catatan pengetahuan yang bisa dipakai ulang oleh skill lain. Naskah tidak berubah oleh skill ini.

## 1. Prinsip

- **Pola, bukan salinan.** Catatan menyimpan struktur, pola argumen, pola kalimat, dan aturan. Catatan tidak menyalin paragraf panjang dari sumber.
- **Sumber dicatat.** Setiap catatan menyebut asal, jenis, tanggal sumber, dan keandalannya.
- **Pedoman menang.** Jika sumber bertentangan dengan pedoman kampus, pedoman menang dan konflik dicatat.
- **Tidak menyimpan fakta yang belum diverifikasi.** Klaim faktual dari sumber hanya dicatat sebagai "menurut sumber ini" dan tidak masuk ke naskah tanpa verifikasi.

## 2. Alur

1. **Terima sumber.** Pengguna memberikan berkas, tautan, atau teks. Jika berkas ada di `/mnt/user-data/uploads/` atau di repositori, baca dari sana. Jika tautan, buka hanya bila diizinkan.
2. **Klasifikasikan.** Tentukan jenis: pedoman institusi, contoh laporan, panduan gaya, artikel ilmiah, dokumentasi teknis, atau lainnya.
3. **Ekstrak pola.** Ambil hal-hal berikut bila tersedia:
   - struktur bab dan subbab;
   - fungsi setiap bagian;
   - pola argumen (masalah ke solusi, kebutuhan ke rancangan);
   - pola penyajian (tabel, gambar, urutan penjelasan);
   - aturan format dan sitasi;
   - contoh kalimat pembuka dan penutup bagian yang menunjukkan gaya, tanpa menyalin.
4. **Bandingkan dengan proyek.** Tandai pola yang cocok, pola yang bertentangan dengan pedoman, dan pola yang tidak relevan untuk KP.
5. **Tampilkan ringkasan dan minta konfirmasi.** Sebelum menyimpan, tampilkan rancangan catatan dan minta persetujuan.
6. **Simpan.** Setelah disetujui, tulis ke `docs/agents/knowledge/<slug>.md` dengan format di bawah.

## 3. Format catatan

```markdown
---
name: <slug>
source: <nama, tautan, atau nama berkas>
type: <pedoman | contoh-laporan | panduan-gaya | artikel | dokumentasi | lainnya>
source_date: <tanggal terbit atau versi, bila ada>
reliability: <tinggi | sedang | rendah, dengan alasan singkat>
scope: <bagian laporan atau aspek yang relevan>
status: <draf | disetujui>
conflicts_with_pedoman: <daftar konflik, atau "tidak ada">
---

## Ringkasan

Dua sampai empat kalimat tentang isi sumber dan kegunaannya bagi KP.

## Pola struktur

Daftar bab atau subbab dengan fungsi masing-masing.

## Pola argumen

Pola yang bisa dipakai, dijelaskan dalam kalimat sendiri.

## Aturan format dan sitasi

Aturan yang berlaku dari sumber ini, dengan rujukan halaman atau bagian.

## Yang tidak dipakai

Pola dari sumber yang sengaja tidak diambil, beserta alasannya.

## Catatan verifikasi

Klaim faktual dari sumber yang belum diverifikasi.
```

## 4. Batasan hak cipta dan kutipan

- Jangan menyalin paragraf panjang dari sumber ke catatan maupun ke naskah. Ringkas dengan kata sendiri.
- Jika perlu mengutip, batasi pada frasa pendek dan beri sitasi sesuai `kp-20`.
- Jangan mengutip jurnal dari `resources/journal/` ke naskah tanpa konfirmasi eksplisit.

## 5. Yang tidak boleh dilakukan

- Menganggap contoh laporan lain sebagai standar mutlak tanpa mengecek pedoman.
- Menyimpan informasi pribadi atau data identitas dari contoh laporan.
- Menyimpan catatan yang berisi klaim hasil atau data orang lain sebagai fakta penulis.
- Menulis catatan ke repositori tanpa konfirmasi.
