"""Get terms from various sources (CSV files or SQLite database."""

from traiter.pylib.terms import get_common_names, itis_terms, read_terms

from .util import DATA_DIR, VOCAB_DIR

ODONATA_TERMS = VOCAB_DIR / 'odonata.csv'
COMMON_TERMS = VOCAB_DIR / 'common.csv'
ITIS_DB = DATA_DIR / 'ITIS.sqlite'

TERMS = read_terms(ODONATA_TERMS)
TERMS += read_terms(COMMON_TERMS)
TERMS += itis_terms('Odonata', abbrev=True, species=True)
TERMS += get_common_names('Odonata')

REPLACE = {t['pattern']: r for t in TERMS if (r := t.get('replace'))}
