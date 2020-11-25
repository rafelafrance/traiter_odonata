"""Base matcher object."""

from traiter.spacy_nlp.matcher import SpacyMatcher

from .body_part import BODY_PART
from .color import COLOR
from .flight_period import FLIGHT_PERIOD
from .header import HEADER
from .hind_wing_length import HIND_WING_LENGTH
from .month_time import MONTH_TIME
from .range import RANGE
from .scientific_name import SCI_NAME
from .sex import SEX
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR
from ..pylib.util import GROUP_STEP, HEADER_STEP, TRAIT_STEP

FRASER_MATCHERS = [
    FLIGHT_PERIOD, HEADER, MONTH_TIME, RANGE, SCI_NAME, TOTAL_LENGTH, VERNACULAR]

PAULSON_MATCHERS = [
    BODY_PART, COLOR, HEADER, HIND_WING_LENGTH, RANGE, SCI_NAME, SEX, TOTAL_LENGTH,
    VERNACULAR]


class RuleMatcher(SpacyMatcher):
    """Base matcher object."""

    def __init__(self, nlp, matchers):
        super().__init__(nlp)

        self.add_patterns(matchers, GROUP_STEP)
        self.add_patterns(matchers, TRAIT_STEP)
        self.add_patterns(matchers, HEADER_STEP)
