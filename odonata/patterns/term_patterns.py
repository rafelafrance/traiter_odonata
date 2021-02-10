"""These patterns are used during the term building phase."""

import re

from spacy import registry
from traiter.const import DASH_RE, FLOAT_RE
from traiter.patterns.matcher_patterns import MatcherPatterns
from traiter.util import to_positive_float

RANGE_ACTION = 'range.v1'

SEGMENTS = MatcherPatterns(
    'segments',
    patterns=[[{'LOWER': {'REGEX': fr'^s\d+{DASH_RE}\d+$'}}]])

RANGE = MatcherPatterns(
    'range',
    patterns=[[{'TEXT': {'REGEX': f'^{FLOAT_RE}{DASH_RE}{FLOAT_RE}$'}}]],
)

DOC_HEADING = MatcherPatterns(
    'doc_heading',
    patterns=[
        [{'TEXT': 'Description'}],
        [{'TEXT': 'Flight'}, {'TEXT': 'Season'}],
        [{'TEXT': 'Identification'}],
        [{'TEXT': 'Natural'}, {'TEXT': 'History'}],
    ],
)


@registry.misc(RANGE_ACTION)
def range_(ent):
    """Build the range parts for other patterns."""
    values = re.findall(FLOAT_RE, ent.text)
    ent._.data = {f: to_positive_float(v) for f, v in zip(['low', 'high'], values)}
