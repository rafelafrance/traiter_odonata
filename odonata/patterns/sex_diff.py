"""Sex terms."""

import spacy
from traiter.entity_data_util import text_action
from traiter.pipes.dependency import NEAREST_LINKER

from .linker_patterns import linker_patterns
from ..pylib.const import REPLACE

SIMILAR = """ like similar as than """.split()
TRAITS = """color color_mod body_part body_part_loc""".split()

SEX_DIFF = [
    {
        'label': 'sex_diff',
        'on_match': 'sex_diff.v1',
        'patterns': [
            [
                {'LOWER': {'IN': SIMILAR}},
                {'POS': {'IN': ['ADP']}, 'OP': '?'},
                {'ENT_TYPE': 'sex'},
                {'POS': {'IN': ['CCONJ']}, 'OP': '?'},
            ],
            [
                {'POS': {'IN': ['SCONJ', 'ADP']}},
                {'POS': {'IN': ['DET']}, 'OP': '?'},
                {'POS': {'IN': ['ADP']}},
                {'ENT_TYPE': 'sex'},
            ],
        ],
    },
]

SEX_DIFF_LINKER = [
    {
        'label': 'sex_diff_linker',
        'patterns': linker_patterns('sex_diff', traits=TRAITS),
        'after_match': {
            'func': NEAREST_LINKER,
            'kwargs': {'root': 'sex_diff', 'exclude': ''}
        },
    },
]


@spacy.registry.misc(SEX_DIFF[0]['on_match'])
def sex_diff(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)
