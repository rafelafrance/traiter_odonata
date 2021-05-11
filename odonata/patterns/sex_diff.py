"""Sex terms."""

from spacy import registry
from traiter.actions import text_action
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS, REPLACE

SIMILAR = """ like similar as than """.split()
TRAITS = """color color_mod body_part body_part_loc""".split()

SEX_DIFF = MatcherPatterns(
    'sex_diff',
    on_match='odonata.sex_diff.v1',
    decoder=COMMON_PATTERNS | {
        'adp': {'POS': {'IN': ['ADP']}},
        'cconj': {'POS': {'IN': ['CCONJ']}},
        'det': {'POS': {'IN': ['DET']}},
        'sconj': {'POS': {'IN': ['SCONJ', 'ADP']}},
        'sex': {'ENT_TYPE': 'sex'},
        'similar': {'LOWER': {'IN': SIMILAR}},
    },
    patterns=[
        'similar adp? sex cconj?',
        'sconj det? adp sex',
    ],
)


@registry.misc(SEX_DIFF.on_match)
def text_action_(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)
