"""Sex terms."""

from spacy import registry
from traiter.actions import text_action
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS, REPLACE

COLORED = """ colored """.split()
SIMILAR = """ like similar as than """.split()
TRAITS = """color color_mod body_part body_part_loc""".split()

COLOR_LIKE = MatcherPatterns(
    'color_like',
    on_match='odonata.color_like.v1',
    decoder=COMMON_PATTERNS | {
        'adp': {'POS': {'IN': ['ADP']}},
        'cconj': {'POS': {'IN': ['CCONJ']}},
        'det': {'POS': {'IN': ['DET']}},
        'sconj': {'POS': {'IN': ['SCONJ', 'ADP']}},
        'sex': {'ENT_TYPE': 'sex'},
        'similar': {'LOWER': {'IN': SIMILAR}},
        'colored': {'LOWER': {'IN': COLORED}},
    },
    patterns=[
        'similar adp? sex',
        'sconj det? adp sex',
        'colored similar sex',
    ],
)


@registry.misc(COLOR_LIKE.on_match)
def color_like(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)
