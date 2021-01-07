"""Utilities and constants."""

from pathlib import Path

from traiter.pylib.itis_terms import ItisTerms

DATA_DIR = Path.cwd() / 'data'
DOC_DIR = DATA_DIR
PDF_DIR = DOC_DIR / 'pdf'
TXT_DIR = DOC_DIR / 'txt'
VOCAB_DIR = Path.cwd() / 'src' / 'vocabulary'

GROUP_STEP = 'group'
TRAIT_STEP = 'traits'
HEADER_STEP = 'header'
LINK_STEP = 'link'

TERMS = ItisTerms.read_csv(VOCAB_DIR / 'odonata_terms.csv')
TERMS += ItisTerms.read_csv(VOCAB_DIR / 'odonata_species.csv')
TERMS += ItisTerms.read_csv(VOCAB_DIR / 'common_terms.csv')
TERMS += ItisTerms.shared('animals insect_anatomy units time colors')
TERMS += ItisTerms.itis_common_names(taxon='Odonata')
TERMS += ItisTerms.abbrev_species(TERMS, label='odonata')
TERMS += ItisTerms.taxon_level_terms(
    TERMS, label='odonata', new_label='odonata_species')
TERMS.drop('imperial_length')

REPLACE = TERMS.pattern_dicts('replace')

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
