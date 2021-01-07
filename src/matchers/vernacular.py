"""Get common names."""

import re

from ..pylib.consts import GROUP_STEP, SLASH


SLASH_RE = re.compile(fr'{"|".join(SLASH)}')


def vernacular(span):
    """Enrich the match."""
    name = [t.lower_ for t in span if t.ent_type_ == 'common_name'][0]
    first = SLASH_RE.split(span.text)
    if len(first) > 1:
        name = [name, f'{first[0]} {" ".join(name.split()[1:])}']
    return {'vernacular': name}


VERNACULAR = {
    GROUP_STEP: [
        {
            'label': 'vernacular',
            'on_match': vernacular,
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
    ],
}
