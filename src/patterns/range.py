"""Range patterns."""

import re

import spacy
from traiter.consts import DASH_RE
from traiter.util import to_positive_float

NUMBER = r'\d+\.?\d*'
NUMBER_PAT = f'^{NUMBER}$'
RANGE_PAT = f'^{NUMBER}({DASH_RE}){NUMBER}$'

RANGE_ACTION = 'range.v1'


@spacy.registry.misc(RANGE_ACTION)
def range_(ent):
    """Build the range parts for other patterns."""
    values = re.findall(NUMBER, ent.text)
    data = {f: to_positive_float(v) for f, v in zip(['low', 'high'], values)}
    ent._.data = data


RANGE = [
    {
        'label': 'range',
        'patterns': [
            # [
            #     {'TEXT': {'REGEX': NUMBER_PAT}},
            #     {'TEXT': {'IN': DASH}},
            #     {'TEXT': {'REGEX': NUMBER_PAT}},
            # ],
            [
                {'TEXT': {'REGEX': RANGE_PAT}},
            ],
        ],
    },
]
