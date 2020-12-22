"""Base matcher object."""

from traiter.pylib.matcher import SpacyMatcher

from .body_part import BODY_PART
from .color import COLOR
from .header import HEADER
from .hind_wing_length import HIND_WING_LENGTH
from .month_range import MONTH_RANGE
from .range import RANGE
from .sci_name import SCI_NAME
from .sex import SEX
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR
from ..pylib.actions import text_action
from ..pylib.util import GROUP_STEP, HEADER_STEP, TERMS, TRAIT_STEP

MATCHERS = [
    BODY_PART, COLOR, HEADER, HIND_WING_LENGTH, MONTH_RANGE, RANGE, SCI_NAME, SEX,
    TOTAL_LENGTH, VERNACULAR,
]


class Matcher(SpacyMatcher):
    """Base matcher object."""

    def __init__(self, nlp):
        super().__init__(nlp)

        self.add_terms(TERMS, on_match=text_action)
        self.add_patterns(MATCHERS, GROUP_STEP)
        self.add_patterns(MATCHERS, TRAIT_STEP)
        self.add_patterns(MATCHERS, HEADER_STEP)
