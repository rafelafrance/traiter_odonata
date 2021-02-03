"""Link traits to body parts."""

from traiter.pipes.dependency import NEAREST_ANCHOR

from odonata.pylib.token import COMPILE

TRAITS = """ color color_mod """.split()
LINKERS = """ prep conj cc """.split()

MAP = {
    'body_part': {'ENT_TYPE': 'body_part'},
    'trait': {'ENT_TYPE': {'IN': TRAITS}},
    'linker': {'DEP': {'IN': LINKERS}},
    'verb': {'POS': {'IN': ['VERB']}},
}

BODY_PART_LINKER = [
    {
        'label': 'body_part_linker',
        'on_match': {
            'func': NEAREST_ANCHOR,
            'kwargs': {'anchor': 'body_part', 'exclude': ''}
        },
        'patterns': COMPILE.to_dependencies(
            MAP,
            'body_part .  trait',
            'body_part .  trait >> trait',
            'body_part >> trait',
            'body_part << trait',
            'body_part <  linker << trait',
            'body_part >  linker >> trait',
            'body_part <  linker <  verb > trait',
        ),

    },
]
