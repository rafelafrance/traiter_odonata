"""Extract body part annotations."""

from ..pylib.consts import COMMA, DASH, INT, MISSING, REPLACE

PART = ['part', 'fly']
ANY_PART = PART + ['part_loc']
NUMBERED = ['abdomen_seg', 'stripe']
AS_PART = PART + ['abdomen_seg']
PART_MOD = """ fine thick broad thin narrow irregular moderate unmarked """.split()
BOTH = """ both either """.split()


def body_part(ent):
    """Enrich the match."""
    data = {}

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    label = 'body_part'

    if not any(t for t in ent if t._.prev_label in AS_PART):
        label = 'body_part_loc'
        ent._.new_label = label

    data[label] = REPLACE.get(ent.lower_, ent.lower_)

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
