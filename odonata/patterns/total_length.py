"""Get total the total length."""

from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.patterns.range import range_

TOTAL_LENGTH = MatcherPatterns(
    'total_length',
    on_match=range_,
    patterns=[
        [{'ENT_TYPE': 'total_length_key'}, {'ENT_TYPE': 'range'}]
    ]
)
