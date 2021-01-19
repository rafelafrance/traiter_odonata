"""Get common names."""

import re

from ..pylib.consts import SLASH

SLASH_RE = re.compile(fr'{"|".join(SLASH)}')


def vernacular(ent):
    """Enrich the match."""
    name = [t.lower_ for t in ent if t._.label_cache == 'common_name'][0]
    first = SLASH_RE.split(ent.text)
    if len(first) > 1:
        name = [name, f'{first[0]} {" ".join(name.split()[1:])}']
    ent._.data = {'vernacular': name}


VERNACULAR = [
    {
        'label': 'vernacular',
        'action': vernacular,
        'patterns': [
            [
                {'ENT_TYPE': 'common_name'},
            ],
            [
                {'IS_ALPHA': True},
                {'TEXT': {'IN': SLASH}},
                {'ENT_TYPE': 'common_name'},
            ],
        ],
    },
]
