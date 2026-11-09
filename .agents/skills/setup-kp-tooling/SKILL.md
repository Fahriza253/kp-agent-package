---
name: setup-kp-tooling
description: Memasang skrip validasi Markdown dan generator DOCX minimal ke repo laporan (scripts/). Dipakai saat bootstrap atau bila scripts/ belum ada. Bagian dari keluarga setup-kp-*.
---

# Setup KP Tooling

Skill ini menyalin bundle skrip dari paket ke `scripts/` di **repo laporan** pengguna. Skrip ini direferensikan `kp-00`, `kp-audit`, dan `kp-docx-sync`.

## Prasyarat

- Root workspace adalah repo laporan.
- Skill dipasang lewat CLI (`npx skills add`) sehingga path `.agents/skills/setup-kp-tooling/` tersedia.

## Langkah

1. Konfirmasi tidak menimpa skrip kustom pengguna. Jika `scripts/generate_laporan_docx.py` sudah ada dan berbeda dari bundle, hentikan dan tanyakan.
2. Jalankan:

   ```bash
   bash .agents/skills/setup-kp-tooling/scripts/install-tooling.sh .
   ```

   Dari repo pemeliharaan paket:

   ```bash
   bash skills/kp/setup-kp-tooling/scripts/install-tooling.sh /path/ke/repo-laporan
   ```

3. Verifikasi: `python scripts/check_project_markdown.py` dari akar repo (boleh exit 0 pada repo baru).
4. Opsional: `python3 -m venv .venv` lalu `pip install -r scripts/requirements-docx.txt` bila pengguna akan memakai `kp-docx-sync`.

## Isi bundle

| Berkas | Fungsi |
| ------ | ------ |
| `check_project_markdown.py` | Menolak em dash U+2014; mengecualikan path yang mengandung `laporan/archive` |
| `generate_laporan_docx.py` | Konversi minimal `laporan/ARCHIVE/DRAFT_KP.md` ke `laporan/GENERATED/` |
| `requirements-docx.txt` | Dependensi generator |

Generator minimal boleh diganti salinan dari repo referensi mahasiswa. Jangan menimpa tanpa konfirmasi.

## Yang tidak boleh dilakukan

- Menimpa skrip pengguna tanpa persetujuan.
- Menyatakan generator minimal setara template kampus tanpa pemeriksaan manual.
