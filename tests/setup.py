"""Setup for all tests."""

from typing import Dict, List

from traiter.util import shorten

from src.matchers.pipeline import Pipeline
from src.pylib.consts import SEX_STEP

TEST_PIPELINE = Pipeline()  # Singleton for testing
# TEST_PIPELINE.nlp.remove_pipe(SEX_STEP)


def test_traits(text: str) -> List[Dict]:
    """Find entities in the doc."""
    text = shorten(text)
    return TEST_PIPELINE.test_traits(text)
