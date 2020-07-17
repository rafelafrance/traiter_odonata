"""Utilities for converting PDFs into text."""

import re
from pathlib import Path

import pdftotext
from traiter.util import FLAGS

from .db import connect
from .util import now


def pdfs_to_text(pdfs):
    """Load PDFs into the database."""
    for pdf in pdfs:
        pdf_to_text(pdf)


def pdf_to_text(path):
    """Load one PDF into the database."""
    path = Path(path)
    doc_id = path.name

    with open(path, 'rb') as handle:
        pdf = pdftotext.PDF(handle)
    text = '\n\n'.join(pdf)

    sql = """
        INSERT OR REPLACE INTO docs
            (doc_id, path, loaded, edited, extracted, method, raw, edits)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
    with connect() as cxn:
        cxn.execute(
            sql,
            (doc_id, str(path), now(), '', '', 'pdf to text', text, text))


def clean_text_more(text):
    """Clean peculiarities particular to these guides."""
    text = re.sub(r'(?<= [a-z] -) \s (?= [a-z])', '', text, flags=FLAGS)
    text = re.sub(r'(?<= [a-z]) \s (?= - [a-z])', '', text, flags=FLAGS)
    text = re.sub(r'(?<=[a-z]) / (?=[a-z])', 'l', text, flags=FLAGS)
    return text
