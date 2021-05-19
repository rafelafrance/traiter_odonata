"""Parse the total length notation."""

from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.patterns.term_patterns import RANGE_ACTION

TOTAL_LENGTH = MatcherPatterns(
    'total_length',
    on_match=RANGE_ACTION,
    patterns=[
        [{'ENT_TYPE': 'total_length_key'}, {'ENT_TYPE': 'range'}]
    ]
)
