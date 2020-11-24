"""Extract body part annotations."""

from src.traiter.traiter.pylib.util import squash

from ..pylib.util import COMMA, GROUP_STEP, REPLACE


def body_part(span):
    """Enrich the match."""
    return {'body_part': REPLACE.get(span.lower_, span.lower_)}


def multiple_parts(span):
    """Enrich the match."""
    parts = []
    for token in span:
        if token.ent_type_ == 'part':
            parts.append(token.lower_)
    return {'body_part': squash(parts)}


JOINER = ['and', 'or'] + COMMA

BODY_PART = {
    GROUP_STEP: [
        {
            'label': 'body_part',
            'on_match': body_part,
            'patterns': [
                [
                    {'ENT_TYPE': 'part', 'OP': '+'},
                ],
                [
                    {'ENT_TYPE': {'IN': ['location', 'part']}, 'OP': '*'},
                    {'ENT_TYPE': 'part'},
                ],
            ],
        },
        {
            'label': 'body_part',
            'on_match': multiple_parts,
            'patterns': [
                [
                    {'ENT_TYPE': 'part', 'OP': '+'},
                    {'LOWER': {'IN': JOINER}, 'OP': '*'},
                    {'ENT_TYPE': 'part', 'OP': '*'},
                    {'LOWER': {'IN': JOINER}, 'OP': '*'},
                    {'ENT_TYPE': 'part', 'OP': '+'},
                ],
            ],
        },
    ],
}
