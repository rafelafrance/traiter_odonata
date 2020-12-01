"""Test the header matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import test_paulson


class TestHeader(unittest.TestCase):
    """Test the header parser."""

    def test_header_01(self):
        self.assertEqual(
            test_paulson(shorten("""
                3 Sparkling Jewelwing Calopteryx dimidiata TL 37–50, HW 23–31
                """)),
            [{'vernacular': 'sparkling jewelwing',
              'trait': 'vernacular', 'start': 2, 'end': 21},
             {'sci_name': 'Calopteryx dimidiata', 'group': 'odonata',
              'trait': 'sci_name', 'start': 22, 'end': 42},
             {'total_length_key': 'total length',
              'trait': 'total_length_key', 'start': 43, 'end': 45},
             {'low': 37.0, 'high': 50.0, 'trait': 'range', 'start': 46, 'end': 51},
             {'hind_wing_length_key': 'hind wing length',
              'trait': 'hind_wing_length_key', 'start': 53, 'end': 55},
             {'low': 23.0, 'high': 31.0, 'trait': 'range', 'start': 56, 'end': 61}]
        )
