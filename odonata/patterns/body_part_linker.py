"""Link traits to body parts."""

from traiter.patterns.dependency_patterns import DependencyPatterns
from traiter.pipes.dependency import NEAREST_ANCHOR

TRAITS = """ color color_mod """.split()
LINKERS = """ prep conj cc """.split()

BODY_PART_LINKER = DependencyPatterns(
    'body_part_linker',
    on_match={
        'func': NEAREST_ANCHOR,
        'kwargs': {'anchor': 'body_part', 'exclude': ''}
    },
    decoder={
        'body_part': {'ENT_TYPE': 'body_part'},
        'trait': {'ENT_TYPE': {'IN': TRAITS}},
        'linker': {'DEP': {'IN': LINKERS}},
        'verb': {'POS': 'VERB'},
    },
    patterns=[
        'body_part .  trait',
        'body_part .  trait >> trait',
        'body_part >> trait',
        'body_part << trait',
        'body_part <  linker << trait',
        'body_part >  linker >> trait',
        'body_part <  linker <  verb > trait',
    ],
)
