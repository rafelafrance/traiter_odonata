"""Base matcher object."""

from traiter.spacy_nlp.matcher import SpacyMatcher

from .body_part import BODY_PART
from .color import COLOR
from .month_range import MONTH_RANGE
from .range import RANGE
from .scientific_name import SCI_NAME
from .sex import SEX
from .vernacular import VERNACULAR
from ..pylib.actions import text_action
from ..pylib.util import GROUP_STEP, TERMS

FRASER_MATCHERS = [MONTH_RANGE, RANGE, SCI_NAME, VERNACULAR]

PAULSON_MATCHERS = [BODY_PART, COLOR, RANGE, SCI_NAME, SEX, VERNACULAR]


class Matcher(SpacyMatcher):
    """Base matcher object."""

    def __init__(self, nlp, matchers):
        super().__init__(nlp)

        self.add_terms(TERMS, on_match=text_action)
        self.add_patterns(matchers, GROUP_STEP)
