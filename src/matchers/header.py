"""Get scientific names."""

import re

from ..pylib.terms import REPLACE
from .shared import OPEN, CLOSE, SLASH


def header(span):
    """Enrich the match."""
    data = {'trait': 'header', 'vernacular': ''}
    for token in span:
        if token.ent_type_ == 'sci_name':
            data['sci_name'] = REPLACE[token.text.lower()]
        elif token.ent_type_ == 'species':
            data['sci_name'] += '/' + token.lower_
        elif token.ent_type_ == 'vernacular':
            data['vernacular'] += token.text
        elif re.match(r'^[a-z]+$', token.lower_):
            data['vernacular'] += token.text + '/'
    return data


def invalid_species(span):
    """Get header of species that are not in the ITIS database."""
    data = {'_relabel': 'header'}
    sci_name = []
    for token in span:
        if token.ent_type_ == 'vernacular':
            data['vernacular'] = token.text
        elif re.match(r'^[a-z]+$', token.lower_):
            sci_name.append(token.text)
    data['sci_name'] = ' '.join(sci_name)

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
                    {'IS_SPACE': True, 'OP': '?'},
                    {'TEXT': {'IN': OPEN}},
                    {'ENT_TYPE': 'vernacular'},
                    {'TEXT': {'IN': CLOSE}},
                ],
                [
                    {'ENT_TYPE': 'sci_name'},
                    {'TEXT': {'IN': SLASH}},
                    {'ENT_TYPE': 'species'},
                    {'IS_SPACE': True, 'OP': '?'},
                    {'TEXT': {'IN': OPEN}},
                    {'IS_ALPHA': True},
                    {'TEXT': {'IN': SLASH}},
                    {'ENT_TYPE': 'vernacular'},
                    {'TEXT': {'IN': CLOSE}},
                ],
            ],
        },
        {
            'label': 'invalid_species',
            'on_match': invalid_species,
            'patterns': [
                [
                    {'IS_ALPHA': True},
                    {'IS_ALPHA': True},
                    {'IS_SPACE': True, 'OP': '?'},
                    {'TEXT': {'IN': OPEN}},
                    {'ENT_TYPE': 'vernacular'},
                    {'TEXT': {'IN': CLOSE}},
                ],
            ],
        },
    ],
}
