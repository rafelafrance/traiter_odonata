"""Base matcher object."""

from traiter.spacy_nlp.matcher import SpacyMatcher

from ..pylib.util import GROUP_STEP, HEADER_STEP, TERMS, TRAIT_STEP
from .flight_period import FLIGHT_PERIOD
from .header import HEADER
from .month_time import MONTH_TIME
from .range import RANGE
from .scientific_name import SCI_NAME
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR

MATCHERS = [
    FLIGHT_PERIOD, HEADER, MONTH_TIME, RANGE,
    SCI_NAME, TOTAL_LENGTH, VERNACULAR,
]


class Matcher(SpacyMatcher):
    """Base matcher object."""

    def __init__(self, nlp):
        super().__init__(nlp)

        self.add_terms(TERMS)
        self.add_patterns(MATCHERS, GROUP_STEP)
        self.add_patterns(MATCHERS, TRAIT_STEP)
        self.add_patterns(MATCHERS, HEADER_STEP)
