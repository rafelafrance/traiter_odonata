"""Sex terms."""

import spacy
from traiter.pipe_util import text_action

from odonata.pylib.const import REPLACE
from odonata.pylib.token import COMPILE_MATCHES

SIMILAR = """ like similar as than """.split()
TRAITS = """color color_mod body_part body_part_loc""".split()

MAP = {
    'adp': {'POS': {'IN': ['ADP']}},
    'cconj': {'POS': {'IN': ['CCONJ']}},
    'det': {'POS': {'IN': ['DET']}},
    'sconj': {'POS': {'IN': ['SCONJ', 'ADP']}},
    'sex': {'ENT_TYPE': 'sex'},
    'similar': {'LOWER': {'IN': SIMILAR}},
}

SEX_DIFF = [
    {
        'label': 'sex_diff',
        'on_match': 'sex_diff.v1',
        'patterns': COMPILE_MATCHES(
            MAP,
            'similar adp? sex cconj?',
            'sconj det? adp sex',
        ),
    },
]


@spacy.registry.misc(SEX_DIFF[0]['on_match'])
def sex_diff(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)
