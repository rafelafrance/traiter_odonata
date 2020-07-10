#!/usr/bin/env python3

"""Extract odonata traits from scientific literature (PDFs to text)."""

from pathlib import Path

from pdfminer.high_level import extract_text

from odonata.pylib.segmenter import clean_pdf

PDF_DIR = Path('.') / 'data' / 'pdf'
TXT_DIR = Path('.') / 'data' / 'txt'

DOCS = ['The_Dragonflies_and_Damselflies_of_Nebraska.pdf']


def main():
    """Extract data from the PDFs."""
    for path in DOCS:
        path = str(PDF_DIR / path)
        text = extract_text(path)
        text = clean_pdf(text)
        print(text)


if __name__ == '__main__':
    main()
