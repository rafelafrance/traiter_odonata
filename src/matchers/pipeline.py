"""Build the NLP pipeline."""

from functools import partial

from traiter.actions import text_action
from traiter.matchers.rule import Rule
from traiter.matchers.term import Term
from traiter.pipeline import SpacyPipeline
from traiter.sentencizer import Sentencizer
from traiter.to_entities import ToEntities
from traiter.util import TERM_STEP

from .body_part import BODY_PART
from .body_part_linker import BODY_PART_LINKER
from .color import COLOR
from .header import HEADER
from .hind_wing_length import HIND_WING_LENGTH
from .month_range import MONTH_RANGE
from .range import RANGE
from .sci_name import SCI_NAME
from .sex import SEX
from .sex_linker import sex_linker
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR
from ..pylib.consts import ABBREVS, GROUP_STEP, HEADER_STEP, PART_STEP, REPLACE, \
    SEX_STEP, TERMS, TRAIT_STEP

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

        Term.add_pipes(self.nlp, TERMS, before='parser',
                       action=partial(text_action, replace=REPLACE))
        Sentencizer.add_pipe(self.nlp, ABBREVS, headings='heading', before='parser')
        Rule.add_pipe(self.nlp, MATCHERS, GROUP_STEP, before='parser')
        Rule.add_pipe(self.nlp, MATCHERS, TRAIT_STEP, before='parser')
        Rule.add_pipe(self.nlp, MATCHERS, HEADER_STEP, before='parser')
        Rule.add_pipe(self.nlp, MATCHERS, PART_STEP, before='parser')
        ToEntities.add_pipe(self.nlp, entities2keep, token2entity, before='parser')
        self.nlp.add_pipe(sex_linker, name=SEX_STEP)
