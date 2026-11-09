# Paket Agen Penulisan Laporan KP

Kosakata untuk repositori **kp-agent-package**: paket skill Cursor yang dapat di-install ke workspace pengguna. Bukan glosarium isi laporan atau domain SIAKAD (itu milik repositori laporan pengguna).

## Arsitektur paket

**Lapisan reusable**:
Skill penulisan akademik umum di `skills/academic/` (misalnya `academic-writing-core`, `academic-humanize`).
_Avoid_: skill generik (ambigu dengan skill engineering Matt Pocock)

**Lapisan KP**:
Skill khusus Laporan Kerja Praktik UNPI Cianjur di `skills/kp/` (`kp-intent-router`, `kp-draft-section`, dan sejenisnya).
_Avoid_: layer laporan, modul KP (tanpa menyebut rules)

**Katalog skill**:
Tree `skills/<kategori>/<nama>/SKILL.md` yang di-clone CLI dari repo GitHub saat `npx skills add`.
_Avoid_: artefak pemasangan, folder resources

**Rules KP**:
Berkas `.mdc` di `.cursor/rules/` repo penerbit. Pengguna memasang lewat skill `kp-install-rules` atau salin manual; tidak ikut `npx skills` otomatis.
_Avoid_: skill rules (rules bukan skill)

**Sinkronisasi katalog**:
Skrip `scripts/sync_catalog_to_agents.sh` menyalin `skills/` ke `.agents/skills/` dan memperbarui bundle rules di `kp-install-rules`.
_Avoid_: sync manual (kecuali darurat)

**Skill terpasang**:
Salinan skill di workspace pengguna setelah instalasi, biasanya `.agents/skills/<nama>/`.
_Avoid_: plugin skill (kecuali konteks marketplace Cursor)

**Skill engineering**:
Skill pihak ketiga (misalnya Matt Pocock) di-pin lewat `skills-lock.json` dan disimpan di `.agents/skills/` di repo penerbit.
_Avoid_: matt skills

## Routing dan intent

**Intent**:
Kategori tugas penulisan KP yang dipilih `kp-intent-router` (misalnya DRAFT, AUDIT, SYNC, LEARN).
_Avoid_: mode, task type (untuk tugas KP)

**Peta intent**:
Tabel di `README.md` yang memetakan intent ke skill utama KP.

## Pelacakan kerja

**Issue tracker lokal**:
Spesifikasi dan tiket di `.scratch/<feature-slug>/`. Lihat `docs/agents/issue-tracker.md`.

**Status triage**:
Pada berkas isu lokal, peran triage ditulis di baris `Status:`. Lihat `docs/agents/triage-labels.md`.

## Dokumentasi domain

**ADR**:
Keputusan arsitektur paket di `docs/adr/`, termasuk layout instalasi (ADR-0002).
_Avoid_: decision log (gunakan ADR)

**Sumber kebenaran (repo laporan)**:
Tabel path di `kp-00-core.mdc` di workspace pengguna setelah rules disalin (draf, pedoman, progress, knowledge).
_Avoid_: source of truth (gunakan istilah Indonesia di narasi laporan)
