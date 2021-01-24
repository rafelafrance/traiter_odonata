"""Link traits to body parts."""

import spacy
from traiter.linker_utils import linker

from .linker_patterns import linker_patterns

TRAITS = ['color', 'color_mod']
LINKERS = ['prep', 'conj', 'cc']

BODY_PART_LINKER = [
    {
        'label': 'body_part_linker',
        'on_match': 'body_part_linker.v1',
        'patterns': linker_patterns('body_part')
    },
]


@spacy.registry.misc(BODY_PART_LINKER[0]['on_match'])
def body_part_linker(_, doc, idx, matches):
    """Use an entity matcher for entity linking."""
    linker(_, doc, idx, matches, 'body_part')
