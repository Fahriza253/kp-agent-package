# Paket Agen Penulisan Laporan KP (Cursor)

Paket skill dan rules Cursor untuk Laporan Kerja Praktik Teknik Informatika UNPI Cianjur. Lapisan **reusable** (`skills/academic/`) dapat dipakai untuk skripsi atau makalah lain; lapisan **KP** (`skills/kp/`) mengikat pedoman dan alur naskah KP.

## Struktur repositori

```
skills/
  academic/                  Skill reusable (SKILL.md per folder)
  kp/                        Skill khusus KP
.agents/skills/              Salinan untuk dogfooding + skill engineering pihak ketiga
.cursor/rules/               Rules KP (.mdc); salin ke workspace laporan
docs/agents/                 Dokumentasi agen (domain, progress template, dll.)
```

## Pemasangan di workspace laporan

Ganti `<owner>/<repo>` dengan URL GitHub paket ini setelah dipublish.

### 1. Skill (Skills CLI)

Dari root repositori laporan:

```bash
npx skills@latest add <owner>/<repo> -a cursor
```

Pilih skill yang diinginkan (semua `kp-*` dan/atau `academic-*`). CLI memasang ke **`.agents/skills/<nama>/`**. Untuk skill global di semua proyek, tambahkan `-g`.

Lihat [Agent Skills (Cursor)](https://cursor.com/docs/skills).

### 2. Bootstrap repo (disarankan)

Rules **tidak** ikut instalasi `npx skills`. Untuk repo laporan baru, minta agen menjalankan skill **`setup-kp-repo`** (intent SETUP), atau jalankan berurutan:

```bash
bash .agents/skills/setup-kp-rules/scripts/install-rules.sh .
bash .agents/skills/setup-kp-scaffold/scripts/scaffold.sh .
bash .agents/skills/setup-kp-tooling/scripts/install-tooling.sh .
bash .agents/skills/setup-kp-repo/scripts/verify-layout.sh .
```

Alias rules: `kp-install-rules` memakai bundle yang sama dengan `setup-kp-rules`.

### 3. Isian manual setelah scaffold

- `resources/PEDOMAN-KP-2026.md` (dari sumber kampus)
- DOCX resmi di `laporan/`; path dicatat di `docs/agents/progress-laporan.md`
- Opsional: submodule `siakad/`, folder `.custom-skills/my-research-paper-writing/`

Mulai sesi dengan: "Setup repo KP" atau "Cek posisi laporan, lalu ringkas BAB IV." Agen memuat `kp-intent-router` (SETUP atau STATUS/DRAFT).

## Pengembangan paket ini

1. Edit skill di `skills/kp/` atau `skills/academic/`.
2. Edit rules di `.cursor/rules/` (kanonik), lalu jalankan:

   ```bash
   npm run sync:skills
   # atau: bash scripts/sync_catalog_to_agents.sh
   ```

   Skrip menyelaraskan `.agents/skills/` dan bundle rules di `kp-install-rules`.
3. Skill engineering: `npx skills@latest add mattpocock/skills -a cursor` (pin di `skills-lock.json`).

## Verifikasi CLI

Diuji: `npx skills@latest add <path-atau-github-repo> -a cursor -y` mendeteksi skill di `skills/academic/` dan `skills/kp/` (termasuk keluarga `setup-kp-*` dan `kp-install-rules`).

## Cara kerja agen (di repo laporan)

1. `kp-00-core.mdc` selalu aktif.
2. Tugas dimulai dari skill `kp-intent-router`.
3. DRAFT/REVISE memakai `kp-draft-section` + `academic-writing-core`.
4. Perubahan substantif, sitasi, knowledge, dan DOCX menunggu konfirmasi (lihat rule inti).

## Peta intent

| Intent     | Skill utama                    |
| ---------- | ------------------------------ |
| BRAINSTORM | kp-ideation                    |
| DRAFT      | kp-draft-section               |
| REVISE     | kp-draft-section (mode revisi) |
| AUDIT      | kp-audit (audit)               |
| IMPROVE    | kp-audit (gap)                 |
| VALIDATE   | kp-audit (validate)            |
| LEARN      | kp-source-learning             |
| HUMANIZE   | academic-humanize              |
| SYNC       | kp-docx-sync                   |
| SETUP      | setup-kp-repo                  |
| STATUS     | progress-laporan.md            |

Singkatan `kp-10` dan `kp-20` di dalam skill merujuk ke `kp-10-pedoman-format.mdc` dan `kp-20-sitasi-apa.mdc`.

## Memakai ulang di proyek lain

- Install hanya `academic-writing-core` dan `academic-humanize` lewat CLI.
- Untuk skripsi atau makalah: rules format baru + skill draft versi proyek Anda.

## Keputusan atas konflik (naskah KP)

1. Bab V mengikuti pedoman, tanpa subjudul tersendiri.
2. _Sehingga_ dan _sedangkan_ tidak di awal kalimat (did audit, tidak diubah otomatis).
3. Sitasi: _et al._ untuk 3+ penulis, _n.d._ jika tanggal tidak ada, "&" untuk dua penulis.

## Yang perlu diverifikasi

- Edisi APA yang berlaku di kampus.
- Perilaku Cursor untuk `paths`, `alwaysApply`, dan discovery skill di versi tim Anda.
- URL repo GitHub untuk `npx skills add` setelah publish (path lokal sudah valid untuk uji).
