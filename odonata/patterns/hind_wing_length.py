"""Get total the hind wing length."""

from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.patterns.range import range_

HIND_WING_LENGTH = MatcherPatterns(
    'hind_wing_length',
    on_match=range_,
    patterns=[
        [{'ENT_TYPE': 'hind_wing_length_key'}, {'ENT_TYPE': 'range'}]
    ]
)
