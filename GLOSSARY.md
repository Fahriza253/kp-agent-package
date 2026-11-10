# Glosarium (Laporan KP)

Istilah yang dipakai agen dan dokumentasi proyek saat mengerjakan naskah laporan.

## Naskah Word resmi

Berkas `laporan/DRAFT LAPORAN KP - SIAKAD FT - DAFA FAWAZ.docx`. Naskah kerja utama untuk tata letak, gaya Word, nomor halaman, daftar isi otomatis, dan penyerahan akhir. Agen tidak mengganti peran DOCX sebagai acuan format cetak; perubahan teks substantif dimulai dari naskah Markdown kerja kecuali pengguna meminta sebaliknya.

## Naskah Markdown kerja

Berkas `laporan/ARCHIVE/DRAFT_KP.md`. Representasi teks laporan untuk revisi di repositori: diff Git, tinjauan agen, dan penyuntingan bab. Isinya selaras dengan naskah Word resmi; Markdown bukan pengganti paginasi atau template Word.

## Sinkronisasi naskah

Proses menjaga teks Markdown kerja dan naskah Word resmi selaras. Alur baku: edit `DRAFT_KP.md`, lalu port perubahan ke DOCX (salin/tempel terarah, `scripts/generate_laporan_docx.py`, atau konversi yang disetujui pengguna). Setelah port, verifikasi struktur bab dan format Word di DOCX. Prinsip agen: `AGENTS.md`.

## Generator DOCX dari Markdown (`generate_laporan_docx.py`)

Skrip `scripts/generate_laporan_docx.py` membuat berkas `.docx` **baru** dari `DRAFT_KP.md` dengan gaya template naskah Word resmi. Template dan DOCX resmi di `laporan/` tidak ditimpa; keluaran baku disimpan di `laporan/GENERATED/` (nama ber-cap waktu). Gambar di-resolve ke `laporan/assets/images/` (registri `manifest.json`); ekstraksi dari Word resmi: `scripts/extract_laporan_docx_images.py`. Bila berkas tidak ada, diganti catatan untuk sisip manual. Detail: docstring skrip dan `laporan/assets/images/README.md`.

## Paket skill penulisan KP

Tiga berkas di `.custom-skills/my-research-paper-writing/` yang **wajib** dipakai agen saat menyusun atau merevisi teks draft laporan: skill utama `research-paper-writing-skills.md`, lapisan gaya `human-academic-writing-kp-skills.md`, dan pemeriksaan alur `does-my-writing-flow-skills.md`. Urutan dan prioritas: bagian Penulisan draft KP di `AGENTS.md`.

## Referensi Kerja Praktik

Folder `resources/` menyimpan **bahan rujukan** pengerjaan KP (pedoman kampus dan konteks proyek). Indeks lengkap, prioritas pemakaian, dan peringatan bundel teknis: `resources/README.md`.

| Jenis rujukan                  | Lokasi                                                     | Peran singkat                                                                                              |
| ------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Pedoman kampus                 | `resources/PEDOMAN-KP-2026.md`                             | Panduan utama FT UNPI: struktur laporan, penyusunan, pengetikan                                            |
| Catatan implementasi developer | `resources/technical/` (`README.md`, bundel `SIAKAD_*.md`) | Murni catatan developer SIAKAD; bukan naskah KP; non-SSOT, verifikasi sebelum klaim di laporan             |
| Jurnal rujukan KP              | `resources/journal/` (`README.md`, PDF)                    | Literatur pendukung landasan teori; petunjuk penulisan; sitasi ke naskah hanya setelah konfirmasi pengguna |
| Masukan pembimbing             | `revisi/`                                                  | Arah revisi setelah selaras dengan pedoman                                                                 |

## Sumber kebenaran menurut tugas

| Tugas agen                                                     | Sumber utama                                                                                               |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Revisi teks, struktur bab, diff, commit                        | `laporan/ARCHIVE/DRAFT_KP.md`                                                                              |
| Draft DOCX baru dari Markdown (gaya template, non-destructive) | `scripts/generate_laporan_docx.py` → `laporan/GENERATED/`; docstring skrip                                 |
| Format halaman, gaya institusi, DOCX final                     | `laporan/DRAFT LAPORAN KP - SIAKAD FT - DAFA FAWAZ.docx`                                                   |
| Pedoman struktur dan ketentuan KP                              | `resources/PEDOMAN-KP-2026.md` (indeks: `resources/README.md`)                                             |
| Fakta proyek SIAKAD (klaim implementasi, domain)               | Kode, pengujian, dan dokumen sumber proyek; `resources/technical/` hanya catatan developer untuk navigasi  |
| Landasan teori dan gaya kajian pustaka (agen)                  | `resources/journal/` (baca untuk arah tulisan); kutipan ke naskah setelah konfirmasi pengguna + pedoman KP |
| Masukan pembimbing                                             | `revisi/`                                                                                                  |
| Struktur bab, klaim–bukti, gaya, alur tulisan (agen)           | `.custom-skills/my-research-paper-writing/` (tiga berkas skill; `AGENTS.md`)                               |
