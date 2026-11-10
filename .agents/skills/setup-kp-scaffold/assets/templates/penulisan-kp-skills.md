# Prosedur penulisan draft KP (repo laporan)

Berkas ini memenuhi rujukan di `kp-00-core.mdc`. Rincian per bab dan workflow ada di **`docs/agents/draft-guides/`** (indeks: [README.md](draft-guides/README.md)).

## Urutan kerja agen

1. Baca `docs/agents/progress-laporan.md`.
2. Muat `kp-intent-router`, lalu skill untuk intent DRAFT atau REVISE.
3. Buka **hanya modul yang relevan** menurut tabel di `draft-guides/README.md` (jangan memuat keempat berkas penuh sekaligus).
4. Ikuti `kp-draft-section`, `academic-writing-core`, rules `kp-10` dan `kp-20`.
5. Jangan menulis sitasi atau data tanpa konfirmasi (lihat `kp-00`).

## Tiga lapisan panduan

| Lapisan | Lokasi |
| ------- | ------ |
| Router dan skill Cursor | `kp-intent-router`, `kp-draft-section`, `academic-writing-core` |
| Panduan draft modular | `docs/agents/draft-guides/` |
| Pedoman kampus | `resources/PEDOMAN-KP-2026.md` (otoritas struktur) |

Sesuaikan contoh konteks SIAKAD di panduan dengan judul dan lembaga di progress Anda.
