"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test_traits


class TestHeader(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_header_01(self):
        self.assertEqual(
            test_traits("""Amphiagrion saucium/abbreviatum
                    (Eastern/Western Red Damsel)"""),
            [{'sci_name': ['Amphiagrion saucium', 'Amphiagrion abbreviatum'],
              'group': 'odonata',
              'trait': 'sci_name', 'start': 0, 'end': 31},
             {'vernacular': ['western red damsel', 'Eastern red damsel'],
              'trait': 'vernacular', 'start': 33, 'end': 59}]
        )

    def test_header_02(self):
        self.assertEqual(
            test_traits('Gomphurus externus (Plains Clubtail)'),
            [{'sci_name': 'Gomphurus externus', 'group': 'odonata',
              'trait': 'sci_name', 'start': 0, 'end': 18},
             {'vernacular': 'plains clubtail',
              'trait': 'vernacular', 'start': 20, 'end': 35}]
        )

    def test_header_03(self):
        self.assertEqual(
            test_traits("""
                3 Sparkling Jewelwing Calopteryx dimidiata TL 37–50, HW 23–31
                """),
            [{'vernacular': 'sparkling jewelwing', 'in_header': True,
              'trait': 'vernacular', 'start': 2, 'end': 21},
             {'sci_name': 'Calopteryx dimidiata', 'group': 'odonata', 'in_header': True,
              'trait': 'sci_name', 'start': 22, 'end': 42},
             {'low': 37.0, 'high': 50.0, 'in_header': True,
              'trait': 'total_length', 'start': 43, 'end': 51},
             {'low': 23.0, 'high': 31.0, 'in_header': True,
              'trait': 'hind_wing_length', 'start': 53, 'end': 61}]
        )
