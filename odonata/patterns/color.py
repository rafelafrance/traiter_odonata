"""Common color snippets."""

from spacy import registry
from traiter.const import DASH
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS, MISSING, REPLACE

JOINERS = DASH + ['with', 'or', 'to', 'and']
COLOR_ADJ = """ fine thick broad thin mostly entire entirely narrow """.split()

DECODER = COMMON_PATTERNS | {
    'color': {'ENT_TYPE': 'color'},
    'color_mod': {'ENT_TYPE': 'color_mod'},
    'any_color': {'ENT_TYPE': {'IN': ['color', 'color_mod']}},
    'prep': {'LOWER': {'IN': JOINERS}},
    'adj': {'LOWER': {'IN': COLOR_ADJ}},
    'part_loc': {'ENT_TYPE': 'part_loc'},
    'tip': {'LOWER': 'tip'},
}


COLOR = MatcherPatterns(
    'color',
    on_match='odonata.color.v1',
    decoder=DECODER,
    patterns=[
        'missing? any_color* -? color+',
        'missing? any_color* prep? color+',
        'missing? any_color* prep? tip',
        'missing? adj? any_color+',
        'any_color+ prep any_color+ prep color',
        'any_color+ prep any_color+ prep color any_color',
    ],
)


COLOR_MOD = MatcherPatterns(
    'color_mod',
    on_match='odonata.color_mod.v1',
    decoder=DECODER,
    patterns=[
        'part_loc color_mod',
    ],
)


@registry.misc(COLOR.on_match)
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


@registry.misc(COLOR_MOD.on_match)
def color_mod(ent):
    """Enrich the match."""
    lower = ent.text.lower()
    ent._.data = {'color_mod': REPLACE.get(lower, lower)}
