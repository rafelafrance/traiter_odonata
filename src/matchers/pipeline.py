"""Build the NLP pipeline."""

from traiter.pylib.pipeline import SpacyPipeline
from traiter.pylib.sentencizer import SpacySentencizer
from traiter.pylib.to_entities import ToEntities

from src.pylib.util import ABBREVS, GROUP_STEP, TERM_STEP, TRAIT_STEP
from .matcher import Matcher


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    token2entity = {TERM_STEP, GROUP_STEP, TRAIT_STEP}
    entities2keep = {TERM_STEP, GROUP_STEP, TRAIT_STEP}

    def __init__(self):
        super().__init__()

        self.nlp.disable_pipes(['ner'])

        matcher = Matcher(self.nlp)
        sentencizer = SpacySentencizer(ABBREVS, headings='heading')
        to_entities = ToEntities(self.entities2keep, self.token2entity)

        self.nlp.add_pipe(matcher, before='parser')
        self.nlp.add_pipe(to_entities, before='parser')
        self.nlp.add_pipe(sentencizer, before='parser')
