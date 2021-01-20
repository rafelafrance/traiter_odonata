#!/usr/bin/env python3
"""Extract Odonata traits from scientific literature."""

import argparse
import re
import textwrap

from spacy.tokens import Doc
from tqdm import tqdm

from src.patterns.sex_linker import sex_linker
from src.pylib.pipeline import sentence_pipeline, trait_pipeline
from src.writers.html_ import html_writer


def paulson_guide(args):
    """Parse Paulson's Odonate guide."""
    trait_nlp = trait_pipeline()
    sent_nlp = sentence_pipeline()

    filter_lines = re.compile(r'(\d+|Description)')
    lines = args.input.readlines()
    lines = [ln for ln in lines if filter_lines.match(ln)]
    lines = [' '.join(ln.split()) for ln in lines]

    rows = []
    for sent_doc in tqdm(sent_nlp.pipe(lines)):
        texts = [s.text for s in sent_doc.sents]
        starts = [s.start_char for s in sent_doc.sents]
        docs = [d for d in trait_nlp.pipe(texts)]
        for start, doc in zip(starts, docs):
            for ent in doc.ents:
                ent._.data['start'] += start
                ent._.data['end'] += start
        doc = Doc.from_docs(docs)
        sex_linker(doc)
        traits = [e._.data for e in doc.ents]
        rows.append({'doc': doc, 'traits': traits})

    if args.html_file:
        html_writer(args, rows)


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
