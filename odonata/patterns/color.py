"""Common color snippets."""

from traiter.const import DASH
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS, MISSING, REPLACE

ALL_COLORS = ['color', 'color_mod']
JOINERS = DASH + ['with', 'or', 'to', 'and']
COLOR_ADJ = """ fine thick broad thin mostly entire entirely narrow """.split()


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


COLOR = MatcherPatterns(
    'color',
    on_match=color,
    decoder=COMMON_PATTERNS | {
        'any_color': {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '+'},
        'any_color?': {'ENT_TYPE': {'IN': ALL_COLORS}, 'OP': '*'},
        'join?': {'TEXT': {'IN': JOINERS}, 'OP': '?'},
        'color_adj?': {'TEXT': {'IN': COLOR_ADJ}, 'OP': '?'},
        'color_mod': {'ENT_TYPE': 'color_mod', 'OP': '+'},
        'color_mod?': {'ENT_TYPE': 'color_mod', 'OP': '*'},
        'color': {'ENT_TYPE': 'color', 'OP': '+'},
    },
    patterns=[
        'missing? color - any_color?',
        'missing? any_color? - color',

        'missing? any_color? color any_color?',

        ('missing? color_adj? any_color join? any_color? join? any_color? '
         'color any_color? join? any_color'),

        'missing? color_adj? any_color join? any_color? join? any_color? color',

        'missing? color_adj? color_mod',
        'missing? color_adj? color_mod join? color_mod',
        'missing? color_adj? color_mod join? color_mod join? color_mod',
    ],
)
