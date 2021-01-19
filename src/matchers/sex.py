"""Sex terms."""

import spacy
from traiter.pipes.entity_data import text_action

from ..pylib.consts import REPLACE

SIMILAR = """ like similar as """.split()

SEX = [
    {
        'label': 'sex_diff',
        'action': 'sex_diff.v1',
        'patterns': [
            [
                {'LOWER': {'IN': SIMILAR}},
                {'POS': {'IN': ['ADP']}, 'OP': '?'},
                {'ENT_TYPE': 'sex'},
                {'POS': {'IN': ['CCONJ']}, 'OP': '?'},
            ],
            [
                {'POS': {'IN': ['SCONJ']}},
                {'POS': {'IN': ['DET']}, 'OP': '?'},
                {'POS': {'IN': ['ADP']}, 'OP': '?'},
                {'ENT_TYPE': 'sex'},
            ],
        ],
    },
]


@spacy.registry.misc(SEX[0]['action'])
def sex_diff(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)
