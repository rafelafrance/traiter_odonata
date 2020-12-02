"""Test the color matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import test_traits


class TestColor(unittest.TestCase):
    """Test the color trait parser."""

    def test_color_01(self):
        self.assertEqual(
            test_traits(shorten("""may be glossed with red.""")),
            [{'color': 'glossed with red', 'trait': 'color', 'start': 7, 'end': 23}]
        )

    def test_color_02(self):
        self.assertEqual(
            test_traits(shorten("""Wings without dark tip;""")),
            [{'body_part': 'wing', 'trait': 'body_part', 'start': 0, 'end': 5},
             {'color_pat': 'without dark', 'missing': True,
              'trait': 'color_pat', 'start': 6, 'end': 18},
             {'body_part_loc': 'tip', 'trait': 'body_part_loc', 'start': 19, 'end': 22}]
        )

    def test_color_03(self):
        self.assertEqual(
            test_traits(shorten("""Large metallic green damselfly""")),
            [{'color': 'metallic green', 'trait': 'color', 'start': 6, 'end': 20},
             {'body_part': 'damselfly', 'trait': 'body_part', 'start': 21, 'end': 30}]
        )

    def test_color_04(self):
        self.assertEqual(
            test_traits(shorten("""may have fine pale lines""")),
            [{'color_pat': 'fine pale lines',
              'trait': 'color_pat', 'start': 9, 'end': 24}]
        )

    def test_color_05(self):
        self.assertEqual(
            test_traits(shorten("""with slight greenish gloss""")),
            [{'color': 'greenish gloss',
              'trait': 'color', 'start': 12, 'end': 26}]
        )

    def test_color_06(self):
        self.assertEqual(
            test_traits(shorten("""often bluish-green""")),
            [{'color': 'bluish-green',
              'trait': 'color', 'start': 6, 'end': 18}]
        )

    def test_color_07(self):
        self.assertEqual(
            test_traits(shorten("""clear or faintly washed with yellowish tint""")),
            [{'color': 'clear or faintly washed with yellowish tint',
              'trait': 'color', 'start': 0, 'end': 43}]
        )
