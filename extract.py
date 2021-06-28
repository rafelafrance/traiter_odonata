#!/usr/bin/env python3
"""Extract Odonata traits from scientific literature."""

import argparse
import textwrap
from pathlib import Path

from odonata.pylib.log import finished, started
from odonata.readers.paulson import paulson_reader
from odonata.writers.html_ import html_writer
from odonata.writers.sqlite3_db import sqlite3_db

GUIDE = {
    'paulson': paulson_reader,
}


def parse_guide(args):
    """Parse Paulson's Odonate guide."""
    rows = GUIDE[args.guide](args)

    if args.html_file:
        html_writer(args, rows)

    if args.db:
        sqlite3_db(args, rows)


def parse_args():
    """Process command-line arguments."""
    description = """Parse data from dragonfly guides."""
    arg_parser = argparse.ArgumentParser(
        description=textwrap.dedent(description), fromfile_prefix_chars='@')

    arg_parser.add_argument(
        '--text-file', '-t', type=Path,
        help="""The text version of the guide to extract.""")

    guides = list(GUIDE.keys())
    arg_parser.add_argument(
        '--guide', '-g', choices=[guides], default=guides[0],
        help="""The guide format. """)

    arg_parser.add_argument(
        '--html-file', '-H', type=Path,
        help="""Output the results to this HTML file.""")

    arg_parser.add_argument(
        '--db', '-D', type=Path,
        help="""Output to this sqlite3 database.""")

    arg_parser.add_argument(
        '--clear-db', action='store_true',
        help="""Clear the duck_db before writing to it.""")

    arg_parser.add_argument(
        '--limit', type=int,
        help="""Limit the input records. Typically used for debugging.""")

    args = arg_parser.parse_args()
    return args


if __name__ == '__main__':
    started()
    ARGS = parse_args()
    parse_guide(ARGS)
    finished()
