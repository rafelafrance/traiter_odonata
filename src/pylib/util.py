"""Utilities and constants."""

from pathlib import Path

import traiter.spacy_nlp.terms as terms

DATA_DIR = Path.cwd() / 'data'
DOC_DIR = DATA_DIR
PDF_DIR = DOC_DIR / 'pdf'
TXT_DIR = DOC_DIR / 'txt'
VOCAB_DIR = Path.cwd() / 'src' / 'vocabulary'

GROUP_STEP = 'group'
TRAIT_STEP = 'traits'
HEADER_STEP = 'header'
LINK_STEP = 'link'

TERMS = terms.read_terms(VOCAB_DIR / 'odonata.csv')
TERMS += terms.read_terms(VOCAB_DIR / 'common.csv')
TERMS += terms.itis_terms(taxon='Odonata', label='odonata')
TERMS += terms.itis_common_names(taxon='Odonata')
TERMS += terms.species_only(TERMS, label='odonata')
TERMS += terms.abbrev_species(TERMS, label='odonata')
REPLACE = {t['pattern']: r for t in TERMS if (r := t.get('replace'))}

ABBREVS = """
    Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    mm cm m
    """

CLOSE = ' ) ] '.split()
CROSS = ' x × '.split()
DASH = ' – - –– -- '.split()
DOT = ' . '.split()
INT = r'^\d+$'
NUMBER = r'^\d+(\.\d*)?$'
OPEN = ' ( [ '.split()
PLUS = ' + '.split()
SLASH = ' / '.split()
QUOTE = ' “ ” " \' '.split()
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

PER_COUNTS = """ pair pairs """.split()
PER_COUNT = set(PER_COUNTS)
