"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import TEST_PAULSON


class TestSegmenter(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_sentencizer_01(self):
        text = shorten("""
            Description Large metallic green damselfly
        """)
        doc = TEST_PAULSON.nlp(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 2)
