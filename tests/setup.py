"""Setup for all tests."""

from typing import Dict, List

from src.matchers.matcher import FRASER_MATCHERS
from src.matchers.pipeline import Pipeline

TEST_PIPELINE = Pipeline(FRASER_MATCHERS)  # Singleton for testing


def test_traits(text: str) -> List[Dict]:
    """Find entities in the doc."""
    return TEST_PIPELINE.test_traits(text)
