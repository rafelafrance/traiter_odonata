"""Common color snippets."""

import spacy
from traiter.const import DASH

from odonata.pylib.const import MISSING, REPLACE
from odonata.pylib.token import COMPILE_MATCHES

ALL_COLORS = ['color', 'color_mod']
JOINERS = DASH + ['with', 'or', 'to', 'and']
COLOR_ADJ = """ fine thick broad thin mostly entire entirely narrow """.split()

MAP = {
    'any_color': {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
    'any_color?': {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
    'join?': {'TEXT': {'IN': JOINERS}, 'OP': '?'},
    'color_adj?': {'TEXT': {'IN': COLOR_ADJ}, 'OP': '?'},
    'color_mod': {'ENT_TYPE': 'color_mod', 'OP': '+'},
    'color_mod?': {'ENT_TYPE': 'color_mod', 'OP': '*'},
    'color': {'ENT_TYPE': 'color', 'OP': '+'},
}

COLOR = [
    {
        'label': 'color',
        'on_match': 'color.v1',
        'patterns': COMPILE_MATCHES(
            MAP,
            'missing? color - any_color?',
            'missing? any_color? - color',

            'missing? any_color? color any_color?',

            ('missing? color_adj? any_color join? any_color? join? any_color? '
             'color any_color? join? any_color'),

            'missing? color_adj? any_color join? any_color? join? any_color? color',

            'missing? color_adj? color_mod',
            'missing? color_adj? color_mod join? color_mod',
            'missing? color_adj? color_mod join? color_mod join? color_mod',
        ),
    },
]


@spacy.registry.misc(COLOR[0]['on_match'])
def color(ent):
    """Enrich the match."""
    data = {}

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    label = 'color'
    if not any(t for t in ent if t._.cached_label == 'color'):
        label = 'color_mod'
        ent._.new_label = label

    lower = ent.text.lower()
    data[label] = REPLACE.get(lower, lower)

    ent._.data = data
