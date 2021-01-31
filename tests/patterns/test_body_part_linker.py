"""Test the link matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test


class TestBodyPartLinker(unittest.TestCase):
    """Test the link trait parser."""

    def test_body_part_linker_01(self):
        self.assertEqual(
            test('Large metallic green damselfly,'),
            [{'body_part': 'damselfly', 'color': 'metallic green',
              'trait': 'color', 'start': 6, 'end': 20},
             {'body_part': 'damselfly', 'trait': 'body_part', 'start': 21, 'end': 30}]
        )

    def test_body_part_linker_02(self):
        self.assertEqual(
            test('may have fine pale lines on thorax,'),
            [{'color_mod': 'fine pale lines', 'body_part': 'thorax',
              'trait': 'color_mod', 'start': 9, 'end': 24},
             {'body_part': 'thorax', 'trait': 'body_part', 'start': 28, 'end': 34}]
        )

    def test_body_part_linker_03(self):
        self.assertEqual(
            test('Face duller and may be glossed with red.'),
            [{'body_part': 'face', 'trait': 'body_part', 'start': 0, 'end': 4},
             {'color_mod': 'duller', 'body_part': 'face',
              'trait': 'color_mod', 'start': 5, 'end': 11},
             {'color': 'glossed with red', 'body_part': 'face',
              'trait': 'color', 'start': 23, 'end': 39}]
        )

    def test_body_part_linker_04(self):
        self.assertEqual(
            test('narrow wings with dusky wingtips.'),
            [{'body_part': 'narrow wings', 'trait': 'body_part', 'start': 0, 'end': 12},
             {'color_mod': 'dusky', 'body_part': 'wingtip',
              'trait': 'color_mod', 'start': 18, 'end': 23},
             {'body_part': 'wingtip', 'trait': 'body_part', 'start': 24, 'end': 32}]
        )

    def test_body_part_linker_05(self):
        self.assertEqual(
            test('Wings often tinged with golden,'),
            [{'body_part': 'wing', 'trait': 'body_part', 'start': 0, 'end': 5},
             {'color': 'tinged with golden', 'body_part': 'wing',
              'trait': 'color', 'start': 12, 'end': 30}]
        )

    def test_body_part_linker_06(self):
        self.assertEqual(
            test('dorsal carina usually blue'),
            [{'body_part': 'dorsal carina',
              'trait': 'body_part', 'start': 0, 'end': 13},
             {'color': 'blue', 'body_part': 'dorsal carina',
              'trait': 'color', 'start': 22, 'end': 26}]
        )
