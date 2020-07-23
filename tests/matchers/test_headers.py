"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from src.pylib.pipeline import parse


class TestHeader(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_header_01(self):
        self.assertEqual(
            parse("""Amphiagrion saucium/abbreviatum
                    (Eastern/Western Red Damsel)"""),
            [
                {
                 'trait': 'header',
                 'sci_name': 'Amphiagrion saucium/abbreviatum',
                 'vernacular': 'Eastern/Western Red Damsel',
                 'start': 0, 'end': 80}]
        )

    def test_header_02(self):
        self.assertEqual(
            parse("""Gomphurus externus (Plains Clubtail)"""),
            [
                {
                 'trait': 'header',
                 'sci_name': 'Gomphurus externus',
                 'vernacular': 'Plains Clubtail',
                 'start': 0, 'end': 36}]
        )
