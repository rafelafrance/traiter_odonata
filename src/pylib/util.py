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

TERMS = terms.shared_terms('animal_terms.csv')
TERMS += terms.shared_terms('insect_body_terms.csv')
TERMS += terms.shared_terms('metric_terms.csv')
TERMS += terms.shared_terms('time_terms.csv')
TERMS += terms.shared_terms('color_terms.csv')
TERMS += terms.read_terms(VOCAB_DIR / 'odonata_terms.csv')
TERMS += terms.read_terms(VOCAB_DIR / 'odonata_species.csv')
TERMS += terms.read_terms(VOCAB_DIR / 'common_terms.csv')
TERMS += terms.itis_common_names(taxon='Odonata')
TERMS += terms.abbrev_species(TERMS, label='odonata')
REPLACE = {t['pattern']: r for t in TERMS if (r := t.get('replace'))}

ABBREVS = """
    Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    mm cm m
    """

CLOSE = ' ) ] '.split()
COMMA = ' , '.split()
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
MISSING = """ without missing lacking """.split()
