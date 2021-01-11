"""Extract body part annotations."""

from traiter.actions import text_action

from ..pylib.consts import BOTH, COMMA, DASH, GROUP_STEP, INT, MISSING, PART_MOD, \
    REPLACE

PART = ['part', 'fly']
ANY_PART = PART + ['part_loc']
NUMBERED = ['abdomen_seg', 'stripe']
AS_PART = ANY_PART + ['abdomen_seg']


def body_part(span):
    """Enrich the match."""
    data = text_action(span, REPLACE)

    if not [t for t in span if t.ent_type_ in AS_PART]:
        data['_label'] = 'body_part_loc'

    if [t for t in span if t.lower_ in MISSING]:
        data['missing'] = True

    return data


def multiple_parts(span):
    """Enrich the match."""
    data = {}
    parts = [t for t in span if t.ent_type_ == 'body_part']
    for part in parts:
        data = {**data, **part._.data}
    data['body_part'] = span.lower_
    return data


BODY_PART = {
    GROUP_STEP: [
        {
            'label': 'body_part',
            'on_match': body_part,
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
    ],
}
