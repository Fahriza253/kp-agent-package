# ADR-0001: Pisah paket agen dan artefak pemasangan

## Status

Superseded (partial) oleh ADR-0002 untuk lokasi skill dan rules. Tetap berlaku untuk pemisahan repo paket vs repo laporan dan issue tracker lokal.

## Context

Penulisan Laporan KP membutuhkan rules dan skill Cursor yang konsisten. Beberapa skill (penulisan akademik umum) harus reusable untuk skripsi atau makalah lain. Repo pemeliharaan paket tidak selalu sama dengan repo yang menyimpan naskah, submodule SIAKAD, dan resource kampus.

## Decision

1. Simpan skill engineering Matt Pocock di `.agents/skills/` dengan pin `skills-lock.json`.
2. Simpan rules dan skill KP siap salin di `resources/.cursor/`, bukan di `.cursor/` akar repo paket, agar pemasangan ke repo laporan eksplisit (salin ke `.cursor/` target).
3. Dokumentasi agen konsumsi skill engineering (`docs/agents/*.md`, `GLOSSARY.md`, `docs/adr/`) hidup di akar repo paket.
4. Issue tracker default untuk pekerjaan paket: Markdown lokal di `.scratch/`, tanpa asumsi GitHub remote.

## Consequences

- Agen harus membedakan tugas "memelihara paket" vs "menulis laporan" (lihat `docs/agents/domain.md`).
- README dan `AGENTS.md` menjadi pintu masuk; `kp-00-core.mdc` tetap otoritatif untuk path repo laporan setelah instalasi.
- Pengguna yang ingin GitHub Issues dapat mengganti isi `docs/agents/issue-tracker.md` dan blok terkait di `AGENTS.md` tanpa mengubah skill KP.
