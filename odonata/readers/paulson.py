"""Parse a text version of the Paulson guide."""

import logging
import re

from tqdm import tqdm
from traiter.util import shorten

from odonata.patterns.sex_life_stage_linker import sex_life_stage_linker
from odonata.pylib.const import KEEP
from odonata.pylib.pipeline import pipeline


def paulson_reader(args):
    """Parse this guide."""
    nlp = pipeline()

    lines = read_lines(args)

    if hasattr(args, 'limit') and args.limit:
        lines = lines[:args.limit]
    rows = []
    taxon = ''

    logging.info('Parsing records.')
    for line in tqdm(lines):
        doc = nlp(line)

        # Header line
        if re.match(r'^(\uFEFF)?\d+', line):
            taxon = [s for e in doc.ents if (s := e._.data.get('sci_name'))]
            taxon = taxon[0] if taxon else ''

        # Description line
        elif line.startswith('Description'):
            sex_life_stage_linker(doc)

        traits = [e._.data for e in filter_ents(doc)]
        if taxon and traits:
            rows.append({
                'guide': args.text_file.stem,
                'taxon': taxon,
                'text': line,
                'traits': traits,
            })

    return rows


def filter_ents(doc):
    """Remove duplicate entities."""
    dupes = {(link.start_char, link.end_char) for e in doc.ents for link in e._.links}
    old_ents = [e for e in doc.ents if (e.start_char, e.end_char) not in dupes]
    new_ents = []
    for ent in old_ents:
        if ent.label_ not in KEEP:
            continue
        if ent.label_ == 'color_like' and not ent._.data.get('body_part'):
            continue
        new_ents.append(ent)
    # ents = [e for e in old_ents if e.label_ in KEEP]
    return new_ents


def read_lines(args):
    """Read & filter lines."""
    logging.info('Reading records.')
    filter_lines = re.compile(r'^(\uFEFF)?(\d+|Description|Habitat)')
    with open(args.text_file) as in_file:
        lines = in_file.readlines()
    lines = [shorten(ln) for ln in lines if filter_lines.match(ln)]
    return lines
