"""Link sexual dimorphism notations to traits."""

from traiter.dependency_compiler import DependencyCompiler
from traiter.pipes.dependency import NEAREST_ANCHOR

TRAITS = """ color color_mod body_part body_part_loc """.split()
LINKERS = """ prep conj cc """.split()

COMPILE = DependencyCompiler({
    'sex_diff': {'ENT_TYPE': 'sex_diff'},
    'trait': {'ENT_TYPE': {'IN': TRAITS}},
    'linker': {'DEP': {'IN': LINKERS}},
    'verb': {'POS': {'IN': ['VERB']}},
})

SEX_DIFF_LINKER = [
    {
        'label': 'sex_diff_linker',
        'on_match': {
            'func': NEAREST_ANCHOR,
            'kwargs': {'anchor': 'sex_diff', 'exclude': ''}
        },
        'patterns': COMPILE(
            'sex_diff . trait',
            'sex_diff . trait >> trait',
            'sex_diff >> trait',
            'sex_diff << trait',
            'sex_diff <  linker << trait',
            'sex_diff >  linker >> trait',
            'sex_diff <  linker < verb > trait',
        ),
    },
]
