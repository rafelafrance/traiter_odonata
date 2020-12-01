"""Test the body part matcher."""

# pylint: disable=missing-function-docstring

import unittest

from traiter.pylib.util import shorten

from tests.setup import test_paulson


class TestBodyPart(unittest.TestCase):
    """Test the body part trait parser."""

    def test_body_part_01(self):
        self.assertEqual(
            test_paulson(shorten("""
                tip with fine dorsal line and lower sides pale.
                """)),
            [{'part_location': 'tip', 'trait': 'part_location', 'start': 0, 'end': 3},
             {'body_part': 'fine dorsal line',
              'trait': 'body_part', 'start': 9, 'end': 25},
             {'part_location': 'lower sides',
              'trait': 'part_location', 'start': 30, 'end': 41},
             {'color': 'pale', 'trait': 'color', 'start': 42, 'end': 46}]
        )

    def test_body_part_02(self):
        self.assertEqual(
            test_paulson(shorten("""underside extends onto lower sides.""")),
            [{'body_part': 'underside', 'trait': 'body_part', 'start': 0, 'end': 9},
             {'part_location': 'lower sides',
              'trait': 'part_location', 'start': 23, 'end': 34}]
        )
