"""Common color snippets."""

from traiter.actions import text_action

from ..pylib.consts import COLOR_MOD, DASH, GROUP_STEP, MISSING, REPLACE

ALL_COLORS = ['color', 'color_mod']
JOINERS = DASH + ['with', 'or', 'to', 'and']


def color(span):
    """Enrich the match."""
    data = text_action(span, REPLACE)
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
                    {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                ],
                [
                    {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
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
            'label': 'color_mod',
            'on_match': color,
            'patterns': [
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color_mod', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color_mod', 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': 'color_mod', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
                    {'ENT_TYPE': 'color_mod', 'OP': '+'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': 'color_mod', 'OP': '*'},
                    {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                    {'ENT_TYPE': 'color_mod', 'OP': '+'},
                ],
            ],
        },
    ],
}
