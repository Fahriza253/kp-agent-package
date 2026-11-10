#!/usr/bin/env python3
"""Ekstrak gambar dari naskah Word resmi ke laporan/assets/images/.

Berkas PNG (atau format asli) disalin ke folder aset. Registri JSON
(`manifest.json`) diperbarui agar `generate_laporan_docx.py` dapat menyisipkan
gambar sesuai referensi `![...](...)` pada DRAFT_KP.md.

Contoh:
    .venv/bin/python scripts/extract_laporan_docx_images.py
    .venv/bin/python scripts/extract_laporan_docx_images.py --force
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from laporan_image_assets import (  # noqa: E402
    DEFAULT_ASSETS_DIR,
    ImageAssetEntry,
    MANIFEST_VERSION,
    load_manifest,
    manifest_path,
    merge_manifest_entries,
    save_manifest,
    slugify,
)

PROJECT_ROOT = SCRIPTS_DIR.parent
DEFAULT_DOCX = (
    PROJECT_ROOT
    / "laporan"
    / "DRAFT LAPORAN KP - SIAKAD FT - DAFA FAWAZ.docx"
)

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W_NS, "a": A_NS}
EMU_PER_INCH = 914400

HEADING_STYLE_LEVEL = {
    "826": 1,
    "827": 2,
    "828": 3,
    "829": 4,
    "830": 5,
    "831": 6,
}


@dataclass(frozen=True)
class DocxImage:
    media_path: str
    anchor_heading: str
    width_inches: float | None
    paragraph_index: int


def _rel_target_map(zf: zipfile.ZipFile) -> dict[str, str]:
    rels_xml = zf.read("word/_rels/document.xml.rels")
    root = ET.fromstring(rels_xml)
    mapping: dict[str, str] = {}
    for rel in root:
        rid = rel.get("Id")
        target = rel.get("Target")
        if rid and target:
            mapping[rid] = target
    return mapping


def _paragraph_style_id(paragraph: ET.Element) -> str | None:
    p_pr = paragraph.find("w:pPr", NS)
    if p_pr is None:
        return None
    p_style = p_pr.find("w:pStyle", NS)
    if p_style is None:
        return None
    return p_style.get(f"{{{W_NS}}}val")


def _paragraph_text(paragraph: ET.Element) -> str:
    parts: list[str] = []
    for node in paragraph.findall(".//w:t", NS):
        if node.text:
            parts.append(node.text)
    return "".join(parts).strip()


def _image_width_inches(paragraph: ET.Element) -> float | None:
    for extent in paragraph.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent"):
        cx = extent.get("cx")
        if cx:
            return int(cx) / EMU_PER_INCH
    return None


def find_docx_images(docx: Path) -> list[DocxImage]:
    found: list[DocxImage] = []
    with zipfile.ZipFile(docx) as zf:
        rels = _rel_target_map(zf)
        document = ET.fromstring(zf.read("word/document.xml"))
        body = document.find("w:body", NS)
        if body is None:
            return found

        heading_stack: list[tuple[int, str]] = []
        paragraphs = body.findall("w:p", NS)
        for index, paragraph in enumerate(paragraphs):
            text = _paragraph_text(paragraph)
            style_id = _paragraph_style_id(paragraph)
            if style_id in HEADING_STYLE_LEVEL and text:
                level = HEADING_STYLE_LEVEL[style_id]
                heading_stack = [(lvl, title) for lvl, title in heading_stack if lvl < level]
                heading_stack.append((level, text))

            for blip in paragraph.findall(".//a:blip", NS):
                rid = blip.get(f"{{{R_NS}}}embed")
                if not rid:
                    continue
                target = rels.get(rid)
                if not target:
                    continue
                media_path = target
                if not media_path.startswith("media/"):
                    media_path = f"media/{Path(target).name}"
                anchor = heading_stack[-1][1] if heading_stack else ""
                found.append(
                    DocxImage(
                        media_path=f"word/{media_path}",
                        anchor_heading=anchor,
                        width_inches=_image_width_inches(paragraph),
                        paragraph_index=index,
                    )
                )
    return found


def entry_from_docx_image(
    item: DocxImage,
    *,
    docx: Path,
    assets_rel: str,
) -> ImageAssetEntry:
    media_name = Path(item.media_path).name
    stem = slugify(item.anchor_heading) if item.anchor_heading else Path(media_name).stem
    file_name = f"{stem}{Path(media_name).suffix.lower()}"
    docx_rel = docx.relative_to(PROJECT_ROOT).as_posix()
    return ImageAssetEntry(
        id=stem,
        file=file_name,
        markdown_src=f"{assets_rel}/{file_name}",
        caption=item.anchor_heading,
        width_inches=item.width_inches,
        anchor_heading=item.anchor_heading,
        source_docx=docx_rel,
        source_media=item.media_path,
        notes="Diekstrak otomatis dari naskah Word resmi.",
    )


def extract_binary(zf: zipfile.ZipFile, media_path: str) -> bytes:
    return zf.read(media_path)


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--docx", type=Path, default=DEFAULT_DOCX)
    parser.add_argument(
        "--assets-dir",
        type=Path,
        default=PROJECT_ROOT / DEFAULT_ASSETS_DIR,
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Timpa berkas gambar dan gabungkan ulang entri manifest yang sama id.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.docx.is_file():
        raise SystemExit(f"DOCX tidak ditemukan: {args.docx}")

    images = find_docx_images(args.docx)
    if not images:
        print("Tidak ada gambar yang ditemukan di dokumen.")
        return 0

    args.assets_dir.mkdir(parents=True, exist_ok=True)
    assets_rel = args.assets_dir.relative_to(PROJECT_ROOT).as_posix()
    manifest = manifest_path(args.assets_dir)
    existing = load_manifest(manifest) if manifest.is_file() else []

    discovered: list[ImageAssetEntry] = []
    with zipfile.ZipFile(args.docx) as zf:
        for item in images:
            entry = entry_from_docx_image(item, docx=args.docx, assets_rel=assets_rel)
            discovered.append(entry)
            target = args.assets_dir / entry.file
            if target.exists() and not args.force:
                print(f"Lewati (sudah ada): {target.name}")
                continue
            target.write_bytes(extract_binary(zf, item.media_path))
            print(f"Ekstrak: {item.media_path} -> {target}")

    merged = merge_manifest_entries(existing, discovered, force=args.force)
    save_manifest(manifest, merged)
    print(f"Manifest ({MANIFEST_VERSION}): {manifest}")
    print(f"Entri: {len(merged)}")
    for entry in merged:
        print(f"  - {entry.id}: {entry.markdown_src}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
