"""Sex terms."""

from functools import partial

from traiter.actions import text_action

from ..pylib.consts import REPLACE

SIMILAR = """ like similar as """.split()

SEX = [
    {
        'label': 'sex_diff',
        'action': partial(text_action, replace=REPLACE),
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
