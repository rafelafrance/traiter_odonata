"""Get document headers."""

from traiter.patterns.matcher_patterns import MatcherPatterns

DOC_HEADING = MatcherPatterns(
    'doc_heading',
    patterns=[
        [{'TEXT': 'Description'}],
        [{'TEXT': 'Flight'}, {'TEXT': 'Season'}],
        [{'TEXT': 'Identification'}],
        [{'TEXT': 'Natural'}, {'TEXT': 'History'}],
    ],
)
