"""Test the sex matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import test_paulson


class TestSex(unittest.TestCase):
    """Test the sex trait parser."""

    def test_sex_01(self):
        self.assertEqual(
            test_paulson(shorten("""
                Female: Colored like male but duller
                """)),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'color': 'colored', 'trait': 'color', 'start': 8, 'end': 15},
             {'sex_comparison': 'like male',
              'trait': 'sex_comparison', 'start': 16, 'end': 25},
             {'color': 'duller', 'trait': 'color', 'start': 30, 'end': 36}]
        )

    def test_sex_02(self):
        self.assertEqual(
            test_paulson(shorten("""
                Female: Colored similar to male but duller
                """)),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'color': 'colored', 'trait': 'color', 'start': 8, 'end': 15},
             {'sex_comparison': 'similar to male',
              'trait': 'sex_comparison', 'start': 16, 'end': 31},
             {'color': 'duller', 'trait': 'color', 'start': 36, 'end': 42}]
        )
