"""Base matcher object."""

from traiter.spacy_nlp.matcher import SpacyMatcher

from ..pylib.util import GROUP_STEP, HEADER_STEP, TERMS, TRAIT_STEP
from .flight_period import FLIGHT_PERIOD
from .header import HEADER
from .hind_wing_length import HIND_WING_LENGTH
from .month_time import MONTH_TIME
from .range import RANGE
from .scientific_name import SCI_NAME
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR

FRASER_MATCHERS = [
    FLIGHT_PERIOD, HEADER, MONTH_TIME, RANGE,
    SCI_NAME, TOTAL_LENGTH, VERNACULAR]

PAULSON_MATCHERS = [
    HEADER, HIND_WING_LENGTH, RANGE, SCI_NAME, TOTAL_LENGTH, VERNACULAR]


class Matcher(SpacyMatcher):
    """Base matcher object."""

    def __init__(self, nlp, matchers):
        super().__init__(nlp)

        self.add_terms(TERMS)
        self.add_patterns(matchers, GROUP_STEP)
        self.add_patterns(matchers, TRAIT_STEP)
        self.add_patterns(matchers, HEADER_STEP)
