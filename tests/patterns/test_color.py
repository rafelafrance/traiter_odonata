"""Test the color matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test


class TestColor(unittest.TestCase):
    """Test the color trait parser."""

    def test_color_01(self):
        self.assertEqual(
            test('may be glossed with red.'),
            [{'color': 'glossed with red', 'trait': 'color', 'start': 7, 'end': 23}]
        )

    def test_color_02(self):
        self.assertEqual(
            test('Wings without dark tip;'),
            [{'body_part': 'wing', 'trait': 'body_part', 'start': 0, 'end': 5},
             {'missing': True, 'color_mod': 'without dark tip', 'body_part': 'wing',
              'trait': 'color_mod', 'start': 6, 'end': 22}]
        )

    def test_color_03(self):
        self.assertEqual(
            test('Large metallic green damselfly'),
            [{'color': 'metallic green', 'body_part': 'damselfly',
              'trait': 'color', 'start': 6, 'end': 20},
             {'body_part': 'damselfly', 'trait': 'body_part', 'start': 21, 'end': 30}]
        )

    def test_color_04(self):
        self.assertEqual(
            test('may have fine pale lines'),
            [{'color_mod': 'fine pale lines',
              'trait': 'color_mod', 'start': 9, 'end': 24}]
        )

    def test_color_05(self):
        self.assertEqual(
            test('with slight greenish gloss'),
            [{'color': 'greenish gloss',
              'trait': 'color', 'start': 12, 'end': 26}]
        )

    def test_color_06(self):
        self.assertEqual(
            test('often bluish-green'),
            [{'color': 'bluish-green',
              'trait': 'color', 'start': 6, 'end': 18}]
        )

    def test_color_07(self):
        self.assertEqual(
            test('clear or faintly washed with yellowish tint'),
            [{'color': 'clear or faintly washed with yellowish tint',
              'trait': 'color', 'start': 0, 'end': 43}]
        )

    def test_color_08(self):
        self.assertEqual(
            test('showing yellow squares on S7 '),
            [{'color': 'yellow squares', 'body_part': 's7',
              'trait': 'color', 'start': 8, 'end': 22},
             {'body_part': 's7', 'end': 28, 'start': 26, 'trait': 'body_part'}]
        )

    def test_color_09(self):
        self.assertEqual(
            test('Colored much like male but not pruinose,'),
            [{'sex_diff': 'like male but',
              'trait': 'sex_diff', 'start': 13, 'end': 26},
             {'color_mod': 'not pruinose', 'missing': True, 'sex_diff': 'like male but',
              'trait': 'color_mod', 'start': 27, 'end': 39}]
        )
