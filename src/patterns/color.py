"""Common color snippets."""

import spacy

from ..pylib.consts import DASH, MISSING, REPLACE

ALL_COLORS = ['color', 'color_mod']

JOINERS = DASH + ['with', 'or', 'to', 'and']
COLOR_ADJ = """ fine thick broad thin mostly entire entirely narrow """.split()

COLOR = [
    {
        'label': 'color',
        'on_match': 'color.v1',
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
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'TEXT': {'IN': COLOR_ADJ}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
                {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
                {'ENT_TYPE': 'color', 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'TEXT': {'IN': COLOR_ADJ}, 'OP': '?'},
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
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'TEXT': {'IN': COLOR_ADJ}, 'OP': '?'},
                {'ENT_TYPE': 'color_mod', 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'TEXT': {'IN': COLOR_ADJ}, 'OP': '?'},
                {'ENT_TYPE': 'color_mod', 'OP': '+'},
                {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                {'ENT_TYPE': 'color_mod', 'OP': '+'},
            ],
            [
                {'LOWER': {'IN': MISSING}, 'OP': '?'},
                {'TEXT': {'IN': COLOR_ADJ}, 'OP': '?'},
                {'ENT_TYPE': 'color_mod', 'OP': '+'},
                {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                {'ENT_TYPE': 'color_mod', 'OP': '*'},
                {'TEXT': {'IN': JOINERS}, 'OP': '?'},
                {'ENT_TYPE': 'color_mod', 'OP': '+'},
            ],
        ],
    },
]


@spacy.registry.misc(COLOR[0]['on_match'])
def color(ent):
    """Enrich the match."""
    data = {}

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    label = 'color'
    if not any(t for t in ent if t._.label_cache == 'color'):
        label = 'color_mod'
        ent._.new_label = label

    lower = ent.text.lower()
    data[label] = REPLACE.get(lower, lower)

    ent._.data = data
