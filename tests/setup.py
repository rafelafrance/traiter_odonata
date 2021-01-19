"""Setup for all tests."""

from typing import Dict, List

from spacy import displacy
from traiter.util import shorten

from src.pylib.pipeline import pipeline
# from src.pylib.consts import SEX_STEP

NLP = pipeline()  # Singleton for testing
# NLP.remove_pipe(SEX_STEP)


def test_traits(text: str) -> List[Dict]:
    """Find entities in the doc."""
    text = shorten(text)
    doc = NLP(text)
    displacy.serve(doc)
    return doc
