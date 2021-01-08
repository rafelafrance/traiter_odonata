"""Build the NLP pipeline."""

from traiter.pipeline import SpacyPipeline
from traiter.rule_matcher import RuleMatcher
from traiter.sentencizer import Sentencizer
from traiter.term_matcher import TermMatcher
from traiter.to_entities import ToEntities
from traiter.util import TERM_STEP
from ..pylib.actions import text_action

from .body_part import BODY_PART
from .body_part_linker import BODY_PART_LINKER
from .color import COLOR
from .header import HEADER
from .hind_wing_length import HIND_WING_LENGTH
from .month_range import MONTH_RANGE
from .range import RANGE
from .sci_name import SCI_NAME
from .sex import SEX
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR
from ..pylib.consts import ABBREVS, GROUP_STEP, HEADER_STEP, LINK_STEP, TERMS, \
    TRAIT_STEP

MATCHERS = [
    BODY_PART, BODY_PART_LINKER, COLOR, HEADER, HIND_WING_LENGTH, MONTH_RANGE, RANGE,
    SCI_NAME, SEX, TOTAL_LENGTH, VERNACULAR,
]


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    def __init__(self):
        super().__init__()

        self.nlp.disable_pipes(['ner'])

        token2entity = {TERM_STEP, GROUP_STEP, TRAIT_STEP}
        entities2keep = {TERM_STEP, GROUP_STEP, TRAIT_STEP}

        TermMatcher.add_pipes(self.nlp, TERMS, before='parser', action=text_action)
        RuleMatcher.add_pipe(self.nlp, MATCHERS, GROUP_STEP, before='parser')
        RuleMatcher.add_pipe(self.nlp, MATCHERS, TRAIT_STEP, before='parser')
        RuleMatcher.add_pipe(self.nlp, MATCHERS, HEADER_STEP, before='parser')
        RuleMatcher.add_pipe(self.nlp, MATCHERS, LINK_STEP, before='parser')
        ToEntities.add_pipe(self.nlp, entities2keep, token2entity, before='parser')
        Sentencizer.add_pipe(self.nlp, ABBREVS, headings='heading', before='parser')
