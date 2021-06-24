"""Link the color trait to other traits like body_part and color_mod. """

from traiter.patterns.dependency_patterns import DependencyPatterns
from traiter.pipes.dependency import LINK_NEAREST

COLOR_LINKER = DependencyPatterns(
    'color_linker',
    on_match={
        'func': LINK_NEAREST,
        'kwargs': {'anchor': 'color'}
    },
    decoder={
        'color': {'ENT_TYPE': 'color'},
        'mod': {'ENT_TYPE': 'color_mod'},
        'like': {'ENT_TYPE': 'color_like'},
        'part': {'ENT_TYPE': 'body_part'},
        'subpart': {'ENT_TYPE': 'body_subpart'},
        'prep': {'DEP': 'prep'},
        'conj': {'DEP': 'cc'},
    },
    patterns=[
        'part    .  color',
        'color   .  part',
        'color   .  subpart',
        'subpart .  color',
        'color   .  mod',
        'color   .  like',
        'mod     .  color',
        'like    .  color',
        'part    >> color',
        'color   >> part',
        'color   >> subpart',
        'color   >> mod',
        'color   >> like',
        'color   .  prep . part',
        'part    >> ( color ) mod ',
        'like . conj . part . color',
    ],
)
