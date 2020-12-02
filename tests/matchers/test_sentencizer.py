"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import TEST_PIPELINE


class TestSegmenter(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_sentencizer_01(self):
        text = shorten("""It was common “along a tiny stream.” Argia apicalis.""")
        doc = TEST_PIPELINE.nlp(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 2)

    def test_sentencizer_02(self):
        text = shorten("""It was common along a tiny stream. Argia apicalis.""")
        doc = TEST_PIPELINE.nlp(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 2)

    def test_sentencizer_03(self):
        text = shorten("""Description Large metallic green damselfly""")
        doc = TEST_PIPELINE.nlp(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 2)