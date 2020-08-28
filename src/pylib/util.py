"""Utilities and constants."""

from pathlib import Path

from traiter.pylib.terms import get_common_names, itis_terms, read_terms

NAME = 'odonata'

DATA_DIR = Path('.') / 'data'
DOC_DIR = DATA_DIR
PDF_DIR = DOC_DIR / 'pdf'
TXT_DIR = DOC_DIR / 'txt'
VOCAB_DIR = Path('.') / 'src' / 'vocabulary'

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
