#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import re
import argparse
import textwrap

from spacy import displacy

from src.matchers.pipeline import Pipeline


OPTIONS = {
    'colors': {
        'VERNACULAR': '#a6cee388',
        'SCI_NAME': '#1f78b488',
        'TOTAL_LEN': '#b2df8a88',
        'HIND_WING_LEN': '#33a02c88',
        'COLOR_PAT': '#fb9a9988',
        'qq1': '#e31a1c88',
        'RANGE': '#fdbf6f88',
        'COLOR': '#ff7f0088',
        'BODY_PART': '#cab2d688',
        'SEX': '#b1592888',
        'SEX_DIFF': '#ffff9988',
        'BODY_PART_LOC': '#6a3d9a88',
        'qq3': '#dddddd88',
        'qq4': '#b3b3b388',
    },
}


def main(args):
    """Perform actions based on the arguments."""
    pipeline = Pipeline()

    filter_lines = re.compile(r'(\d+|Description)')
    lines = args.input.readlines()
    lines = [ln for ln in lines if filter_lines.match(ln)]
    lines = [' '.join(ln.split()) for ln in lines]

    sentences = []
    for doc in pipeline.nlp.pipe(lines[:2]):
        sentences += list(doc.sents)
        for ent in doc.ents:
            print(ent, ent._.data)
        print()

    displacy.serve(sentences, style='ent', options=OPTIONS)


def parse_args():
    """Process command-line arguments."""
    description = """Parse data from dragonfly guides."""
    arg_parser = argparse.ArgumentParser(
        description=textwrap.dedent(description),
        fromfile_prefix_chars='@')

    arg_parser.add_argument(
        '--input', '-i', type=argparse.FileType(),
        help="""Which guide in text form to parse""")

    args = arg_parser.parse_args()
    return args


if __name__ == '__main__':
    ARGS = parse_args()
    main(ARGS)
