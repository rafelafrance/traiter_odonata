#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import argparse
import textwrap

from src.matchers.matcher import FRASER_MATCHERS, PAULSON_MATCHERS
from src.matchers.pipeline import Pipeline
from src.readers.fraser_reader import fraser_1933
from src.readers.paulson_reader import paulson_2011

KITS = {
    'fraser': {
        'reader': fraser_1933,
        'matchers': FRASER_MATCHERS,
    },
    'paulson': {
        'reader': paulson_2011,
        'matchers': PAULSON_MATCHERS,
    },
}


def main(args):
    """Perform actions based on the arguments."""
    kit = KITS[args.reader]
    reader = kit['reader']
    matchers = kit['matchers']

    pipeline = Pipeline(matchers)

    paras = reader()
    for doc in pipeline.nlp.pipe(paras):
        if len(doc) > 0:
            print(doc[0])


def parse_args():
    """Process command-line arguments."""
    description = """Parse data from dragonfly guides."""
    arg_parser = argparse.ArgumentParser(
        description=textwrap.dedent(description),
        fromfile_prefix_chars='@')

    readers = list(KITS.keys())
    arg_parser.add_argument(
        '--reader', '-r', choices=readers, default=readers[0],
        help="""Which flora to read.""")

    args = arg_parser.parse_args()
    return args


if __name__ == '__main__':
    ARGS = parse_args()
    main(ARGS)
