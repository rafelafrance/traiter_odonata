"""Link the color trait to other traits like body_part and color_mod. """

from traiter.patterns.dependency_patterns import DependencyPatterns
from traiter.pipes.dependency import LINK_NEAREST

COLOR_MOD_LINKER = DependencyPatterns(
    'color_mod_linker',
    on_match={
        'func': LINK_NEAREST,
        'kwargs': {'anchor': 'color_mod'}
    },
    decoder={
        'color': {'ENT_TYPE': 'color'},
        'mod': {'ENT_TYPE': 'color_mod'},
        'like': {'ENT_TYPE': 'color_like'},
        'part': {'ENT_TYPE': 'body_part'},
        'subpart': {'ENT_TYPE': 'body_subpart'},
        'prep': {'DEP': 'prep'},
    },
    patterns=[
        'part    .  mod',
        'subpart .  mod',
        'color   .  mod',
        'like    .  mod',
        'mod     .  color',
        'mod     .  like',
        'mod     .  part',
        'mod     >> part',
        'color   >> mod',
        'like    >> mod',
        'mod     >> subpart >> part',
        # 'subpart << color',
        # 'color   >> part',
        # 'color   >> part > subpart',
    ],
)
