"""Range patterns."""

import re

from traiter.const import DASH_RE, FLOAT_RE
from traiter.patterns.matcher_patterns import MatcherPatterns
from traiter.util import to_positive_float

RANGE = MatcherPatterns(
    'range',
    patterns=[
        [
            {'TEXT': {'REGEX': f'^{FLOAT_RE}{DASH_RE}{FLOAT_RE}$'}},
        ],
    ],
)


def range_(ent):
    """Build the range parts for other patterns."""
    values = re.findall(FLOAT_RE, ent.text)
    data = {f: to_positive_float(v) for f, v in zip(['low', 'high'], values)}
    ent._.data = data
