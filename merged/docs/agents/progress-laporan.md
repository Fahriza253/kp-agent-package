# Status Laporan KP

Berkas ini dibaca agen di awal setiap tugas (lihat skill `kp-intent-router`). Perbarui hanya setelah pengguna setuju, atau bila pengguna meminta.

Terakhir diperbarui: 2026-11-09

## Posisi naskah

- Naskah kerja (edit default): `laporan/ARCHIVE/DRAFT_KP.md`
- Naskah Word resmi: `laporan/DRAFT LAPORAN KP - SIAKAD FT - DAFA FAWAZ.docx`
- Terakhir disinkronkan ke Word: belum diketahui (perlu dicek di repositori)
- Pedoman: `resources/PEDOMAN-KP-2026.md`
- Masukan pembimbing: `revisi/7-Oktober-2026.md` (dirujuk README, berkasnya belum diunggah ke sesi ini)

## Status per bab

| Bagian                                    | Status di DRAFT_KP.md      | Catatan terbuka                                                   |
| ----------------------------------------- | -------------------------- | ----------------------------------------------------------------- |
| Bagian awal (sampul s.d. daftar lampiran) | Belum ada di DRAFT_KP.md   | Tidak ditemukan prakata, pengesahan, atau daftar isi              |
| BAB I Pendahuluan                         | Ada (1.1 s.d. 1.8)         | Belum diaudit (jalankan kp-audit mode gap)                        |
| BAB II Kajian Pustaka                     | Ada (2.1 s.d. 2.2.4.4)     | Belum diaudit. Sumber landasan teori perlu dicek                  |
| BAB III Sarana dan Prasarana              | Ada (3.1 s.d. 3.4)         | Belum diaudit. Verifikasi versi dan perangkat dengan berkas nyata |
| BAB IV Analisis dan Pembahasan            | Ada (4.1 s.d. 4.7.3)       | Perlu audit konsistensi dengan BAB I dan II                       |
| BAB V Implementasi dan Pengujian          | Belum ada di DRAFT_KP.md   | Tanpa subjudul tersendiri (pedoman)                               |
| BAB VI Penutup                            | Belum ada di DRAFT_KP.md   | Menunggu BAB V                                                    |
| Daftar pustaka                            | Ada, format APA 7 campuran | Migrasi t.t. ke n.d. dan et al. perlu konfirmasi per batch        |
| Lampiran                                  | Belum ada                  | Belum ada di draf                                                 |

## Keputusan yang sudah dikonfirmasi

- Gaya sitasi dasar: APA (edisi yang berlaku diverifikasi sebelum dipakai).
- Sitasi tiga penulis atau lebih: _et al._
- Tanggal tidak tersedia: _n.d._
- Bab V: ikuti pedoman, satu bab terpadu tanpa subjudul tersendiri.
- Kata hubung _sehingga_ dan _sedangkan_ tidak boleh di awal kalimat. Kemunculannya di draf didaftar untuk revisi, tidak diubah otomatis.
- Bahasa utama: Indonesia baku. Istilah Inggris diterima bila lazim.
- Agen wajib konfirmasi sebelum menambah atau mengubah sitasi, klaim, scope, bab, atau DOCX.
- Agen boleh belajar dari sumber yang diberikan, tetapi menyimpan hasilnya ke repositori hanya setelah konfirmasi.
- Agen boleh memperbarui berkas ini di akhir sesi tanpa konfirmasi tambahan.
- Sitasi dua penulis: "&" di semua posisi (dalam kurung dan dalam narasi).

## Keputusan yang menunggu konfirmasi

1. Migrasi entri _t.t._ di draf ke _n.d._: perlu konfirmasi per batch.

## Dilewati atas permintaan pengguna

- Istilah "Skripsi" pada kalimat judul halaman sampul pedoman. Jangan diangkat lagi kecuali pengguna membukanya sendiri.
- Bahasa sitasi di teks. Tidak dibahas.

## Daftar sitasi terverifikasi

Isi bertahap. Hanya sumber yang sudah dibuka dan dicek agen atau pengguna.

- [belum ada]

## Riwayat sesi

- 2026-11-09: IMPROVE (kp-audit mode gap) dan pemasangan paket. Perubahan: mode viewer diganti mode gap, router dan kp-docx-sync disesuaikan dengan generator dan prosedur penulisan di repo. Temuan: DRAFT_KP.md belum memuat bagian awal, tabel, gambar, atau lampiran; skrip check_project_markdown.py mengecualikan laporan/archive/ sehingga em dash di draf tidak terperiksa otomatis. Yang masih menunggu: migrasi t.t. ke n.d. per batch; BAB V dan VI belum ditulis.
