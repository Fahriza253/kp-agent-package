---
name: kp-intent-router
description: Titik masuk untuk setiap tugas penulisan Laporan Kerja Praktik. Membaca status proyek, menentukan intent pengguna (brainstorm, draft, revisi, celah improvement, audit, validasi, belajar dari sumber, humanize, sinkronisasi DOCX, status), lalu memuat hanya skill dan rules yang relevan. Gunakan di awal setiap sesi atau setiap kali tujuan pengguna belum jelas.
---

# KP Intent Router

Skill ini dipakai di awal setiap tugas. Ia memastikan agen tahu posisi naskah, tahu apa yang diminta, dan memuat konteks yang tepat tanpa membebani sesi.

## Langkah 1. Baca status

Baca `docs/agents/progress-laporan.md`. Dari berkas itu, ambil:

- posisi naskah kerja dan naskah Word;
- status tiap bab;
- keputusan yang sudah dikonfirmasi;
- keputusan yang menunggu konfirmasi;
- catatan sesi terakhir.

Jika berkas tidak ada, kenali intent **SETUP**, muat skill `setup-kp-repo`, dan tawarkan bootstrap (rules, scaffold, tooling). Template progress ada di skill `setup-kp-scaffold` dan, setelah scaffold, di `docs/agents/progress-laporan.md`. Jangan membuat berkas tanpa konfirmasi.

Jika progress ada tetapi audit VALIDATE atau `verify-layout.sh` menunjukkan berkas hilang, arahkan ke `setup-kp-repo` atau langkah setup yang sesuai. Peta lengkap: `skills/kp/references/workspace-document-contract.md` (di repo paket) atau salinan di dokumentasi tim Anda.

Jika status berkas bertentangan dengan draf yang sebenarnya (misalnya status menyebut bab V selesai tetapi bab itu tidak ada di draf), tampilkan konfliknya dan tanyakan sebelum bekerja.

## Langkah 2. Tentukan intent

Pilih satu intent utama. Jika pengguna meminta beberapa hal, urutkan dan kerjakan satu per satu.

| Intent       | Ciri permintaan                                                                  | Skill yang dimuat                                                       |
| ------------ | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| BRAINSTORM   | "ide", "adu gagasan", "bandingkan pendekatan", "kritik ide ini", "apa kelemahan argumen ini" | `kp-ideation`, `academic-writing-core` (bagian 1 dan 3)                 |
| DRAFT        | "tulis", "buat draf", "lengkapi subbab", "susun bab"                            | `kp-draft-section`, `academic-writing-core`, `kp-10`, `kp-20`           |
| REVISE       | "perbaiki", "revisi", "ubah", "susun ulang paragraf"                             | `kp-draft-section` (mode revisi), `academic-writing-core`, `kp-10`, `kp-20` |
| AUDIT        | "periksa menyeluruh", "audit", "apakah sudah konsisten", "cek klaim"             | `kp-audit` (mode audit)                                                 |
| IMPROVE      | "celah", "improvement", "apa yang kurang", "bagian mana yang lemah", "review"   | `kp-audit` (mode gap), tanpa perubahan berkas                           |
| VALIDATE     | "validasi", "cek format", "cek sitasi", "cek tanda baca", "jalankan check"       | `kp-audit` (mode validate), `kp-20`                                     |
| LEARN        | "pelajari sumber ini", "ini contoh laporan", "ini pedoman lain", lampiran contoh | `kp-source-learning`                                                    |
| HUMANIZE     | "humanize", "deslop", "kurangi kesan AI", "rapikan gaya"                         | `academic-humanize`, `kp-10`, `kp-00`; lihat catatan di bawah           |
| SYNC         | "buat DOCX", "port ke Word", "sinkronkan"                                        | `kp-docx-sync`                                                          |
| SETUP        | "setup repo", "bootstrap laporan", progress/draf belum ada, "pasang KP dari nol" | `setup-kp-repo`, `setup-kp-rules`, `setup-kp-scaffold`, `setup-kp-tooling` |
| STATUS       | "di mana posisi kita", "apa yang belum", "ringkasan kemajuan"                    | Hanya `docs/agents/progress-laporan.md` dan `kp-00`                     |

Catatan HUMANIZE: pengguna dapat menjalankan skill ini sendiri, atau meminta agen lain melakukannya. Dalam kedua kasus, agen wajib membaca `kp-00` dan `kp-10` dan menyertakan brief serah terima dari `academic-humanize` bagian 8.

## Langkah 3. Muat skill secara selektif

Muat hanya skill yang tercantum untuk intent itu. Jika pekerjaan ternyata membutuhkan intent lain (misalnya REVISE membuka masalah konsistensi yang harus diaudit), tambahkan skill itu dan beri tahu pengguna dalam satu kalimat.

Untuk setiap bagian yang akan dikerjakan, baca hanya bagian draf, pedoman, dan sumber yang relevan dengan bagian itu.

## Langkah 4. Nyatakan rencana

Sebelum mengubah berkas, tulis rencana dalam tiga sampai lima baris:

- intent yang dikenali;
- bagian yang akan disentuh;
- skill yang dimuat;
- perubahan yang memerlukan konfirmasi (lihat `kp-00` bagian "Wajib konfirmasi dulu").

Jika intent tidak jelas, ajukan satu pertanyaan saja. Jangan mengajukan daftar pertanyaan panjang.

## Langkah 5. Tutup sesi

Di akhir tugas yang mengubah sesuatu, perbarui `docs/agents/progress-laporan.md` dengan catatan sesi singkat: tanggal, intent, apa yang berubah, dan apa yang masih menunggu. Pengguna sudah memberi izin untuk ini. Sebutkan dalam satu kalimat bahwa berkas itu diperbarui.

## Aturan umum

- Jangan memuat seluruh referensi sekaligus. Baca pedoman dan sumber per bagian.
- Jika tugas tidak termasuk penulisan laporan (misalnya pertanyaan umum tentang Git atau Python), jawab langsung tanpa memuat skill KP.
- Balasan kepada pengguna dalam bahasa Indonesia.
