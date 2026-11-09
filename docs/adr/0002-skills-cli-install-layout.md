# ADR-0002: Katalog `skills/` dan instalasi lewat Skills CLI

## Status

Accepted (2026-11-09). Menggantikan keputusan poin 2–4 ADR-0001 tentang `resources/.cursor/` dan salin manual.

## Context

Pengguna memasang paket ke workspace laporan mereka sendiri. Cursor memuat skill dari `.agents/skills/` (dan `.cursor/skills/`). CLI `npx skills add … -a cursor` menulis ke `.agents/skills/`. Rules (`.mdc`) tidak ikut dalam instalasi skill; mereka tetap di `.cursor/rules/`.

## Decision

1. **Sumber skill yang dipublish**: `skills/academic/<nama>/` dan `skills/kp/<nama>/`, masing-masing berisi `SKILL.md` (plus `scripts/` atau `references/` bila perlu).
2. **Dogfooding di repo penerbit**: salinan skill KP dan akademik juga ada di `.agents/skills/<nama>/`, sejajar dengan skill engineering pihak ketiga.
3. **Rules KP**: kanonik di `.cursor/rules/` di repo penerbit; workspace pengguna menyalin atau menggabungkan folder itu ke repo laporan (instruksi di README).
4. **`resources/.cursor/`**: dihapus; tidak dipakai lagi sebagai staging.
5. **Rules untuk pengguna**: skill `kp-install-rules` membawa `assets/rules/` dan skrip `install-rules.sh`; rules kanonik tetap di `.cursor/rules/` repo penerbit.
6. **Sinkronisasi maintainer**: `scripts/sync_catalog_to_agents.sh` (atau `npm run sync:skills`).

## Consequences

- README dan AGENTS.md menjelaskan `npx skills add` untuk skill dan `kp-install-rules` untuk rules.
- Maintainer mengedit `skills/` dan `.cursor/rules/`, lalu menjalankan skrip sync.
- ADR-0001 tetap berlaku untuk pemisahan repo paket vs repo laporan dan issue tracker lokal.
