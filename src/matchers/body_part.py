"""Extract body part annotations."""

from traiter.actions import text_action

from ..pylib.consts import BOTH, COMMA, DASH, INT, MISSING, PART_MOD, REPLACE

PART = ['part', 'fly']
ANY_PART = PART + ['part_loc']
NUMBERED = ['abdomen_seg', 'stripe']
AS_PART = PART + ['abdomen_seg']


def body_part(ent):
    """Enrich the match."""
    print(ent)
    data = text_action(ent, REPLACE)

    if not [t for t in ent if t.ent_type_ in AS_PART]:
        data['_label'] = 'body_part_loc'

    if [t for t in ent if t.lower_ in MISSING]:
        data['missing'] = True

    ent._.data = data


BODY_PART = [
    {
        'label': 'body_part',
        'action': body_part,
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
                {'TEXT': {'REGEX': INT}},
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
