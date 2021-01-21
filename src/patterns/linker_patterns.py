"""Handle common linker patterns."""

from collections import defaultdict

TRAITS = ['color', 'color_mod']
LINKERS = ['prep', 'conj', 'cc']


def linker(_, doc, idx, matches, key):
    """Link traits to the root trait trait."""
    match_ents = defaultdict(list)
    for ent in doc.ents:
        for k, i in enumerate(matches[idx][1]):
            if ent.start <= i < ent.end:
                match_ents[ent].append(k)
                break
    match_ents = dict(sorted(match_ents.items(), key=lambda x: min(x[1])))
    root, *others = match_ents.keys()
    root = root._.data[key]
    for ent in others:
        ent._.data[key] = root


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
