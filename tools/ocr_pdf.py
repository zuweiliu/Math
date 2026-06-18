#!/usr/bin/env python3
"""
ocr_pdf.py — extract text from a scanned (image-only) PDF using OCR.

Many of the camp source PDFs are scanned images with NO embedded text layer, so
`pdftotext` / Spotlight return nothing. This script rasterizes every page with
PyMuPDF and runs Tesseract OCR on each page, printing (or saving) the text.

Requirements (already set up on this machine):
  - Python package:  pymupdf            (pip install pymupdf)
  - CLI tool:        tesseract          (brew install tesseract)

Usage:
  python3 tools/ocr_pdf.py "AMC10 Factiorization.pdf"
  python3 tools/ocr_pdf.py "path/to/source.pdf" --out notes.txt
  python3 tools/ocr_pdf.py "path/to/source.pdf" --dpi 400 --psm 6

The default DPI (300) and Tesseract page-seg mode (6 = "assume a uniform block
of text") work well for these worksheet-style pages.
"""
from __future__ import annotations
import argparse
import os
import subprocess
import sys
import tempfile


def ocr_pdf(pdf_path: str, dpi: int = 300, psm: int = 6) -> str:
    try:
        import pymupdf  # noqa
    except ImportError:
        sys.exit("Missing dependency: pip install pymupdf")

    if not _have("tesseract"):
        sys.exit("Missing tool: brew install tesseract")

    doc = pymupdf.open(pdf_path)
    chunks: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, page in enumerate(doc):
            png = os.path.join(tmp, f"page_{i + 1:02d}.png")
            page.get_pixmap(dpi=dpi).save(png)
            text = subprocess.run(
                ["tesseract", png, "stdout", "--psm", str(psm)],
                capture_output=True, text=True,
            ).stdout
            chunks.append(f"===== page {i + 1:02d} =====\n{text.strip()}\n")
    return "\n".join(chunks)


def _have(cmd: str) -> bool:
    from shutil import which
    return which(cmd) is not None


def main() -> None:
    ap = argparse.ArgumentParser(description="OCR a scanned PDF to text.")
    ap.add_argument("pdf", help="path to the source PDF")
    ap.add_argument("--out", help="write text here instead of stdout")
    ap.add_argument("--dpi", type=int, default=300, help="raster DPI (default 300)")
    ap.add_argument("--psm", type=int, default=6, help="Tesseract page-seg mode (default 6)")
    args = ap.parse_args()

    text = ocr_pdf(args.pdf, dpi=args.dpi, psm=args.psm)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✓ wrote {args.out} ({len(text)} chars)")
    else:
        print(text)


if __name__ == "__main__":
    main()
