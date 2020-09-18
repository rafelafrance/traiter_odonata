"""Build the NLP pipeline."""

from traiter.spacy_nlp.pipeline import SpacyPipeline
from traiter.spacy_nlp.sentencizer import SpacySentencizer

from ..spacy_matchers.consts import ABBREVS, HEADER_STEP, TRAIT_STEP
from ..spacy_matchers.matcher import Matcher


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    steps2link = {TRAIT_STEP, HEADER_STEP}

    def __init__(self):
        super().__init__()

        self.nlp.disable_pipes(['ner'])

        self.matcher = Matcher(self.nlp)
        # self.linker = LinkMatcher(self.nlp)

        self.matcher = Matcher(self.nlp)
        sentencizer = SpacySentencizer(ABBREVS)

        self.nlp.add_pipe(sentencizer, before='parser')
        self.nlp.add_pipe(self.matcher, last=True)
        # self.nlp.add_pipe(self.linker, last=True, name=LINK_STEP)


PIPELINE = Pipeline()
