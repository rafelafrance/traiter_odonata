#!/usr/bin/env python3

"""Extract odonata traits from scientific literature (PDFs to text)."""

import re

import traiter.pdf as pdf
from traiter.util import FLAGS

from odonata.pylib.pipeline import parse
from odonata.pylib.util import PDF_DIR, TXT_DIR


def main():
    """Extract data from the files."""
    pdf.pdf2txt(PDF_DIR, TXT_DIR)
    for i, txt in enumerate(TXT_DIR.glob('*.txt')):
        print(txt)
        if i == 0:
            continue
        with open(txt) as txt_file:
            text = txt_file.read()
            text = pdf.clean_text(text)
            text = clean_text_more(text)
            traits = parse(text)

            # from pprint import pp
            # pp(dict(traits))
            break


def clean_text_more(text):
    """Clean peculiarities particular to these guides."""
    text = re.sub(r'(?<= [a-z] -) \s (?= [a-z])', '', text, flags=FLAGS)
    text = re.sub(r'(?<= [a-z]) \s (?= - [a-z])', '', text, flags=FLAGS)
    text = re.sub(r'(?<=[a-z]) / (?=[a-z])', 'l', text, flags=FLAGS)
    return text


if __name__ == '__main__':
    main()
