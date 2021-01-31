"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from odonata.pylib.pipeline import sentence_pipeline

NLP = sentence_pipeline()


class TestSegmenter(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_sentencizer_01(self):
        text = 'It was common “along a tiny stream.” Argia apicalis.'
        doc = NLP(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 2)

    def test_sentencizer_02(self):
        text = 'It was common along a tiny stream. Argia apicalis.'
        doc = NLP(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 2)

    def test_sentencizer_03(self):
        text = 'Description Large metallic green damselfly'
        doc = NLP(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 2)

    def test_sentencizer_04(self):
        text = 'Fly is 12cm. long and 14 cm. wide.'
        doc = NLP(text)
        sents = list(doc.sents)
        self.assertEqual(len(sents), 1)
