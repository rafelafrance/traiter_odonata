#!/usr/bin/env python3
"""Extract Odonata traits from scientific literature."""

import re
import argparse
import textwrap
from copy import deepcopy

from src.pylib.pipeline import NLP
from src.writers.html_ import html_writer


def paulson_guide(args):
    """Parse Paulson's Odonate guide."""
    filter_lines = re.compile(r'(\d+|Description)')
    lines = args.input.readlines()
    lines = [ln for ln in lines if filter_lines.match(ln)]
    lines = [' '.join(ln.split()) for ln in lines]

    rows = []
    for doc in NLP.pipe(lines):
        rows.append({'doc': doc, 'traits': list(doc.ents)})

    if args.html_file:
        copied = deepcopy(rows)
        html_writer(args, copied)


def parse_args():
    """Process command-line arguments."""
    description = """Parse data from dragonfly guides."""
    arg_parser = argparse.ArgumentParser(
        description=textwrap.dedent(description), fromfile_prefix_chars='@')

    arg_parser.add_argument(
        '--input', '-i', type=argparse.FileType(),
        help="""Which guide in text form to parse""")

    arg_parser.add_argument(
        '--html-file', '-H', type=argparse.FileType('w'),
        help="""Output the results to this HTML file.""")

    args = arg_parser.parse_args()
    return args


if __name__ == '__main__':
    ARGS = parse_args()
    paulson_guide(ARGS)
