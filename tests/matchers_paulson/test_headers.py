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
              'in_header': True, 'trait': 'vernacular', 'start': 2, 'end': 21},
             {'sci_name': 'Calopteryx dimidiata', 'group': 'odonata',
              'in_header': True, 'trait': 'sci_name', 'start': 22, 'end': 42},
             {'low': 37.0, 'high': 50.0, 'units': 'mm',
              'in_header': True, 'trait': 'total_length', 'start': 43, 'end': 51},
             {'low': 23.0, 'high': 31.0, 'units': 'mm',
              'in_header': True, 'trait': 'hind_wing_length', 'start': 53, 'end': 61}]
        )
