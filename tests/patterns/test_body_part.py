"""Test the body part matcher."""

import unittest

from tests.setup import test


class TestBodyPart(unittest.TestCase):
    """Test the body part trait parser."""

    def test_body_part_01(self):
        self.assertEqual(
            test('tip with fine dorsal line and lower sides pale.'),
            [{'color_mod': 'tip',
              'trait': 'color_mod', 'start': 0, 'end': 3,
              'body_part': 'dorsal line and lower sides'},
             {'body_part': 'dorsal line and lower sides',
              'trait': 'body_part', 'start': 14, 'end': 41},
             {'color_mod': 'pale',
              'trait': 'color_mod', 'start': 42, 'end': 46,
              'body_part': 'dorsal line and lower sides'}]
        )

    def test_body_part_02(self):
        self.assertEqual(
            test('underside extends onto lower sides.'),
            [{'body_part_loc': 'underside',
              'trait': 'body_part_loc', 'start': 0, 'end': 9},
             {'body_part': 'lower sides',
              'trait': 'body_part', 'start': 23, 'end': 34}]
        )

    def test_body_part_03(self):
        self.assertEqual(
            test('on either side of front'),
            [{'body_part_loc': 'either side of front',
              'trait': 'body_part_loc', 'start': 3, 'end': 23}]
        )

    def test_body_part_04(self):
        self.assertEqual(
            test('with narrow, unmarked wings'),
            [{'body_part': 'narrow, unmarked wings',
              'trait': 'body_part', 'start': 5, 'end': 27}]
        )

    def test_body_part_05(self):
        self.assertEqual(
            test('lack stigmas'),
            [{'body_part': 'lack stigmas', 'missing': True,
              'trait': 'body_part', 'start': 0, 'end': 12}]
        )

    def test_body_part_06(self):
        self.assertEqual(
            test('S2–10'),
            [{'body_part': 's2–10', 'trait': 'body_part', 'start': 0, 'end': 5}]
        )

    def test_body_part_07(self):
        self.assertEqual(
            test('bluet unmistakable because of orange face'),
            [{'color': 'orange', 'body_part': 'face',
              'trait': 'color', 'start': 30, 'end': 36},
             {'body_part': 'face', 'trait': 'body_part', 'start': 37, 'end': 41}]
        )

    def test_body_part_08(self):
        self.assertEqual(
            test('underside of thorax and abdomen tip.'),
            [{'body_part': 'underside of thorax and abdomen',
              'trait': 'body_part', 'start': 0, 'end': 31},
             {'color_mod': 'tip', 'trait': 'color_mod', 'start': 32, 'end': 35,
              'body_part': 'underside of thorax and abdomen'}]
        )
