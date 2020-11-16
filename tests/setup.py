"""Setup for all tests."""

from typing import Dict, List

from src.matchers.matcher import FRASER_MATCHERS, PAULSON_MATCHERS
from src.matchers.pipeline import Pipeline

TEST_FRASER = Pipeline(FRASER_MATCHERS)  # Singleton for testing
TEST_PAULSON = Pipeline(PAULSON_MATCHERS)  # Singleton for testing


def test_fraser(text: str) -> List[Dict]:
    """Find entities in the doc."""
    return TEST_FRASER.test_traits(text)


def test_paulson(text: str) -> List[Dict]:
    """Find entities in the doc."""
    return TEST_PAULSON.test_traits(text)
