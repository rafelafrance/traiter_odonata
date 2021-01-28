"""Link traits to body parts."""

from traiter.pipes.dependency import SIMPLE_POST_LINKER

from .linker_patterns import linker_patterns

TRAITS = ['color', 'color_mod']
LINKERS = ['prep', 'conj', 'cc']

BODY_PART_LINKER = [
    {
        'label': 'body_part_linker',
        'patterns': linker_patterns('body_part'),
        'after_match': {
            'func': SIMPLE_POST_LINKER,
            'kwargs': {'root': 'body_part', 'exclude': ''}
        },
    },
]
