"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test_fraser


class TestHeader(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_header_01(self):
        self.assertEqual(
            test_fraser("""Amphiagrion saucium/abbreviatum
                    (Eastern/Western Red Damsel)"""),
            [{'sci_name': ['Amphiagrion saucium', 'Amphiagrion abbreviatum'],
              'group': 'odonata',
              'trait': 'sci_name', 'start': 0, 'end': 31},
             {'vernacular': ['western red damsel', 'Eastern red damsel'],
              'trait': 'vernacular', 'start': 53, 'end': 79}]
        )

    def test_header_02(self):
        self.assertEqual(
            test_fraser("""Gomphurus externus (Plains Clubtail)"""),
            [{'sci_name': 'Gomphurus externus', 'group': 'odonata',
              'trait': 'sci_name', 'start': 0, 'end': 18},
             {'vernacular': 'plains clubtail',
              'trait': 'vernacular', 'start': 20, 'end': 35}]
        )
