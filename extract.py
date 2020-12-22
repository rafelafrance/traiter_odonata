#!/usr/bin/env python3
"""Extract Odonata traits from scientific literature."""

import re
import argparse
import textwrap
from copy import deepcopy

from src.matchers.pipeline import Pipeline
from src.writers.html_writer import html_writer


def main(args):
    """Perform actions based on the arguments."""
    pipeline = Pipeline()

    filter_lines = re.compile(r'(\d+|Description)')
    lines = args.input.readlines()
    lines = [ln for ln in lines if filter_lines.match(ln)]
    lines = [' '.join(ln.split()) for ln in lines]

    rows = []
    for doc in pipeline.nlp.pipe(lines[:2]):
        rows.append({
            'doc': doc,
            'traits': pipeline.trait_list(doc),
        })

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
    main(ARGS)
