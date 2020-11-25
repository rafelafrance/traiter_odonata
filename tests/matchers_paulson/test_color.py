"""Test the color matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import test_paulson


class TestColor(unittest.TestCase):
    """Test the color trait parser."""

    def test_color_01(self):
        self.assertEqual(
            test_paulson(shorten("""
                may be glossed with red.
                """)),
            [{'color': 'red-glossed', 'trait': 'color', 'start': 7, 'end': 23}]
        )

    def test_color_02(self):
        self.assertEqual(
            test_paulson(shorten("""
                Wings without dark tip;
                """)),
            [{'body_part': 'wing', 'trait': 'body_part', 'start': 0, 'end': 5},
             {'missing': True, 'color': 'dark', 'part': 'tip',
              'trait': 'color', 'start': 6, 'end': 22}]
        )

    def test_color_03(self):
        self.assertEqual(
            test_paulson(shorten("""
                Wings without dark tip;
                """)),
            [{'body_part': 'wing', 'trait': 'body_part', 'start': 0, 'end': 5},
             {'missing': True, 'color': 'dark', 'part': 'tip',
              'trait': 'color', 'start': 6, 'end': 22}]
        )
