"""Utilities and constants."""

from pathlib import Path

from traiter.pylib.terms import Terms

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

TERMS = Terms(
    csv_file=[VOCAB_DIR / 'odonata_terms.csv',
              VOCAB_DIR / 'odonata_species.csv',
              VOCAB_DIR / 'common_terms.csv'],
    shared='animals insect_anatomy units time colors',
    pattern_dicts='replace',
)
TERMS.itis_common_names(taxon='Odonata')
TERMS.abbrev_species(label='odonata')
TERMS.taxon_level_terms(label='odonata', new_label='odonata_species')
TERMS.drop('imperial_length')

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
