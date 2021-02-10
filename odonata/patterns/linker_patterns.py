"""These patterns are used to link traits."""

from traiter.patterns.dependency_patterns import DependencyPatterns
from traiter.pipes.dependency import NEAREST_ANCHOR

BODY_PART_TRAITS = """ color color_mod """.split()
SEX_DIFF_TRAITS = """ color color_mod body_part body_part_loc """.split()
LINKERS = """ prep conj cc """.split()

BODY_PART_LINKER = DependencyPatterns(
    'body_part_linker',
    on_match={
        'func': NEAREST_ANCHOR,
        'kwargs': {'anchor': 'body_part', 'exclude': ''}
    },
    decoder={
        'body_part': {'ENT_TYPE': 'body_part'},
        'trait': {'ENT_TYPE': {'IN': BODY_PART_TRAITS}},
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

SEX_DIFF_LINKER = DependencyPatterns(
    'sex_diff_linker',
    on_match={
        'func': NEAREST_ANCHOR,
        'kwargs': {'anchor': 'sex_diff', 'exclude': ''}
    },
    decoder={
        'sex_diff': {'ENT_TYPE': 'sex_diff'},
        'trait': {'ENT_TYPE': {'IN': SEX_DIFF_TRAITS}},
        'linker': {'DEP': {'IN': LINKERS}},
        'verb': {'POS': {'IN': ['VERB']}},
    },
    patterns=[
        'sex_diff . trait',
        'sex_diff . trait >> trait',
        'sex_diff >> trait',
        'sex_diff << trait',
        'sex_diff <  linker << trait',
        'sex_diff >  linker >> trait',
        'sex_diff <  linker < verb > trait',
    ],
)
