from traiter.patterns.dependency_patterns import DependencyPatterns
from traiter.old_pipes.dependency import LINK_NEAREST

COLOR_LIKE_LINKER = DependencyPatterns(
    'color_like_linker',
    on_match={
        'func': LINK_NEAREST,
        'kwargs': {'anchor': 'color_like'}
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
        'part    .  like',
        'subpart .  like',
        'color   .  like',
        'like    .  mod',
        'like    .  color',
        'mod     .  like',
        'like    .  part',
        'like    >> part',
        'color   >> like',
        'like    >> like',
        'like    >> subpart >> part',
        # 'subpart << color',
        # 'color   >> part',
        # 'color   >> part > subpart',
    ],
)
