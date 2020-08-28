#!/usr/bin/env python3

"""Extract src traits from scientific literature (PDFs to text)."""

import html

import src.pylib.db as db
import src.pylib.doc as doc
import src.pylib.util as util
from src.pylib.pipeline import link, parse


CLASS = {
    'header': 'head',
    'total_length': 'len',
    'flight_period': 'fly',
    'habitat': 'habit',
}


def main():
    """Extract data from the files."""
    with db.connect(util.DATA_DIR / 'odonata.traiter') as cxn:
        df = doc.select_docs(cxn)
        for doc_id in df['doc_id']:
            text = doc.select_doc_edits(cxn, doc_id)
            text = ' '.join(text.split())  # TODO: Move to a pipeline
            traits = parse(text)
            traits = link(traits)

            parts = []
            prev_end = 0
            for record in traits:
                for trait in record:

                    if trait['start'] != prev_end:
                        prev = text[prev_end:trait['start']]
                        parts.append(html.escape(prev))

                    prev_end = trait['end']
                    if trait['trait'] == 'header':
                        parts.append(f'<br/><hr/>')

                    cls = CLASS[trait['trait']]
                    span = text[trait["start"]:trait["end"]]
                    span = html.escape(span)
                    parts.append(f'<span class="{cls}">{span}</span>')

            if prev_end != len(text):
                parts.append(html.escape(text[prev_end:]))

            result = ''.join(parts)
            print("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>Traiter</title>
                <style>
                    .head { font-weight: bold; }
                    .len { background-color: cyan; }
                    .fly { background-color: lightsalmon; }
                    .habit { background-color: lightgreen; }
                </style>
            </head>
            <body>
            """)
            print(result)
            print("""
                </body>
                </html>
            """)


if __name__ == '__main__':
    main()
