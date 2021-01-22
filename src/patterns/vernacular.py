"""Get common names."""

import re

import spacy

from traiter.consts import SLASH

SLASH_RE = re.compile(fr'{"|".join(SLASH)}')

VERNACULAR = [
    {
        'label': 'vernacular',
        'on_match': 'vernacular.v1',
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


@spacy.registry.misc(VERNACULAR[0]['on_match'])
def vernacular(ent):
    """Enrich the match."""
    name = [t.lower_ for t in ent if t._.label_cache == 'common_name'][0]
    first = SLASH_RE.split(ent.text)
    if len(first) > 1:
        name = [name, f'{first[0]} {" ".join(name.split()[1:])}']
    ent._.data = {'vernacular': name}
