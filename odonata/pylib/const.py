"""Constants used in multiple modules."""

from pathlib import Path

from traiter.const import CLOSE, COMMA, DASH, OPEN, SLASH
from traiter.terms.itis import ITIS_DB, Itis

VOCAB_DIR = Path.cwd() / 'odonata' / 'vocabulary'

# #########################################################################
# Term relate constants
TERMS = Itis.shared('animals insect_anatomy units colors')
TERMS += Itis.read_csv(VOCAB_DIR / 'odonata_terms.csv')
TERMS += Itis.read_csv(VOCAB_DIR / 'odonata_species.csv')

if ITIS_DB.exists():
    TERMS += Itis.itis_common_names(taxon='Odonata')
else:
    TERMS += Itis.mock_itis_traits(VOCAB_DIR / 'mock_itis_terms.csv', 'Odonata')

TERMS += Itis.abbrev_species(TERMS, label='odonata')
TERMS += Itis.taxon_level_terms(
    TERMS, label='odonata', new_label='odonata_species')

TERMS.drop('imperial_length')

REPLACE = TERMS.pattern_dict('replace')

# #########################################################################
# Tokenizer constants
ABBREVS = """
    Jan. Feb. Mar. Apr. Jun. Jul. Aug. Sep. Sept. Oct. Nov. Dec.
    mm. cm. m.
    """.split()

# #########################################################################
# Pattern related constants
CONJ = ['or', 'and']
MISSING = """ without missing lack lacking except excepting not """.split()

COMMON_PATTERNS = {
    '(': {'TEXT': {'IN': CLOSE}},
    ',': {'TEXT': {'IN': COMMA}},
    'or': {'LOWER': {'IN': CONJ}},
    'and': {'LOWER': {'IN': CONJ}},
    '-': {'TEXT': {'IN': DASH}},
    '0-9+': {'IS_DIGIT': True},
    '99': {'IS_DIGIT': True},
    'a-z+': {'IS_ALPHA': True},
    'missing': {'LOWER': {'IN': MISSING}},
    'odonata': {'ENT_TYPE': 'odonata'},
    'odonata_species': {'ENT_TYPE': 'odonata_species'},
    'common_name': {'ENT_TYPE': 'common_name'},
    ')': {'TEXT': {'IN': OPEN}},
    '/': {'TEXT': {'IN': SLASH}},
}

# #########################################################################
# Entities

FORGET = """
    doc_heading group hind_wing_length_key
    metric_length odonata_species range stripe
    """.split()
