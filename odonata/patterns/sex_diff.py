"""Sex terms."""

import spacy
from traiter.pipe_util import text_action
from traiter.pipes.dependency import NEAREST_LINKER

from odonata.patterns.linker_patterns import linker_patterns
from odonata.pylib.const import REPLACE
from odonata.pylib.token import COMPILE

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
        'patterns': COMPILE.to_patterns(
            MAP,
            'similar adp? sex cconj?',
            'sconj det? adp sex',
        ),
    },
]

SEX_DIFF_LINKER = [
    {
        'label': 'sex_diff_linker',
        'patterns': linker_patterns('sex_diff', traits=TRAITS),
        'on_match': {
            'func': NEAREST_LINKER,
            'kwargs': {'root': 'sex_diff', 'exclude': ''}
        },
    },
]


@spacy.registry.misc(SEX_DIFF[0]['on_match'])
def sex_diff(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)
