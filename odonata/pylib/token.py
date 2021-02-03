"""Common token patterns."""

from traiter.const import CLOSE, COMMA, DASH, OPEN, SLASH
from traiter.pattern_compiler import PatternCompiler

from odonata.pylib.const import CONJ, MISSING

COMMON_PATTERNS = {
    '(': {'TEXT': {'IN': CLOSE}},
    ',': {'TEXT': {'IN': COMMA}},
    'or': {'LOWER': {'IN': CONJ}},
    'and': {'LOWER': {'IN': CONJ}},
    '-': {'TEXT': {'IN': DASH}},
    '0-9+': {'IS_DIGIT': True},
    'a-z+': {'IS_ALPHA': True},
    'missing': {'LOWER': {'IN': MISSING}},
    'odonata': {'ENT_TYPE': 'odonata'},
    'odonata_species': {'ENT_TYPE': 'odonata_species'},
    'common_name': {'ENT_TYPE': 'common_name'},
    ')': {'TEXT': {'IN': OPEN}},
    '/': {'TEXT': {'IN': SLASH}},
}

COMPILE = PatternCompiler(COMMON_PATTERNS)
