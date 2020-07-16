#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import re

import pandas as pd
import traiter.pdf as pdf
from traiter.util import FLAGS

from src.pylib.pipeline import parse
from src.pylib.util import PDF_DIR, TXT_DIR


def main():
    """Extract data from the files."""
    pdf.pdf2txt(PDF_DIR, TXT_DIR)
    for i, txt in enumerate(TXT_DIR.glob('*.txt')):
        print(txt)
        if i < 3:
            continue
        with open(txt) as txt_file:
            text = txt_file.read()
            text = pdf.clean_text(text)
            text = clean_text_more(text)
            traits = parse(text)

            df = pd.DataFrame(traits['description'])
            df.to_csv(str(txt) + '.csv', index=False)

            # from pprint import pp
            # pp(dict(traits))
            # pp(sents)
            break


def clean_text_more(text):
    """Clean peculiarities particular to these guides."""
    text = re.sub(r'(?<= [a-z] -) \s (?= [a-z])', '', text, flags=FLAGS)
    text = re.sub(r'(?<= [a-z]) \s (?= - [a-z])', '', text, flags=FLAGS)
    text = re.sub(r'(?<=[a-z]) / (?=[a-z])', 'l', text, flags=FLAGS)
    return text


if __name__ == '__main__':
    main()
