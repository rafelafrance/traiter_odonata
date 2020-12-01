"""Extract body part annotations."""

from ..pylib.actions import text_action
from ..pylib.util import BOTH, COMMA, DASH, GROUP_STEP, MISSING, PART_MOD

PART = ['part', 'fly']
ANY_PART = PART + ['part_location']


def body_part(span):
    """Enrich the match."""
    data = text_action(span)
    if [t for t in span if t.lower_ in MISSING]:
        data['missing'] = True
    return data


BODY_PART = {
    GROUP_STEP: [
        {
            'label': 'body_part',
            'on_match': body_part,
            'patterns': [
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'POS': 'ADJ'},
                    {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
                ],                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'LOWER': {'IN': PART_MOD}},
                    {'TEXT': {'IN': COMMA}, 'OP': '?'},
                    {'POS': 'ADJ'},
                    {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '*'},
                    {'LOWER': {'IN': PART_MOD}, 'OP': '?'},
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
                    {'LOWER': {'IN': PART_MOD}},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                    {'TEXT': {'IN': COMMA}},
                    {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '*'},
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
            ],
        },
        {
            'label': 'body_part_loc',
            'on_match': text_action,
            'patterns': [
                [
                    {'ENT_TYPE': 'part_location', 'OP': '+'},
                ],
                [
                    {'IS_ALPHA': True},
                    {'TEXT': {'IN': DASH}},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': BOTH}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                    {'POS': {'IN': ['ADP', 'CCONJ']}},
                    {'ENT_TYPE': {'IN': ANY_PART}, 'OP': '+'},
                ],
            ],
        },
    ],
}
