"""Common color modification snippets."""

from spacy import registry
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS, REPLACE, MISSING

COLOR_ADJ = """ fine thick broad thin mostly entire entirely narrow """.split()

DECODER = COMMON_PATTERNS | {
    'mod': {'ENT_TYPE': 'color_mod'},
    'color': {'ENT_TYPE': 'color'},
    'subpart': {'ENT_TYPE': 'subpart'},
    'loc': {'ENT_TYPE': 'part_loc'},
    'adv': {'DEP': 'advmod'},
    'adj': {'LOWER': {'IN': COLOR_ADJ}},
    'prep': {'DEP': 'prep'},
}

COLOR_MOD = MatcherPatterns(
    'color_mod',
    on_match='odonata.color_mod.v1',
    decoder=DECODER,
    patterns=[
        'missing? mod+',
        'missing? loc mod',
        'missing? mod subpart',
        'prep color mod',
        'adv mod+',
        'adj mod+',
        'adv mod+ prep subpart',
        'mod+ prep? subpart prep? color',
    ],
)


@registry.misc(COLOR_MOD.on_match)
def color_mod(ent):
    """Enrich the match."""
    data = {}
    lower = ent.text.lower()

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    data['color_mod'] = REPLACE.get(lower, lower)

    ent._.data = data
