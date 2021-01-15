"""Range patterns."""

import re

from traiter.util import to_positive_float

from ..pylib.consts import DASH

NUMBER = r'\d+\.?\d*'
NUMBER_PAT = f'^{NUMBER}$'


def range_(ent):
    """Build the range parts for other matchers."""
    values = re.findall(NUMBER, ent.text)
    data = {f: to_positive_float(v) for f, v in zip(['low', 'high'], values)}
    ent._.data = data


RANGE = [
    {
        'label': 'range',
        'patterns': [
            [
                {'TEXT': {'REGEX': NUMBER_PAT}},
                {'TEXT': {'IN': DASH}},
                {'TEXT': {'REGEX': NUMBER_PAT}},
            ],
        ],
    },
]
