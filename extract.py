#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import argparse
import textwrap

from src.matchers.rule_matcher import FRASER_MATCHERS, PAULSON_MATCHERS
from src.matchers.pipeline import Pipeline
from src.readers.fraser_reader import fraser_1933
from src.readers.paulson_reader import paulson_2011

GUIDES = {
    'fraser': {
        'reader': fraser_1933,
        'matchers_fraser': FRASER_MATCHERS,
    },
    'paulson': {
        'reader': paulson_2011,
        'matchers_fraser': PAULSON_MATCHERS,
    },
}


def main(args):
    """Perform actions based on the arguments."""
    guide = GUIDES[args.guide]
    reader = guide['reader']
    matchers = guide['matchers_fraser']

    pipeline = Pipeline(matchers)

    paras = reader()
    for i, doc in enumerate(pipeline.nlp.pipe(paras)):
        print('=' * 80)
        print(doc)
        for sent in doc.sents:
            print('-' * 80)
            print(sent)
            for ent in sent.ents:
                print(f'{ent.text:<16} {ent._.data}')
            print()
        if i > 0:
            break


def parse_args():
    """Process command-line arguments."""
    description = """Parse data from dragonfly guides."""
    arg_parser = argparse.ArgumentParser(
        description=textwrap.dedent(description),
        fromfile_prefix_chars='@')

    guides = list(GUIDES.keys())
    arg_parser.add_argument(
        '--guide', '-g', choices=guides, default=guides[0],
        help="""Which guide to parse.""")

    args = arg_parser.parse_args()
    return args


if __name__ == '__main__':
    ARGS = parse_args()
    main(ARGS)
