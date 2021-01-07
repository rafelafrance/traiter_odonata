"""Test the sex matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test_traits


class TestSex(unittest.TestCase):
    """Test the sex trait parser."""

    def test_sex_01(self):
        self.assertEqual(
            test_traits('Female: Colored like male but duller'),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'sex_diff': 'like male but', 'trait': 'sex_diff', 'start': 16, 'end': 29},
             {'color_mod': 'duller', 'trait': 'color_mod', 'start': 30, 'end': 36}]
        )

    def test_sex_02(self):
        self.assertEqual(
            test_traits('Female: Colored similar to male but duller'),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'sex_diff': 'similar to male but',
              'trait': 'sex_diff', 'start': 16, 'end': 35},
             {'color_mod': 'duller', 'trait': 'color_mod', 'start': 36, 'end': 42}]
        )
