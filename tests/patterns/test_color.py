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
             {'missing': True,
              'color_mod': 'without dark tip',
              'trait': 'color_mod',
              'start': 6,
              'end': 22,
              'body_part': 'wing'}]
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
            [{'color_like': 'like male', 'trait': 'color_like', 'start': 13, 'end': 22},
             {'missing': True,
              'color_mod': 'not pruinose',
              'trait': 'color_mod',
              'start': 27,
              'end': 39,
              'color_like': 'like male'}]
        )

    def test_color_10(self):
        self.assertEqual(
            test('with whitish rings at ends of all segments 2–9'),
            [{'color': 'whitish rings',
              'trait': 'color',
              'start': 5,
              'end': 18,
              'body_subpart': 'ends',
              'body_part': ['s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']},
             {'body_subpart': 'ends', 'trait': 'body_subpart', 'start': 22, 'end': 26},
             {'body_part': ['s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9'],
              'trait': 'body_part',
              'start': 34,
              'end': 46}]
        )

    def test_color_11(self):
        self.assertEqual(
            test("""
                Description Large, white-ringed northern emerald of large lakes."""),
            [{'color': 'white-ringed', 'trait': 'color', 'start': 19, 'end': 31},
             {'habitat': 'lakes', 'trait': 'habitat', 'start': 58, 'end': 63}]
        )

    def test_color_12(self):
        self.assertEqual(
            test("""Male: Face black, yellow on sides."""),
            [{'sex': 'male', 'trait': 'sex', 'start': 0, 'end': 4},
             {'body_part': 'face',
              'trait': 'body_part',
              'start': 6,
              'end': 10,
              'sex': 'male'},
             {'color': 'black',
              'trait': 'color',
              'start': 11,
              'end': 16,
              'body_part': 'face',
              'sex': 'male'},
             {'color': 'yellow on sides',
              'trait': 'color',
              'start': 18,
              'end': 33,
              'body_part': 'face',
              'sex': 'male'}]
        )

    def test_color_13(self):
        self.assertEqual(
            test("""Thorax metallic green and brown, otherwise unmarked. """),
            [{'body_part': 'thorax', 'trait': 'body_part', 'start': 0, 'end': 6},
             {'color': 'metallic green and brown',
              'trait': 'color',
              'start': 7,
              'end': 31,
              'body_part': 'thorax',
              'color_mod': 'otherwise unmarked'},
             {'color_mod': 'otherwise unmarked',
              'trait': 'color_mod',
              'start': 33,
              'end': 51,
              'color': 'metallic green and brown'}]
        )

    def test_color_14(self):
        self.assertEqual(
            test("""Abdomen black, with whitish rings at ends of all segments 2–9."""),
            [{'body_part': 'abdomen', 'trait': 'body_part', 'start': 0, 'end': 7},
             {'color': 'black',
              'trait': 'color',
              'start': 8,
              'end': 13,
              'body_part': 'abdomen',
              'color_mod': 'with whitish rings',
              'body_subpart': 'ends'},
             {'color_mod': 'with whitish rings',
              'trait': 'color_mod',
              'start': 15,
              'end': 33,
              'color': 'black',
              'body_subpart': 'ends',
              'body_part': ['s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']},
             {'body_subpart': 'ends', 'trait': 'body_subpart', 'start': 37, 'end': 41},
             {'body_part': ['s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9'],
              'trait': 'body_part',
              'start': 49,
              'end': 61}]
        )

    def test_color_15(self):
        self.assertEqual(
            test("""Female: Colored as male."""),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'color_like': 'colored as male',
              'trait': 'color_like',
              'start': 8,
              'end': 23,
              'sex': 'female'}]
        )

    def test_color_16(self):
        self.assertEqual(
            test('Abdomen bright red, variably marked at tip with black.'),
            [{'body_part': 'abdomen', 'trait': 'body_part', 'start': 0, 'end': 7},
             {'color': 'bright red',
              'trait': 'color',
              'start': 8,
              'end': 18,
              'body_part': 'abdomen',
              'color_mod': 'marked at tip with black'},
             {'color_mod': 'marked at tip with black',
              'trait': 'color_mod',
              'start': 29,
              'end': 53}]
        )
