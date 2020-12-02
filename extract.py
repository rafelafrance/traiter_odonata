#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import argparse
import textwrap

from spacy import displacy
from tqdm import tqdm

from src.matchers.matcher import FRASER_MATCHERS, PAULSON_MATCHERS
from src.matchers.pipeline import Pipeline
from src.readers.fraser_reader import fraser_1933
from src.readers.paulson_reader import paulson_2011

GUIDES = {
    'fraser': {
        'reader': fraser_1933,
        'matchers': FRASER_MATCHERS,
    },
    'paulson': {
        'reader': paulson_2011,
        'matchers': PAULSON_MATCHERS,
    },
}

OPTIONS = {
    'colors': {
        'VERNACULAR': '#a6cee388',
        'SCI_NAME': '#1f78b488',
        'TOTAL_LENGTH_KEY': '#b2df8a88',
        'HIND_WING_LENGTH_KEY': '#33a02c88',
        'COLOR_PAT': '#fb9a9988',
        'RANGE': '#e31a1c88',
        'HEADING': '#fdbf6f88',
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
    guide = GUIDES[args.guide]
    reader = guide['reader']
    matchers = guide['matchers']

    pipeline = Pipeline(matchers)

    sentences = []

    paras = reader()
    for doc in tqdm(pipeline.nlp.pipe(paras)):
        if len(doc) > 1 and doc[1].ent_type_ == 'vernacular':
            sentences += list(doc.sents)
        if doc[0].text == 'Description':
            sentences += list(doc.sents)

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
