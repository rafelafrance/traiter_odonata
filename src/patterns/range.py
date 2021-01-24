"""Range patterns."""

import re

import spacy
from traiter.consts import DASH_RE, FLOAT_RE, FLOAT_TOKEN_RE
from traiter.util import to_positive_float

RANGE_ACTION = 'range.v1'


@spacy.registry.misc(RANGE_ACTION)
def range_(ent):
    """Build the range parts for other patterns."""
    values = re.findall(FLOAT_RE, ent.text)
    data = {f: to_positive_float(v) for f, v in zip(['low', 'high'], values)}
    ent._.data = data


RANGE = [
    {
        'label': 'range',
        'patterns': [
            [
                {'TEXT': {'REGEX': f'^{FLOAT_RE}{DASH_RE}{FLOAT_RE}$'}},
            ],
        ],
    },
]
