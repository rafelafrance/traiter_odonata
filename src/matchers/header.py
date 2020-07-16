"""Get scientific names."""

from ..pylib.terms import REPLACE
from .shared import OPEN, CLOSE


def header(span):
    """Enrich the match."""
    data = {}
    for token in span:
        if token.ent_type_ == 'sci_name':
            data['sci_name'] = REPLACE[token.text.lower()]
        elif token.ent_type_ == 'vernacular':
            data['vernacular'] = token.text
    return data


HEADER = {
    'name': 'header',
    'headers': [
        {
            'label': 'header',
            'on_match': header,
            'patterns': [
                [
                    {'ENT_TYPE': 'sci_name'},
                    {'TEXT': {'IN': OPEN}},
                    {'ENT_TYPE': 'vernacular'},
                    {'TEXT': {'IN': CLOSE}},
                ],
            ],
        },
    ],
}
