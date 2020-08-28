"""Shared range patterns."""

import re

from traiter.pylib.util import to_positive_float

from .shared import DASH, NUMBER
from ..pylib.util import GROUP_STEP


def range_(span):
    """Build the range parts."""
    values = [t.text for t in span if re.match(NUMBER, t.text)]
    return {f: to_positive_float(v) for f, v in zip(['low', 'high'], values)}


RANGE = {
    GROUP_STEP: [
        {
            'label': 'range',
            'on_match': range_,
            'patterns': [
                [
                    {'TEXT': {'REGEX': NUMBER}},
                    {'TEXT': {'IN': DASH}},
                    {'TEXT': {'REGEX': NUMBER}},
                ],
            ],
        },
    ],
}