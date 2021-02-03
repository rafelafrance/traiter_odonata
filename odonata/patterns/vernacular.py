"""Get common names."""

import re

import spacy

from traiter.const import SLASH

from odonata.pylib.token import COMPILE

SLASH_RE = re.compile(fr'{"|".join(SLASH)}')

VERNACULAR = [
    {
        'label': 'vernacular',
        'on_match': 'vernacular.v1',
        'patterns': COMPILE.to_patterns(
            None,
            'common_name',
            'a-z+ / common_name',
        ),
    },
]


@spacy.registry.misc(VERNACULAR[0]['on_match'])
def vernacular(ent):
    """Enrich the match."""
    name = [t.lower_ for t in ent if t._.cached_label == 'common_name'][0]
    first = SLASH_RE.split(ent.text)
    if len(first) > 1:
        name = [name, f'{first[0]} {" ".join(name.split()[1:])}']
    ent._.data = {'vernacular': name}
