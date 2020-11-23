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
            [{'group': 'odonata',
              'sci_name': ['Amphiagrion saucium', 'Abbreviatum amphiagrion'],
              'in_header': True, 'trait': 'sci_name', 'start': 0, 'end': 31},
             {'vernacular': ['Eastern red damsel', 'Western red damsel'],
              'in_header': True, 'trait': 'vernacular', 'start': 53, 'end': 79}]
        )

    def test_header_02(self):
        self.assertEqual(
            test_fraser("""Gomphurus externus (Plains Clubtail)"""),
            [{'sci_name': 'Gomphurus externus', 'group': 'odonata', 'in_header': True,
              'trait': 'sci_name', 'start': 0, 'end': 18},
             {'vernacular': 'plains clubtail', 'in_header': True,
              'trait': 'vernacular', 'start': 20, 'end': 35}]
        )
