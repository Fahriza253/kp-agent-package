#!/usr/bin/env python3
"""Pemeriksaan mekanis Markdown proyek laporan KP (tanpa em dash U+2014)."""

from __future__ import annotations

import sys
from pathlib import Path

EM_DASH = "\u2014"
EXCLUDE_PARTS = ("laporan/archive",)


def should_scan(path: Path, root: Path) -> bool:
    try:
        rel = path.relative_to(root).as_posix().lower()
    except ValueError:
        return False
    if path.suffix.lower() != ".md":
        return False
    for part in EXCLUDE_PARTS:
        if part in rel:
            return False
    return True


def main() -> int:
    root = Path(".").resolve()
    violations: list[tuple[Path, int, str]] = []
    for path in sorted(root.rglob("*.md")):
        if not should_scan(path, root):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"SKIP {path}: {exc}", file=sys.stderr)
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            if EM_DASH in line:
                violations.append((path, lineno, line.strip()))

    if violations:
        print("Em dash (U+2014) ditemukan:", file=sys.stderr)
        for path, lineno, line in violations:
            print(f"  {path}:{lineno}: {line[:120]}", file=sys.stderr)
        return 1

    print("OK: tidak ada em dash pada Markdown yang diperiksa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
