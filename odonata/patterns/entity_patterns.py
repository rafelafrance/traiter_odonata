"""These patterns are used during the entity building phase."""

from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.patterns.term_patterns import RANGE_ACTION

HIND_WING_LENGTH = MatcherPatterns(
    'hind_wing_length',
    on_match=RANGE_ACTION,
    patterns=[
        [{'ENT_TYPE': 'hind_wing_length_key'}, {'ENT_TYPE': 'range'}]
    ]
)

TOTAL_LENGTH = MatcherPatterns(
    'total_length', on_match=RANGE_ACTION,
    patterns=[
        [{'ENT_TYPE': 'total_length_key'}, {'ENT_TYPE': 'range'}]
    ]
)
