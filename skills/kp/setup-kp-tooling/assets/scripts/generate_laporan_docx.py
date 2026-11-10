#!/usr/bin/env python3
"""Buat naskah DOCX baru dari Markdown kerja laporan KP.

Naskah Word resmi dipakai sebagai template gaya: margin, font, heading
bernomor otomatis, daftar bernomor, dan gaya daftar pustaka ikut terbawa.
Isi naskah diambil dari `laporan/ARCHIVE/DRAFT_KP.md`.

Hasil selalu berupa berkas baru. Berkas template dan berkas output yang
sudah ada tidak pernah ditimpa. Gambar pada Markdown disisipkan bila
berkasnya ada (registri `laporan/assets/images/manifest.json` atau path
relatif yang dapat di-resolve). Bila berkas tidak ditemukan, diganti
catatan yang disorot kuning agar mudah dicari.

Ekstraksi gambar dari naskah Word resmi:
    .venv/bin/python scripts/extract_laporan_docx_images.py

Dependensi: lihat `scripts/requirements-docx.txt`.

Setup venv lokal (dari akar repositori):
    python3 -m venv .venv
    .venv/bin/pip install -r scripts/requirements-docx.txt

Contoh:
    .venv/bin/python scripts/generate_laporan_docx.py
    .venv/bin/python scripts/generate_laporan_docx.py --out "/tmp/naskah-uji.docx"
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX, WD_LINE_SPACING
from docx.styles.style import BaseStyle
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor, Twips
from docx.text.paragraph import Paragraph as DocxParagraph
from docx.text.run import Run

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from laporan_image_assets import (  # noqa: E402
    DEFAULT_ASSETS_DIR,
    ImageAssetEntry,
    build_src_lookup,
    load_manifest,
    manifest_path,
    resolve_image_path,
)

PROJECT_ROOT = SCRIPTS_DIR.parent
DEFAULT_SOURCE = PROJECT_ROOT / "laporan" / "ARCHIVE" / "DRAFT_KP.md"
DEFAULT_TEMPLATE = (
    PROJECT_ROOT
    / "laporan"
    / "DRAFT LAPORAN KP - SIAKAD FT - DAFA FAWAZ.docx"
)
DEFAULT_OUT_DIR = PROJECT_ROOT / "laporan" / "GENERATED"

BODY_FONT = "Times New Roman"
CODE_FONT = "Courier New"
BODY_SIZE = Pt(12)
LINK_COLOR = RGBColor(0x00, 0x00, 0xFF)
# Jarak vertikal dalam satu paragraf Heading 1 (nomor BAB ↔ judul).
CHAPTER_LINE_SPACING = 2.4
# Baris kosong tambahan antara nomor BAB (Word) dan teks judul (satu paragraf).
CHAPTER_BLANK_LINE_BEFORE_TITLE = False

STYLE_CHAPTER = "Heading 1"
STYLE_UNNUMBERED = "Heading Tanpa Nomor"
STYLE_LIST = "List Paragraph"
NUMBERED_HEADING_STYLES = {2: "Heading 2", 3: "Heading 3", 4: "Heading 4"}
BIBLIOGRAPHY_TITLE = "DAFTAR PUSTAKA"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ORDERED_RE = re.compile(r"^(\d+)\.\s+(.+)$")
IMAGE_RE = re.compile(r"^!\[([^\]]*)\]\(([^)\s]+)\)$")
CHAPTER_RE = re.compile(r"^BAB\s+[IVXLC]+$")
# Word numbers headings automatically, so typed numbers are removed.
NUMBER_PREFIX_RE = re.compile(r"^\d+(?:\.\d+)*\.?\s+")
UNSUPPORTED_PREFIXES = ("|", "```", ">")

INLINE_RE = re.compile(
    r"(?P<link>\[(?P<link_text>[^\]]+)\]\((?P<link_url>[^)\s]+)\))"
    r"|(?P<auto><(?P<auto_url>https?://[^>\s]+)>)"
    r"|(?P<bold>\*\*(?P<bold_text>.+?)\*\*)"
    r"|(?P<code>`(?P<code_text>[^`]+)`)"
    r"|(?P<italic_star>\*(?P<italic_star_text>[^*\s][^*]*?)\*)"
    r"|(?P<italic_us>(?<!\w)_(?P<italic_us_text>[^_\s][^_]*?)_(?!\w))"
)


@dataclass(frozen=True)
class Heading:
    level: int
    text: str


@dataclass(frozen=True)
class Paragraph:
    text: str


@dataclass(frozen=True)
class ListItem:
    number: int
    text: str


@dataclass(frozen=True)
class Image:
    alt: str
    src: str


Block = Heading | Paragraph | ListItem | Image


def paragraph_style_by_name(document: Document, style_name: str) -> BaseStyle:
    """Ambil gaya paragraf; template Word resmi memakai styleId numerik untuk Heading built-in."""
    for style in document.styles:
        if style.name == style_name and style.type == WD_STYLE_TYPE.PARAGRAPH:
            return style
    raise KeyError(f"no paragraph style with name {style_name!r}")


@dataclass(frozen=True)
class RunFormat:
    bold: bool = False
    italic: bool = False
    font_name: str | None = None
    size: Pt | None = None


class MarkdownParser:
    """Ubah Markdown kerja menjadi daftar blok yang sudah dikenali."""

    def __init__(self) -> None:
        self.blocks: list[Block] = []
        self.warnings: list[str] = []
        self._kind: str | None = None
        self._parts: list[str] = []
        self._number = 0

    def parse(self, text: str) -> list[Block]:
        for line_no, raw in enumerate(text.splitlines(), start=1):
            line = raw.strip()
            if not line:
                self._flush()
                continue
            if self._handle_structural_line(line, line_no):
                continue
            if self._kind is None:
                self._kind = "paragraph"
            self._parts.append(line)
        self._flush()
        return self.blocks

    def _handle_structural_line(self, line: str, line_no: int) -> bool:
        if heading := HEADING_RE.match(line):
            self._flush()
            self.blocks.append(Heading(len(heading.group(1)), heading.group(2)))
            return True
        if image := IMAGE_RE.match(line):
            self._flush()
            self.blocks.append(Image(image.group(1), image.group(2)))
            return True
        if ordered := ORDERED_RE.match(line):
            self._flush()
            self._kind = "item"
            self._number = int(ordered.group(1))
            self._parts = [ordered.group(2)]
            return True
        if line.startswith(UNSUPPORTED_PREFIXES):
            self.warnings.append(
                f"baris {line_no}: sintaks belum didukung, "
                "ditulis sebagai teks biasa"
            )
        return False

    def _flush(self) -> None:
        if self._kind == "paragraph":
            self.blocks.append(Paragraph(" ".join(self._parts)))
        elif self._kind == "item":
            self.blocks.append(ListItem(self._number, " ".join(self._parts)))
        self._kind = None
        self._parts = []


class LaporanDocxBuilder:
    """Tulis blok Markdown ke dokumen baru yang memakai gaya template."""

    def __init__(
        self,
        template: Path,
        *,
        source_md: Path,
        assets_dir: Path,
        image_entries: list[ImageAssetEntry],
    ) -> None:
        self.document = Document(str(template))
        self._clear_body()
        self._drop_media_relationships()
        self._numbering = self.document.part.numbering_part.element
        self._decimal_abstract_id = _find_decimal_abstract_id(self._numbering)
        self._source_md = source_md
        self._assets_dir = assets_dir
        self._image_lookup = build_src_lookup(image_entries)
        self.warnings: list[str] = []
        self.skipped_images: list[str] = []
        self.embedded_images: list[str] = []
        self.counts: Counter[str] = Counter()
        self._pending_chapter = False
        self._in_bibliography = False
        self._open_list_id: int | None = None
        self._paragraph_styles: dict[str, BaseStyle] = {}

    def add_blocks(self, blocks: list[Block]) -> None:
        for block in blocks:
            if not isinstance(block, ListItem):
                self._open_list_id = None
            match block:
                case Heading(level=level, text=text):
                    self._add_heading(level, text)
                case Paragraph(text=text):
                    self._add_paragraph(text)
                case ListItem(number=number, text=text):
                    self._add_list_item(number, text)
                case Image(alt=alt, src=src):
                    self._add_image(alt, src)

    def finish(self) -> None:
        self._close_pending_chapter()

    def save(self, target: Path) -> None:
        self.document.save(str(target))

    def _clear_body(self) -> None:
        body = self.document.element.body
        for child in list(body):
            if child.tag != qn("w:sectPr"):
                body.remove(child)

    def _drop_media_relationships(self) -> None:
        # The template embeds a Visio drawing and an EMF image that belong
        # to the old figures. Dropping them keeps the new file small.
        media_types = {RT.IMAGE, RT.PACKAGE, RT.OLE_OBJECT}
        part = self.document.part
        for rel_id, rel in list(part.rels.items()):
            if rel.reltype in media_types:
                part.drop_rel(rel_id)

    def _new_paragraph(self, style_name: str | None = None) -> DocxParagraph:
        paragraph = self.document.add_paragraph()
        if style_name is not None:
            paragraph.style = self._get_paragraph_style(style_name)
        return paragraph

    def _get_paragraph_style(self, style_name: str) -> BaseStyle:
        if style_name not in self._paragraph_styles:
            self._paragraph_styles[style_name] = paragraph_style_by_name(
                self.document, style_name
            )
        return self._paragraph_styles[style_name]

    def _add_heading(self, level: int, text: str) -> None:
        if level == 1 and CHAPTER_RE.match(text):
            self._close_pending_chapter()
            self._pending_chapter = True
            self._in_bibliography = False
            return

        self._close_pending_chapter()
        self._in_bibliography = text == BIBLIOGRAPHY_TITLE
        if level == 1 or self._in_bibliography:
            paragraph = self._new_paragraph(STYLE_UNNUMBERED)
            self._add_inline(paragraph, text, RunFormat())
        else:
            style_name = NUMBERED_HEADING_STYLES[min(level, 4)]
            if level > 4:
                self.warnings.append(
                    f"heading level {level} dipetakan ke Heading 4: {text}"
                )
            paragraph = self._new_paragraph(style_name)
            self._add_inline(
                paragraph, NUMBER_PREFIX_RE.sub("", text, count=1), RunFormat()
            )
        self.counts[f"heading{min(level, 4)}"] += 1

    def _add_paragraph(self, text: str) -> None:
        if self._pending_chapter:
            self._pending_chapter = False
            self._write_chapter(text)
            return
        if text == BIBLIOGRAPHY_TITLE:
            # Written as a plain line in the Markdown draft.
            self._add_heading(1, text)
            return

        paragraph = self.document.add_paragraph()
        if self._in_bibliography:
            self._format_reference(paragraph)
            self.counts["reference"] += 1
        else:
            self.counts["paragraph"] += 1
        self._add_inline(paragraph, text, RunFormat())

    def _add_list_item(self, number: int, text: str) -> None:
        if self._open_list_id is None:
            self._open_list_id = self._create_list(start=number)

        paragraph = self._new_paragraph(STYLE_LIST)
        num_pr = paragraph._p.get_or_add_pPr().get_or_add_numPr()
        num_pr.get_or_add_ilvl().val = 0
        num_pr.get_or_add_numId().val = self._open_list_id
        paragraph.paragraph_format.line_spacing = 2.0
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        self._add_inline(
            paragraph, text, RunFormat(font_name=BODY_FONT, size=BODY_SIZE)
        )
        self.counts["list_item"] += 1

    def _add_image(self, alt: str, src: str) -> None:
        self._close_pending_chapter()
        resolved = resolve_image_path(
            src,
            project_root=PROJECT_ROOT,
            source_md=self._source_md,
            assets_dir=self._assets_dir,
            lookup=self._image_lookup,
        )
        if resolved is None:
            self._add_image_note(alt, src)
            return

        entry = self._image_lookup.get(src.replace("\\", "/"))
        if entry is None:
            entry = self._image_lookup.get(src)
        if entry is None:
            entry = self._image_lookup.get(resolved.name)

        paragraph = self.document.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.paragraph_format.first_line_indent = Twips(0)
        run = paragraph.add_run()
        width = entry.width_inches if entry and entry.width_inches else None
        if width:
            run.add_picture(str(resolved), width=Inches(width))
        else:
            run.add_picture(str(resolved))

        caption = (alt or (entry.caption if entry else "")).strip()
        if caption:
            caption_paragraph = self.document.add_paragraph()
            caption_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            caption_paragraph.paragraph_format.first_line_indent = Twips(0)
            caption_run = caption_paragraph.add_run(caption)
            caption_run.font.name = BODY_FONT
            caption_run.font.size = BODY_SIZE

        self.embedded_images.append(str(resolved))
        self.counts["image"] += 1

    def _add_image_note(self, alt: str, src: str) -> None:
        self._close_pending_chapter()
        self.skipped_images.append(src)
        paragraph = self.document.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.paragraph_format.first_line_indent = Twips(0)
        run = paragraph.add_run(
            f"[Gambar dilewati: {alt or 'tanpa judul'}. "
            f"Sisipkan gambar secara manual pada posisi ini. Sumber: {src}]"
        )
        run.italic = True
        run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        self.counts["image_note"] += 1

    def _close_pending_chapter(self) -> None:
        if self._pending_chapter:
            self.warnings.append("BAB tanpa judul di baris berikutnya")
            self._pending_chapter = False
            self._write_chapter("")

    def _write_chapter(self, title: str) -> None:
        """Satu paragraf Heading 1: baris 1 nomor BAB (Word), baris 2 judul (`w:br`)."""
        paragraph = self._new_paragraph(STYLE_CHAPTER)
        self._format_chapter_paragraph(paragraph)
        run = paragraph.add_run()
        run.add_break()
        if CHAPTER_BLANK_LINE_BEFORE_TITLE:
            run.add_break()
        if title:
            _append_run_text_preserve_space(run, title)
        self.counts["heading1"] += 1

    @staticmethod
    def _format_chapter_paragraph(paragraph: DocxParagraph) -> None:
        # Perataan mengikuti gaya Heading 1 (tengah); hanya jarak antarbaris disetel.
        fmt = paragraph.paragraph_format
        fmt.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
        fmt.line_spacing = CHAPTER_LINE_SPACING

    @staticmethod
    def _format_reference(paragraph: DocxParagraph) -> None:
        fmt = paragraph.paragraph_format
        fmt.space_before = Pt(6)
        fmt.space_after = Pt(6)
        fmt.line_spacing = 1.0
        fmt.left_indent = Twips(567)
        fmt.first_line_indent = -Twips(567)
        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    def _create_list(self, start: int) -> int:
        num = self._numbering.add_num(self._decimal_abstract_id)
        override = num.add_lvlOverride(ilvl=0)
        override.add_startOverride(start)
        self.counts["list"] += 1
        return num.numId

    def _add_inline(
        self, paragraph: DocxParagraph, text: str, fmt: RunFormat
    ) -> None:
        position = 0
        for match in INLINE_RE.finditer(text):
            if match.start() > position:
                self._add_run(paragraph, text[position : match.start()], fmt)
            if match.group("link"):
                self._add_hyperlink(
                    paragraph, match.group("link_url"), match.group("link_text")
                )
            elif match.group("auto"):
                url = match.group("auto_url")
                self._add_hyperlink(paragraph, url, url)
            elif match.group("bold"):
                bold_fmt = RunFormat(True, fmt.italic, fmt.font_name, fmt.size)
                self._add_inline(paragraph, match.group("bold_text"), bold_fmt)
            elif match.group("code"):
                code_fmt = RunFormat(fmt.bold, fmt.italic, CODE_FONT, fmt.size)
                self._add_run(paragraph, match.group("code_text"), code_fmt)
            else:
                inner = match.group("italic_star_text") or match.group(
                    "italic_us_text"
                )
                italic_fmt = RunFormat(fmt.bold, True, fmt.font_name, fmt.size)
                self._add_inline(paragraph, inner, italic_fmt)
            position = match.end()
        if position < len(text):
            self._add_run(paragraph, text[position:], fmt)

    @staticmethod
    def _add_run(paragraph: DocxParagraph, text: str, fmt: RunFormat) -> None:
        if not text:
            return
        run = paragraph.add_run(text)
        _apply_format(run, fmt)

    def _add_hyperlink(
        self, paragraph: DocxParagraph, url: str, text: str
    ) -> None:
        rel_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
        hyperlink = OxmlElement("w:hyperlink")
        hyperlink.set(qn("r:id"), rel_id)
        run_element = OxmlElement("w:r")
        hyperlink.append(run_element)
        run = Run(run_element, paragraph)
        run.text = text
        run.font.color.rgb = LINK_COLOR
        run.font.underline = True
        run.font.size = BODY_SIZE
        run.font.name = BODY_FONT
        paragraph._p.append(hyperlink)


def _append_run_text_preserve_space(run: Run, text: str) -> None:
    """Tambah teks ke run yang sudah berisi `w:br` (jangan pakai `run.text`, menghapus break)."""
    run.add_text(text)
    for text_el in run._r.findall(qn("w:t")):
        if text_el.text:
            text_el.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def _apply_format(run: Run, fmt: RunFormat) -> None:
    if fmt.bold:
        run.bold = True
    if fmt.italic:
        run.italic = True
    if fmt.font_name:
        run.font.name = fmt.font_name
    if fmt.size:
        run.font.size = fmt.size


def _find_decimal_abstract_id(numbering) -> int:
    """Cari definisi daftar 1., 2., 3. yang tidak terikat ke heading."""
    for abstract in numbering.findall(qn("w:abstractNum")):
        level = _find_level_zero(abstract)
        if level is None or level.find(qn("w:pStyle")) is not None:
            continue
        num_fmt = level.find(qn("w:numFmt"))
        lvl_text = level.find(qn("w:lvlText"))
        if num_fmt is None or lvl_text is None:
            continue
        if num_fmt.get(qn("w:val")) == "decimal" and lvl_text.get(qn("w:val")) == "%1.":
            return int(abstract.get(qn("w:abstractNumId")))
    raise RuntimeError("Template tidak memiliki definisi daftar 1., 2., dst.")


def _find_level_zero(abstract):
    for level in abstract.findall(qn("w:lvl")):
        if level.get(qn("w:ilvl")) == "0":
            return level
    return None


def resolve_output_path(out: Path | None, out_dir: Path, template: Path) -> Path:
    """Pilih lokasi output baru. Berkas yang sudah ada tidak pernah ditimpa."""
    if out is not None:
        target = out
        if target.suffix.lower() != ".docx":
            raise SystemExit("Output harus berakhiran .docx")
        if target.exists():
            raise SystemExit(
                f"Output sudah ada, pilih nama lain agar tidak menimpa: {target}"
            )
    else:
        out_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        base = f"DRAFT LAPORAN KP - SIAKAD FT - DAFA FAWAZ - generated {stamp}"
        target = out_dir / f"{base}.docx"
        counter = 2
        while target.exists():
            target = out_dir / f"{base} ({counter}).docx"
            counter += 1

    if target.resolve() == template.resolve():
        raise SystemExit("Output tidak boleh sama dengan naskah Word resmi")
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument(
        "--assets-dir",
        type=Path,
        default=PROJECT_ROOT / DEFAULT_ASSETS_DIR,
        help="Folder aset gambar dan manifest.json.",
    )
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument(
        "--out", type=Path, default=None,
        help="Path file output (.docx). Harus belum ada.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.source.is_file():
        raise SystemExit(f"Markdown sumber tidak ditemukan: {args.source}")
    if not args.template.is_file():
        raise SystemExit(f"Template DOCX tidak ditemukan: {args.template}")

    markdown = MarkdownParser()
    blocks = markdown.parse(args.source.read_text(encoding="utf-8"))

    manifest = manifest_path(args.assets_dir)
    image_entries = load_manifest(manifest) if manifest.is_file() else []

    builder = LaporanDocxBuilder(
        args.template,
        source_md=args.source,
        assets_dir=args.assets_dir,
        image_entries=image_entries,
    )
    builder.add_blocks(blocks)
    builder.finish()

    output = resolve_output_path(args.out, args.out_dir, args.template)
    builder.save(output)

    warnings = markdown.warnings + builder.warnings
    print(f"Sumber   : {args.source}")
    print(f"Template : {args.template}")
    print(f"Output   : {output}")
    print("Ringkasan:")
    for key in sorted(builder.counts):
        print(f"  {key:<12} {builder.counts[key]}")
    if builder.embedded_images:
        print(f"Gambar disisipkan ({len(builder.embedded_images)}):")
        for path in builder.embedded_images:
            print(f"  - {path}")
    if builder.skipped_images:
        print(f"Gambar dilewati ({len(builder.skipped_images)}):")
        for src in builder.skipped_images:
            print(f"  - {src}")
    for message in warnings:
        print(f"PERINGATAN: {message}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
