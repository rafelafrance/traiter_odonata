#!/usr/bin/env python3

"""Extract odonata traits from scientific literature (PDFs to text)."""

import traiter.pdf as pdf

from odonata.pylib.util import PDF_DIR, TXT_DIR


def main():
    """Extract data from the files."""
    pdf.pdf2txt(PDF_DIR, TXT_DIR)
    for txt in TXT_DIR.glob('*.txt'):
        with open(txt) as txt_file:
            text = txt_file.read()
            text = pdf.clean_text(text)
        break


if __name__ == '__main__':
    main()
