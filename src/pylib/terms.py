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

# terms = [
#     {
#         'label': name,
#         'pattern': 'amphiagrion saucium',
#         'attr': 'lower',
#         'replace': 'Amphiagrion saucium',
#     },
#     {
#         'label': name,
#         'pattern': 'gomphurus externus',
#         'attr': 'lower',
#         'replace': 'Gomphurus externus',
#     },
#     {
#         'label': 'species',
#         'pattern': 'abbreviatum',
#         'attr': 'lower',
#         'replace': 'abbreviatum',
#     },
#     {
#         'label': 'common_name',
#         'pattern': 'western red damsel',
#         'attr': 'lower',
#         'replace': 'Amphiagrion saucium',
#     },
#     {
#         'label': 'common_name',
#         'pattern': 'plains clubtail',
#         'attr': 'lower',
#         'replace': 'Gomphurus externus',
#     },
# ]
