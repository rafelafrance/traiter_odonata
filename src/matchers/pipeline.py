"""Build the NLP pipeline."""

from functools import partial

from traiter.actions import Actions, text_action
from traiter.patterns import Patterns
from traiter.pipeline import SpacyPipeline
from traiter.pipes.action_pipe import ActionPipe
from traiter.pipes.entity_ruler_pipe import EntityRulerPipe
from traiter.pipes.retokenize_ruler_pipe import RetokenizeRulerPipe
from traiter.pipes.sentencizer_pipe import SentencizerPipe

from .body_part import BODY_PART
from .body_part_linker import BODY_PART_LINKER
from .color import COLOR
from .doc_heading import DOC_HEADING
from .hind_wing_length import HIND_WING_LENGTH
from .range import RANGE
from .sci_name import SCI_NAME
from .sex import SEX
from .total_length import TOTAL_LENGTH
from .vernacular import VERNACULAR
from ..pylib.consts import ABBREVS, REPLACE, TERMS

ENTITY = [BODY_PART, BODY_PART_LINKER, COLOR, HIND_WING_LENGTH,
          SCI_NAME, SEX, TOTAL_LENGTH, VERNACULAR]
RETOKENIZE = [DOC_HEADING, RANGE]
MATCHERS = RETOKENIZE + ENTITY


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    def __init__(self):
        super().__init__()
        self.nlp.disable_pipes(['ner'])

        retokenize = Patterns.from_terms(TERMS)
        retokenize += Patterns.from_matchers(*RETOKENIZE)

        entities = Patterns.from_matchers(*ENTITY)

        default = partial(text_action, replace=REPLACE)
        actions = Actions.from_terms(TERMS, default=default)
        actions += Actions.from_matchers(*MATCHERS)

        RetokenizeRulerPipe.add_pipe(self.nlp, retokenize, name='step1')
        EntityRulerPipe.add_pipe(self.nlp, entities, name='step2')
        ActionPipe.add_pipe(self.nlp, actions)
        SentencizerPipe.add_pipe(self.nlp, ABBREVS, headings='heading')
