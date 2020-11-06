"""Build the NLP pipeline."""

from traiter.spacy_nlp.pipeline import SpacyPipeline
from traiter.spacy_nlp.sentencizer import SpacySentencizer

from src.pylib.util import ABBREVS, HEADER_STEP, TRAIT_STEP
from src.matchers.matcher import Matcher, FRASER_MATCHERS


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    token2entity = {TRAIT_STEP, HEADER_STEP}

    def __init__(self, matchers):
        super().__init__()

        self.nlp.disable_pipes(['ner'])

        self.matcher = Matcher(self.nlp, matchers)
        sentencizer = SpacySentencizer(ABBREVS)

        self.nlp.add_pipe(sentencizer, before='parser')
        self.nlp.add_pipe(self.matcher, last=True)


PIPELINE = Pipeline(FRASER_MATCHERS)  # TODO
