"""Test the color_like matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test


class TestColorLike(unittest.TestCase):
    """Test the color_like matcher."""

    def test_color_like_01(self):
        self.assertEqual(
            test('Female: Colored and shaped as male but face lighter reddish.'),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'color_like': 'as male',
              'trait': 'color_like',
              'start': 27,
              'end': 34,
              'sex': 'female'},
             {'body_part': 'face',
              'trait': 'body_part',
              'start': 39,
              'end': 43,
              'sex': 'female'},
             {'color': 'lighter reddish',
              'trait': 'color',
              'start': 44,
              'end': 59,
              'color_like': 'as male',
              'body_part': 'face',
              'sex': 'female'}]
        )

    def test_color_like_02(self):
        self.assertEqual(
            test('Wings somewhat paler at base than in male.'),
            [{'body_part': 'wing', 'trait': 'body_part', 'start': 0, 'end': 5},
             {'color_like': 'paler at base than in male',
              'trait': 'color_like',
              'start': 15,
              'end': 41,
              'body_part': 'wing'}]
        )

    def test_color_like_03(self):
        self.assertEqual(
            test('Thorax and abdomen as in male'),
            [{'body_part': ['thorax', 'abdomen'],
              'trait': 'body_part',
              'start': 0,
              'end': 18},
             {'color_like': 'as in male',
              'trait': 'color_like',
              'start': 19,
              'end': 29,
              'body_part': ['thorax', 'abdomen']}]
        )

    def test_color_like_04(self):
        self.assertEqual(
            test('female than in male'),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'color_like': 'than in male',
              'trait': 'color_like',
              'start': 7,
              'end': 19,
              'sex': 'female'}]
        )

    def test_color_like_05(self):
        self.assertEqual(
            test('Colored much like male but slightly duller'),
            [{'color_like': 'colored much like male',
              'trait': 'color_like',
              'start': 0,
              'end': 22},
             {'color_mod': 'slightly duller',
              'trait': 'color_mod',
              'start': 27,
              'end': 42,
              'color_like': 'colored much like male'}]
        )

    def test_color_like_06(self):
        self.assertEqual(
            test('Some colored exactly like male.'),
            [{'color_like': 'colored exactly like male',
              'trait': 'color_like',
              'start': 5,
              'end': 30}]
        )
