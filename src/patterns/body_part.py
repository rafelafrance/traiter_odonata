"""Extract body part annotations."""

import spacy
from traiter.const import COMMA, DASH, DASH_RE, INT_TOKEN_RE

from ..pylib.const import MISSING, REPLACE

PART = ['part', 'fly']
ANY_PART = PART + ['part_loc']
NUMBERED = ['abdomen_seg', 'stripe', 'segments']
AS_PART = PART + ['abdomen_seg', 'segments']

PART_MOD = """ fine thick broad thin narrow irregular moderate unmarked """.split()
BOTH = """ both either """.split()

SEGMENTS = [
    {
        'label': 'segments',
        'patterns': [
            [{'LOWER': {'REGEX': fr'^s\d+{DASH_RE}\d+$'}}]
        ],
    }
]

BODY_PART = [
    {
        'label': 'body_part',
        'on_match': 'body_part.v1',
        'patterns': [
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': PART_MOD}, 'OP': '?'},
                {'ENT_TYPE': {'IN': NUMBERED}},
            ],
            [
                {'ENT_TYPE': {'IN': NUMBERED}},
                {'TEXT': {'IN': DASH}},
                {'TEXT': {'REGEX': INT_TOKEN_RE}},
            ],
            [
                {'ENT_TYPE': {'IN': NUMBERED}},
                {'TEXT': {'IN': DASH}},
                {'ENT_TYPE': {'IN': NUMBERED}},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'LOWER': {'IN': PART_MOD}},
                {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
            ],
            [
                {'IS_ALPHA': True},
                {'TEXT': {'IN': DASH}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '*'},
                {'LOWER': {'IN': PART_MOD}, 'OP': '?'},
                {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': BOTH}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                {'POS': {'IN': ['ADP', 'CCONJ']}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'LOWER': {'IN': PART_MOD}},
                {'TEXT': {'IN': COMMA}, 'OP': '?'},
                {'LOWER': {'IN': PART_MOD}},
                {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'LOWER': {'IN': BOTH}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                {'POS': 'ADP'},
                {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'LOWER': {'IN': BOTH}},
                {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
                {'POS': 'ADP'},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'LOWER': {'IN': PART_MOD}},
                {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
                {'TEXT': {'IN': COMMA}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': BOTH}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                {'POS': {'IN': ['ADP', 'CCONJ']}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                {'POS': {'IN': ['ADP', 'CCONJ']}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '*'},
            ],
            [
                {'LOWER': {'IN': BOTH}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                {'POS': {'IN': ['ADP', 'CCONJ']}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                {'POS': {'IN': ['ADP', 'CCONJ']}},
                {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
            ],
        ],
    },
]


@spacy.registry.misc(BODY_PART[0]['on_match'])
def body_part(ent):
    """Enrich the match."""
    data = {}

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    label = 'body_part'
    if not any(t for t in ent if t._.cached_label in AS_PART):
        label = 'body_part_loc'
        ent._.new_label = label

    lower = ent.text.lower()
    data[label] = REPLACE.get(lower, lower)

    ent._.data = data
