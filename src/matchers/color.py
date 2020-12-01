"""Common color snippets."""

from ..pylib.actions import text_action
from ..pylib.util import DASH, GROUP_STEP, MISSING, PATTERN_MOD

ALL_COLORS = ['color', 'color_modifier']
JOINERS = DASH + ['with', 'or', 'to', 'and']


def color(span):
    """Enrich the match."""
    data = text_action(span)
    if [t for t in span if t.lower_ in MISSING]:
        data['missing'] = True
    return data


COLOR = {
    GROUP_STEP: [
        {
            'label': 'color',
            'on_match': color,
            'patterns': [
                [
                    {'TEXT': {'IN': PATTERN_MOD}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                ],                [
                    {'TEXT': {'IN': PATTERN_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': PATTERN_MOD}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': PATTERN_MOD}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
                ],
            ],
        },
        {
            'label': 'color_pat',
            'on_match': color,
            'patterns': [
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': PATTERN_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color_modifier', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': PATTERN_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color_modifier', 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': 'color_modifier', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': PATTERN_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color_modifier', 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': 'color_modifier', 'OP': '*'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': 'color_modifier', 'OP': '+'},
                ],
            ],
        },
    ],
}
