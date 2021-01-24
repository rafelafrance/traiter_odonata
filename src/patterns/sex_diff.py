"""Sex terms."""

import spacy
from traiter.linker_utils import linker
from traiter.pipes.entity_data import text_action

from .linker_patterns import linker_patterns
from ..pylib.consts import REPLACE

SIMILAR = """ like similar as than """.split()
TRAITS = """color color_mod body_part body_part_loc""".split()

SEX_DIFF = [
    {
        'label': 'sex_diff',
        'on_match': 'sex_diff.v1',
        'patterns': [
            [
                {'LOWER': {'IN': SIMILAR}},
                {'POS': {'IN': ['ADP']}, 'OP': '?'},
                {'ENT_TYPE': 'sex'},
                {'POS': {'IN': ['CCONJ']}, 'OP': '?'},
            ],
            [
                {'POS': {'IN': ['SCONJ', 'ADP']}},
                {'POS': {'IN': ['DET']}, 'OP': '?'},
                {'POS': {'IN': ['ADP']}},
                {'ENT_TYPE': 'sex'},
            ],
        ],
    },
]

SEX_DIFF_LINKER = [
    {
        'label': 'sex_diff_linker',
        'on_match': 'sex_diff_linker.v1',
        'patterns': linker_patterns('sex_diff', traits=TRAITS)
    },
]


@spacy.registry.misc(SEX_DIFF[0]['on_match'])
def sex_diff(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)


@spacy.registry.misc(SEX_DIFF_LINKER[0]['on_match'])
def sex_diff_linker(_, doc, idx, matches):
    """Link traits to the sex diff trait."""
    linker(_, doc, idx, matches, 'sex_diff')
