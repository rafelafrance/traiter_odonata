"""Common color snippets."""

from ..pylib.consts import DASH, MISSING, REPLACE

ALL_COLORS = ['color', 'color_mod']

JOINERS = DASH + ['with', 'or', 'to', 'and']
COLOR_MOD = """ fine thick broad thin mostly entire entirely narrow """.split()


def color(ent):
    """Enrich the match."""
    data = {}

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    label = 'color'
    if not any(t for t in ent if t._.label_cache == 'color'):
        label = 'color_mod'
        ent._.new_label = label

    lower = ' '.join(t.lower_ for t in ent)
    data[label] = REPLACE.get(lower, lower)

    ent._.data = data


COLOR = [
    {
        'label': 'color',
        'action': color,
        'patterns': [
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                {'ENT_TYPE': 'color'},
                {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'ENT_TYPE': 'color'},
                {'TEXT': {'IN': DASH}},
                {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                {'TEXT': {'IN': DASH}},
                {'ENT_TYPE': 'color'},
            ],
            # [
            #     {'LOWER': {'IN': MISSING}, 'OP': '?'},
            #     {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
            #     {'ENT_TYPE': 'color', 'OP': '+'},
            # ],
            # [
            #     {'LOWER': {'IN': MISSING}, 'OP': '?'},
            #     {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
            #     {'ENT_TYPE': 'color', 'OP': '+'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
            # ],
            # [
            #     {'LOWER': {'IN': MISSING}, 'OP': '?'},
            #     {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
            #     {'ENT_TYPE': 'color_mod', 'OP': '+'},
            # ],
            # [
            #     {'LOWER': {'IN': MISSING}, 'OP': '?'},
            #     {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
            #     {'ENT_TYPE': 'color_mod', 'OP': '+'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': 'color_mod', 'OP': '+'},
            # ],
            # [
            #     {'LOWER': {'IN': MISSING}, 'OP': '?'},
            #     {'TEXT': {'IN': COLOR_MOD}, 'OP': '?'},
            #     {'ENT_TYPE': 'color_mod', 'OP': '+'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': 'color_mod', 'OP': '*'},
            #     {'TEXT': {'IN': JOINERS}, 'OP': '?'},
            #     {'ENT_TYPE': 'color_mod', 'OP': '+'},
            # ],
        ],
    },
]
