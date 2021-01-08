"""Test the link matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test_traits


class TestBodyPartLinker(unittest.TestCase):
    """Test the link trait parser."""

    def test_body_part_linker_01(self):
        self.assertEqual(
            test_traits('Large metallic green damselfly,'),
            [{'body_part': 'damselfly', 'color': 'metallic green',
              'trait': 'color', 'start': 6, 'end': 20},
             {'body_part': 'damselfly', 'trait': 'body_part', 'start': 21, 'end': 30}]
        )

    def test_body_part_linker_02(self):
        self.assertEqual(
            test_traits('may have fine pale lines on thorax,'),
            [{'color_mod': 'fine pale lines',
              'trait': 'color_mod', 'start': 9, 'end': 24},
             {'body_part': 'thorax', 'trait': 'body_part', 'start': 28, 'end': 34}]
        )

    def test_body_part_linker_03(self):
        self.assertEqual(
            test_traits('Face duller and may be glossed with red.'),
            [{'body_part': 'face', 'trait': 'body_part', 'start': 0, 'end': 4},
             {'color_mod': 'duller', 'body_part': 'face',
              'trait': 'color_mod', 'start': 5, 'end': 11},
             {'color': 'glossed with red', 'body_part': 'face',
              'trait': 'color', 'start': 23, 'end': 39}]
        )
