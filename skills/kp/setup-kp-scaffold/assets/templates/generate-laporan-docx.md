# Generator DOCX laporan KP

## Lokasi

- Skrip: `scripts/generate_laporan_docx.py`
- Dependensi: `scripts/requirements-docx.txt`

## Pemakaian singkat

Dari akar repo laporan:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements-docx.txt
.venv/bin/python scripts/generate_laporan_docx.py
```

Opsi `--out` menolak target yang sudah ada dan menolak path yang mengindikasikan naskah Word resmi di `laporan/`.

Detail alur dan checklist manual ada di skill `kp-docx-sync`.
