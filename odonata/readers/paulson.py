"""Parse a text version of the Paulson guide."""

import logging
import re

from tqdm import tqdm
from traiter.util import shorten

from odonata.patterns.sex_linker import sex_linker
from odonata.pylib.pipeline import pipeline


def paulson_reader(args):
    """Parse this guide."""
    nlp = pipeline()

    lines = read_lines(args)

    rows = []
    taxon = ''

    logging.info('Parsing records.')
    for line in tqdm(lines):
        doc = nlp(line)
        traits = [e._.data for e in doc.ents]

        # Header line
        if re.match(r'^\d+', line):
            taxon = [s for t in traits if (s := t.get('sci_name'))]
            taxon = taxon[0] if taxon else ''

        # Description line
        elif line.startswith('Description'):
            sex_linker(doc)

        if taxon and traits:
            rows.append({
                'source': args.text_file.name,
                'taxon': taxon,
                'text': line,
                'traits': traits,
            })

    return rows


def read_lines(args):
    """Read & filter lines."""
    logging.info('Reading records.')
    filter_lines = re.compile(r'(\d+|Description)')
    with open(args.text_file) as in_file:
        lines = in_file.readlines()
    lines = [shorten(ln) for ln in lines if filter_lines.match(ln)]
    return lines
