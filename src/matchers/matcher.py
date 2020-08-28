"""Base matcher object."""

from traiter.trait_matcher import TraitMatcher

from .flight_period import FLIGHT_PERIOD
from .header import HEADER
from .month_time import MONTH_TIME
from .range import RANGE
from .scientific_name import SCI_NAME
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR
from ..pylib.terms import TERMS
from ..pylib.util import GROUP_STEP, HEADER_STEP, TRAIT_STEP

MATCHERS = (
    FLIGHT_PERIOD, HEADER, MONTH_TIME, RANGE,
    SCI_NAME, TOTAL_LENGTH, VERNACULAR,
)


class Matcher(TraitMatcher):
    """Base matcher object."""

    def __init__(self, nlp):
        super().__init__(nlp)

        terms = TERMS
        self.add_terms(terms)

        groups = TraitMatcher.step_rules(MATCHERS, GROUP_STEP)
        traits = TraitMatcher.step_rules(MATCHERS, TRAIT_STEP)
        headers = TraitMatcher.step_rules(MATCHERS, HEADER_STEP)

        self.add_patterns(groups, GROUP_STEP)
        self.add_patterns(traits, TRAIT_STEP)
        self.add_patterns(headers, HEADER_STEP)
