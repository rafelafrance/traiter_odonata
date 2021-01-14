"""Utilities and constants."""

from pathlib import Path

from traiter.terms.itis import Itis

DATA_DIR = Path.cwd() / 'data'
DOC_DIR = DATA_DIR
PDF_DIR = DOC_DIR / 'pdf'
TXT_DIR = DOC_DIR / 'txt'
VOCAB_DIR = Path.cwd() / 'src' / 'vocabulary'

GROUP_STEP = 'group'
TRAIT_STEP = 'traits'
HEADER_STEP = 'header'
PART_STEP = 'part'
SEX_STEP = 'sex'

TERMS = Itis.read_csv(VOCAB_DIR / 'odonata_terms.csv')
TERMS += Itis.read_csv(VOCAB_DIR / 'odonata_species.csv')
TERMS += Itis.shared('animals insect_anatomy units time colors')
TERMS += Itis.itis_common_names(taxon='Odonata')
TERMS += Itis.abbrev_species(TERMS, label='odonata')
TERMS += Itis.taxon_level_terms(
    TERMS, label='odonata', new_label='odonata_species')
TERMS.drop('imperial_length')

REPLACE = TERMS.pattern_dicts('replace')
POS = TERMS.pattern_dicts('pos')

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
MISSING = """ without missing lack lacking except excepting not """.split()
BOTH = """ both either """.split()
COLOR_MOD = """ fine thick broad thin mostly entire entirely narrow """.split()
PART_MOD = """ fine thick broad thin narrow irregular moderate unmarked """.split()
