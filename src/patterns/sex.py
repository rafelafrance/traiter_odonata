"""Sex terms."""

import spacy
from traiter.pipes.entity_data import text_action

from ..pylib.consts import REPLACE

SEX = [
    {
        'label': 'sex',
        'on_match': 'sex.v1',
        'patterns': [
            [
                {'ENT_TYPE': 'sex'},
            ],
        ],
    },
]


@spacy.registry.misc(SEX[0]['on_match'])
def sex(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)
