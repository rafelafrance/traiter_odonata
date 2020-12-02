"""Build the NLP pipeline."""

from traiter.pylib.pipeline import SpacyPipeline
from traiter.pylib.sentencizer import SpacySentencizer

from src.pylib.util import ABBREVS
from .matcher import Matcher


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    def __init__(self):
        super().__init__()

        self.nlp.disable_pipes(['ner'])

        matcher = Matcher(self.nlp)
        sentencizer = SpacySentencizer(ABBREVS, headings='heading')

        self.nlp.add_pipe(matcher, before='parser')
        self.nlp.add_pipe(sentencizer, before='parser')
