# ADR-0003: Kontrak dokumen workspace laporan

## Status

Accepted (2026-11-09)

## Context

Skill KP (`kp-draft-section`, `kp-docx-sync`, `kp-audit`, rules di `kp-00`) merujuk puluhan path di repo laporan. Sebagian dibuat scaffold, sebagian manual (pedoman, DOCX). `verify-layout.sh` awalnya tidak mengecek semua rujukan `kp-00`, sehingga router bisa jalan dengan layout setengah lengkap.

## Decision

1. Satu peta dependensi: `skills/kp/references/workspace-document-contract.md`.
2. Scaffold menambah stub `GLOSSARY.md` dan `AGENTS.md` di akar repo laporan.
3. `verify-layout.sh` memeriksa kontrak minimum otomatis; pedoman dan DOCX hanya peringatan.
4. `kp-intent-router` mengarahkan ke setup bila kontrak belum terpenuhi.

## Consequences

- Maintainer memperbarui kontrak saat skill atau `kp-00` menambah path baru.
- Duplikat template di `docs/agents/templates/` tidak dipakai untuk scaffold; kanonik tetap di `setup-kp-scaffold/assets/templates/`.
