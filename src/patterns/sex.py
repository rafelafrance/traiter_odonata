"""Sex terms."""

import spacy
from traiter.pipes.entity_data import text_action

from ..pylib.consts import REPLACE

SIMILAR = """ like similar as than """.split()
TRAITS = ['color', 'color_mod']

SEX = [
    {
        'label': 'sex',
        'on_match': 'sex.v1',
        'patterns': [
            [
                {'ENT_TYPE': 'sex'},
            ],
        ],
    },
    {
        'label': 'sex_diff',
        'on_match': 'sex.v1',
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
        'patterns': [
            # sex diff is the parent of the trait
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            # Body part is the child of the trait
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '<',
                    'RIGHT_ID': 'trait',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
        ]
    },
]


@spacy.registry.misc(SEX[0]['on_match'])
def sex(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)


@spacy.registry.misc(SEX_DIFF_LINKER[0]['on_match'])
def sex_diff_linker(_, doc, idx, matches):
    """Link traits to the sex diff trait."""
    ents = {}
    for i in matches[idx][1]:
        for ent in doc.ents:
            if ent.start <= i <= ent.end - 1:
                ents[i] = ent
                break
    root, *others = ents.values()
    body_part = root._.data['sex_diff']
    for ent in others:
        ent._.data['sex_diff'] = body_part
