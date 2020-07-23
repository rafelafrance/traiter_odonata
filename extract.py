#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import json

import src.pylib.db as db
import src.pylib.doc as doc
import src.pylib.util as util
from src.pylib.pipeline import attach, parse


def main():
    """Extract data from the files."""
    with db.connect(util.DATA_DIR / 'odonata.traiter') as cxn:
        df = doc.select_docs(cxn)
        for doc_id in df['doc_id']:
            text = doc.select_doc_edits(cxn, doc_id)
            text = ' '.join(text.split())  # TODO: Move to a pipeline
            traits = parse(text)
            traits = attach(traits)

            print(json.dumps(traits))


if __name__ == '__main__':
    main()
