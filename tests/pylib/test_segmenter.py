"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.util import shorten

from src.pylib.pipeline import parse


class TestSegmenter(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_sentencizer_01(self):
        text = shorten("""
            It was common “along a tiny stream.” Argia apicalis.
        """)
        _, sents = parse(text, with_sents=True)
        self.assertEqual(len(sents), 2)
        for sent in sents:
            print(sent)
            print()
