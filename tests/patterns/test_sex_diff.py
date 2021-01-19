"""Test the sex matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test_traits


class TestSexDiff(unittest.TestCase):
    """Test the sex trait parser."""

    def test_sex_diff_01(self):
        self.assertEqual(
            test_traits('Female: Colored like male but duller'),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'sex_diff': 'like male but', 'trait': 'sex_diff', 'start': 16, 'end': 29},
             {'color_mod': 'duller', 'sex_diff': 'like male but',
              'trait': 'color_mod', 'start': 30, 'end': 36}]
        )

    def test_sex_diff_02(self):
        self.assertEqual(
            test_traits('Female: Colored similar to male but duller'),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'sex_diff': 'similar to male but',
              'trait': 'sex_diff', 'start': 16, 'end': 35},
             {'color_mod': 'duller', 'sex_diff': 'similar to male but',
              'trait': 'color_mod', 'start': 36, 'end': 42}]
        )

    def test_sex_diff_03(self):
        self.assertEqual(
            test_traits('more contrasty in female than in male.'),
            [{'sex': 'female', 'trait': 'sex', 'start': 18, 'end': 24},
             {'sex_diff': 'than in male',
              'trait': 'sex_diff', 'start': 25, 'end': 37}]
        )

    def test_sex_diff_04(self):
        self.assertEqual(
            test_traits('Duller than male,'),
            [{'color_mod': 'duller', 'sex_diff': 'than male',
              'trait': 'color_mod', 'start': 0, 'end': 6},
             {'sex_diff': 'than male', 'trait': 'sex_diff', 'start': 7, 'end': 16}]
        )

    def test_sex_diff_05(self):
        self.assertEqual(
            test_traits('like those of male'),
            [{'sex_diff': 'like those of male',
              'trait': 'sex_diff', 'start': 0, 'end': 18}]
        )
