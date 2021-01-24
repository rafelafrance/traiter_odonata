"""Handle common linker patterns."""

TRAITS = ['color', 'color_mod']
LINKERS = ['prep', 'conj', 'cc']


def linker_patterns(root, traits=None, linkers=None):
    """Build common linker patterns."""
    traits = traits if traits else TRAITS
    linkers = linkers if linkers else LINKERS
    return [
        # root . trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '.',
                'RIGHT_ID': 'trait1',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root . trait > trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '.',
                'RIGHT_ID': 'trait1',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
            {
                'LEFT_ID': 'trait1',
                'REL_OP': '>',
                'RIGHT_ID': 'trait2',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root > trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '>',
                'RIGHT_ID': 'trait',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root < trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '<',
                'RIGHT_ID': 'trait',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root < linker < trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '<',
                'RIGHT_ID': 'linker',
                'RIGHT_ATTRS': {'DEP': {'IN': linkers}},
            },
            {
                'LEFT_ID': 'linker',
                'REL_OP': '<',
                'RIGHT_ID': 'trait1',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root < linker < trait < trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '<',
                'RIGHT_ID': 'linker',
                'RIGHT_ATTRS': {'DEP': {'IN': linkers}},
            },
            {
                'LEFT_ID': 'linker',
                'REL_OP': '<',
                'RIGHT_ID': 'trait1',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
            {
                'LEFT_ID': 'trait1',
                'REL_OP': '<',
                'RIGHT_ID': 'trait2',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root > linker > trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '>',
                'RIGHT_ID': 'linker',
                'RIGHT_ATTRS': {'DEP': {'IN': linkers}},
            },
            {
                'LEFT_ID': 'linker',
                'REL_OP': '>',
                'RIGHT_ID': 'trait1',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root > linker > trait > trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '>',
                'RIGHT_ID': 'linker',
                'RIGHT_ATTRS': {'DEP': {'IN': linkers}},
            },
            {
                'LEFT_ID': 'linker',
                'REL_OP': '>',
                'RIGHT_ID': 'trait1',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
            {
                'LEFT_ID': 'trait1',
                'REL_OP': '>',
                'RIGHT_ID': 'trait2',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
        # root < linker < verb < trait
        [
            {
                'RIGHT_ID': f'{root}',
                'RIGHT_ATTRS': {'ENT_TYPE': f'{root}'},
            },
            {
                'LEFT_ID': f'{root}',
                'REL_OP': '<',
                'RIGHT_ID': 'linker',
                'RIGHT_ATTRS': {'DEP': {'IN': linkers}},
            },
            {
                'LEFT_ID': 'linker',
                'REL_OP': '<',
                'RIGHT_ID': 'verb',
                'RIGHT_ATTRS': {'POS': {'IN': ['VERB']}},
            },
            {
                'LEFT_ID': 'verb',
                'REL_OP': '>',
                'RIGHT_ID': 'trait1',
                'RIGHT_ATTRS': {'ENT_TYPE': {'IN': traits}},
            },
        ],
    ]
