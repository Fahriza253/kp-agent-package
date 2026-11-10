# Domain Docs

How agents should consume domain documentation in **kp-agent-package**, and how that relates to a **repositori laporan** setelah pemasangan.

Repositori paket: https://github.com/Fahriza253/kp-agent-package (`Fahriza253/kp-agent-package` untuk `npx skills add`).

## Dua lingkungan kerja

| Lingkungan | Cakupan | Mulai dari |
| ---------- | ------- | ---------- |
| **Repo ini (paket penerbit)** | Katalog skill, rules, dokumentasi agen | `skills/`, `GLOSSARY.md`, `docs/adr/` |
| **Repo laporan (workspace pengguna)** | Menulis, merevisi, mengaudit naskah KP | `.agents/skills/kp-intent-router/`, `.cursor/rules/kp-00-core.mdc`, `docs/agents/progress-laporan.md` |

Path naskah (`laporan/`, `siakad/`, `revisi/`) hanya ada di repo laporan pengguna, bukan di clone paket ini.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root.
- **`docs/agents/panduan-penggunaan-skills.md`**: contoh penggunaan lengkap skill di repo laporan.
- **`docs/adr/`**, terutama ADR-0002 untuk layout instalasi.
- **`skills/kp/references/workspace-document-contract.md`**: kontrak path repo laporan.
- **`.cursor/rules/kp-00-core.mdc`**: tabel path dan konfirmasi untuk kerja KP (disalin ke repo laporan).

## File structure (single-context)

```
/
├── skills/
│   ├── academic/<nama>/SKILL.md    Katalog reusable (dipublish)
│   └── kp/<nama>/SKILL.md          Katalog KP (dipublish)
├── .agents/skills/<nama>/          Skill terpasang (dogfooding + engineering)
├── .cursor/rules/*.mdc             Rules KP (salin ke workspace pengguna)
├── GLOSSARY.md
├── docs/adr/
├── docs/agents/
├── .scratch/
└── skills-lock.json
```

## Routing tugas

1. **Memelihara paket**: skill engineering di `.agents/skills/`; isu di `.scratch/`.
2. **Mengedit skill KP**: ubah di `skills/kp/` atau `skills/academic/`, lalu selaraskan `.agents/skills/<nama>/`.
3. **Menulis laporan (di repo pengguna)**: `kp-intent-router`, rules KP, hierarki di `kp-00-core.mdc`.

## Flag ADR conflicts

Jika keluaran Anda bertentangan dengan ADR, nyatakan eksplisit (misalnya ADR-0002 untuk layout `skills/`).
