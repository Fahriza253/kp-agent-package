#!/usr/bin/env python3
"""Generator DOCX minimal dari DRAFT_KP.md. Ganti atau perluas dari repo referensi bila perlu."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print(
        "python-docx belum terpasang. Jalankan: pip install -r scripts/requirements-docx.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)

DEFAULT_SOURCE = Path("laporan/ARCHIVE/DRAFT_KP.md")
DEFAULT_OUT_DIR = Path("laporan/GENERATED")
OFFICIAL_DOCX_MARKER = "DRAFT LAPORAN KP"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate DOCX dari Markdown kerja KP.")
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"Berkas Markdown sumber (default: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Berkas DOCX keluaran. Default: laporan/GENERATED/naskah-YYYYMMDD-HHMM.docx",
    )
    return parser.parse_args()


def reject_official_out(path: Path) -> None:
    resolved = path.resolve()
    name = resolved.name
    if OFFICIAL_DOCX_MARKER in name and resolved.parent.name == "laporan":
        print(
            f"Menolak --out ke naskah resmi: {path}. Gunakan laporan/GENERATED/ atau /tmp.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if path.exists():
        print(f"Menolak menimpa berkas yang sudah ada: {path}", file=sys.stderr)
        raise SystemExit(1)


def default_out() -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    return DEFAULT_OUT_DIR / f"naskah-{stamp}.docx"


def add_line(doc: Document, line: str) -> None:
    if line.startswith("# "):
        doc.add_heading(line[2:].strip(), level=1)
    elif line.startswith("## "):
        doc.add_heading(line[3:].strip(), level=2)
    elif line.startswith("### "):
        doc.add_heading(line[4:].strip(), level=3)
    elif line.startswith("#### "):
        doc.add_heading(line[5:].strip(), level=4)
    elif line.strip().startswith("|") and "|" in line.strip()[1:]:
        doc.add_paragraph(f"[Tabel: perlu disisip manual di Word] {line.strip()}")
    elif line.strip().startswith("!["):
        doc.add_paragraph("[Gambar: sisip manual di Word menggantikan catatan ini]")
    elif line.strip():
        doc.add_paragraph(line)


def markdown_to_docx(source: Path, out: Path) -> None:
    text = source.read_text(encoding="utf-8")
    doc = Document()
    in_fence = False
    for raw in text.splitlines():
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            if in_fence:
                doc.add_paragraph("[Blok kode: salin manual bila diperlukan]")
            continue
        if in_fence:
            doc.add_paragraph(raw, style="Intense Quote")
            continue
        add_line(doc, raw)
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)


def main() -> int:
    args = parse_args()
    source = args.source
    if not source.is_file():
        print(f"Sumber tidak ditemukan: {source}", file=sys.stderr)
        return 1
    out = args.out if args.out else default_out()
    reject_official_out(out)
    markdown_to_docx(source, out)
    print(f"DOCX ditulis: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
