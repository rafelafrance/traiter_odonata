"""Build the NLP pipeline."""

from traiter.spacy_nlp.pipeline import SpacyPipeline
from traiter.spacy_nlp.sentencizer import SpacySentencizer
from traiter.spacy_nlp.to_entities import ToEntities

from src.pylib.util import ABBREVS, GROUP_STEP, HEADER_STEP, TERM_STEP, TRAIT_STEP
from .matcher import Matcher


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    token2entity = {TERM_STEP, GROUP_STEP, TRAIT_STEP, HEADER_STEP}

    def __init__(self, matchers):
        super().__init__()

        self.nlp.disable_pipes(['ner'])

        self.matcher = Matcher(self.nlp, matchers)

        sentencizer = SpacySentencizer(ABBREVS, headings='heading')
        to_entities = ToEntities(token2entity=self.token2entity)

        self.nlp.add_pipe(self.matcher, before='parser')
        self.nlp.add_pipe(sentencizer, before='parser')
        self.nlp.add_pipe(to_entities, last=True)
