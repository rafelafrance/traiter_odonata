"""Utilities and constants."""

from pathlib import Path

import traiter.pylib.terms as terms

DATA_DIR = Path.cwd() / 'data'
DOC_DIR = DATA_DIR
PDF_DIR = DOC_DIR / 'pdf'
TXT_DIR = DOC_DIR / 'txt'
VOCAB_DIR = Path.cwd() / 'src' / 'vocabulary'

TERM_STEP = 'terms'
GROUP_STEP = 'group'
TRAIT_STEP = 'traits'
HEADER_STEP = 'header'
LINK_STEP = 'link'

TERMS = terms.shared_terms('animals.csv')
TERMS += terms.shared_terms('insect_anatomy.csv')
TERMS += terms.shared_terms('units.csv')
TERMS += terms.shared_terms('time.csv')
TERMS += terms.shared_terms('colors.csv')
TERMS += terms.read_terms(VOCAB_DIR / 'odonata_terms.csv')
TERMS += terms.read_terms(VOCAB_DIR / 'odonata_species.csv')
TERMS += terms.read_terms(VOCAB_DIR / 'common_terms.csv')
TERMS += terms.itis_common_names(taxon='Odonata')
TERMS += terms.abbrev_species(TERMS, label='odonata')
TERMS += terms.taxon_level_terms(TERMS, label='odonata', new_label='odonata_species')
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
MISSING = """ without missing lack lacking except excepting """.split()
BOTH = """ both either """.split()
COLOR_MOD = """ fine thick broad thin mostly entire entirely narrow """.split()
PART_MOD = """ fine thick broad thin narrow irregular moderate unmarked """.split()
