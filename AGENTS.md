# Panduan agen: paket penulisan Laporan KP

Repositori ini menerbitkan **skill** penulisan laporan KP (dan lapisan akademik reusable) untuk Cursor, plus **rules** proyek di `.cursor/rules/`. Skill engineering pihak ketiga ada di `.agents/skills/` lewat `skills-lock.json`.

- **GitHub (publik)**: https://github.com/Fahriza253/kp-agent-package
- **Skills CLI**: `npx skills@latest add Fahriza253/kp-agent-package -a cursor`

- **Edit katalog**: `skills/academic/`, `skills/kp/`
- **Dogfooding**: salinan skill yang sama di `.agents/skills/`
- **Rules**: `.cursor/rules/` (salin ke repo laporan pengguna; tidak ikut `npx skills`)

Tugas KP di workspace laporan: muat skill `kp-intent-router` dan rules `kp-00-core.mdc`. Panduan contoh penggunaan: `docs/agents/panduan-penggunaan-skills.md`. Tugas pemeliharaan paket ini: skill engineering + dokumentasi di `docs/agents/`.

## Agent skills

### Issue tracker

Isu dan spesifikasi ditulis sebagai berkas Markdown di `.scratch/`. Lihat `docs/agents/issue-tracker.md`.

### Triage labels

Lima peran triage canonical. Lihat `docs/agents/triage-labels.md`.

### Domain docs

Layout **single-context**. Lihat `docs/agents/domain.md` dan `GLOSSARY.md`.
