"""Common color snippets."""

from spacy import registry
from traiter.const import DASH
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS, MISSING, REPLACE

JOINERS = DASH + """ with or on to and """.split()
COLOR_ADJ = """ fine thick broad thin mostly entire entirely narrow """.split()

DECODER = COMMON_PATTERNS | {
    'color': {'ENT_TYPE': 'color'},
    'any_color': {'ENT_TYPE': {'IN': ['color', 'color_mod']}},
    'prep': {'LOWER': {'IN': JOINERS}},
    'adj': {'LOWER': {'IN': COLOR_ADJ}},
    'part_loc': {'ENT_TYPE': 'part_loc'},
}

COLOR = MatcherPatterns(
    'color',
    on_match='odonata.color.v1',
    decoder=DECODER,
    patterns=[
        'adj+ color+ any_color?',
        'any_color+ -? color+',
        'any_color+ prep any_color+ prep color any_color',
        'any_color+ prep any_color+ prep color',
        'any_color+ prep? color+',
        'color prep? part_loc',
        'color+ -? any_color+',
        'color+',
        'missing adj+ color+ any_color?',
        'missing any_color* -? color+',
        'missing any_color* prep? color+',
        'missing color+ -? any_color+',
        'missing color+ any_color?',
        'missing color+ any_color?',
        'missing prep color+ any_color?',
    ],
)


@registry.misc(COLOR.on_match)
def color(ent):
    """Enrich the match."""
    data = {}
    lower = ent.text.lower()

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    label = 'color'
    if not any(t for t in ent if t._.cached_label == 'color'):
        label = 'color_mod'
        ent._.new_label = label

    data[label] = REPLACE.get(lower, lower)

    ent._.data = data
