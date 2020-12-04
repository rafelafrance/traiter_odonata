"""Test the sex matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import test_traits


class TestSex(unittest.TestCase):
    """Test the sex trait parser."""

    def test_sex_01(self):
        self.assertEqual(
            test_traits(shorten("""Female: Colored like male but duller""")),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'color_mod': 'colored', 'trait': 'color_mod', 'start': 8, 'end': 15},
             {'trait': 'sex_diff', 'start': 16, 'end': 29},
             {'color_mod': 'duller', 'trait': 'color_mod', 'start': 30, 'end': 36}]
        )

    def test_sex_02(self):
        self.assertEqual(
            test_traits(shorten("""Female: Colored similar to male but duller""")),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'color_mod': 'colored', 'trait': 'color_mod', 'start': 8, 'end': 15},
             {'trait': 'sex_diff', 'start': 16, 'end': 35},
             {'color_mod': 'duller', 'trait': 'color_mod', 'start': 36, 'end': 42}]
        )
