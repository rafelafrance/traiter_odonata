"""Test the body part matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test_traits


class TestBodyPart(unittest.TestCase):
    """Test the body part trait parser."""

    def test_body_part_01(self):
        self.assertEqual(
            test_traits("""tip with fine dorsal line and lower sides pale."""),
            [{'body_part_loc': 'tip', 'trait': 'body_part_loc', 'start': 0, 'end': 3},
             {'body_part_loc': 'dorsal line and lower sides',
              'trait': 'body_part_loc', 'start': 14, 'end': 41},
             {'color_mod': 'pale', 'trait': 'color_mod', 'start': 42, 'end': 46}]
        )

    def test_body_part_02(self):
        self.assertEqual(
            test_traits("""underside extends onto lower sides."""),
            [{'body_part_loc': 'underside',
              'trait': 'body_part_loc', 'start': 0, 'end': 9},
             {'body_part': 'lower sides',
              'trait': 'body_part', 'start': 23, 'end': 34}]
        )

    def test_body_part_03(self):
        self.assertEqual(
            test_traits("""on either side of front"""),
            [{'body_part_loc': 'either side of front',
              'trait': 'body_part_loc', 'start': 3, 'end': 23}]
        )

    def test_body_part_04(self):
        self.assertEqual(
            test_traits("""with narrow, unmarked wings"""),
            [{'body_part': 'narrow, unmarked wings',
              'trait': 'body_part', 'start': 5, 'end': 27}]
        )

    def test_body_part_05(self):
        self.assertEqual(
            test_traits("""lack stigmas"""),
            [{'body_part': 'lack stigmas', 'missing': True,
              'trait': 'body_part', 'start': 0, 'end': 12}]
        )

    def test_body_part_06(self):
        self.assertEqual(
            test_traits("""S2–10"""),
            [{'body_part': 's2–10', 'trait': 'body_part', 'start': 0, 'end': 5}]
        )

    def test_body_part_07(self):
        self.assertEqual(
            test_traits("""bluet unmistakable because of orange face"""),
            [{'color': 'orange', 'trait': 'color', 'start': 30, 'end': 36},
             {'body_part': 'face', 'trait': 'body_part', 'start': 37, 'end': 41}]
        )
