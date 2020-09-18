"""Spacy related constants."""

from traiter.spacy_nlp.terms import get_common_names, itis_terms, read_terms

from src.pylib.util import DATA_DIR, VOCAB_DIR

GROUP_STEP = 'group'
TRAIT_STEP = 'traits'
HEADER_STEP = 'header'
LINK_STEP = 'link'

ITIS_DB = DATA_DIR / 'ITIS.sqlite'

TERMS = read_terms(VOCAB_DIR / 'odonata.csv')
TERMS += read_terms(VOCAB_DIR / 'common.csv')
TERMS += itis_terms('Odonata', abbrev=True, species=True)
TERMS += get_common_names('Odonata')

REPLACE = {t['pattern']: r for t in TERMS if (r := t.get('replace'))}

ABBREVS = """
    Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    mm cm m
    """

CLOSE = ' ) ] '.split()
CROSS = ' x × '.split()
DASH = '– - –– --'.split()
DOT = ' . '.split()
INT = r'^\d+$'
NUMBER = r'^\d+(\.\d*)?$'
OPEN = ' ( [ '.split()
PLUS = ' + '.split()
SLASH = ' / '.split()
QUOTE = ' “ ” " \' '.split()
LETTERS = 'abcdefghijklmnopqrstuvwxyz'.split()
PER_COUNTS = ['pair', 'pairs']
PER_COUNT = set(PER_COUNTS)
