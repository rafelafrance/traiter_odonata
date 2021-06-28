"""Test the body part matcher."""

import unittest

from tests.setup import test


class TestBodyPart(unittest.TestCase):
    """Test the body part trait parser."""

    def test_body_part_01(self):
        self.assertEqual(
            test('S2–S4'),
            [{'body_part': ['s2', 's3', 's4'],
              'trait': 'body_part', 'start': 0, 'end': 5}]
        )

    def test_body_part_02(self):
        self.assertEqual(
            test('underside extends onto lower sides.'),
            [{'body_subpart': 'underside', 'trait': 'body_subpart', 'start': 0,
              'end': 9},
             {'body_subpart': 'lower sides',
              'trait': 'body_subpart',
              'start': 23,
              'end': 34}]
        )

    def test_body_part_03(self):
        self.assertEqual(
            test('on either side of front'),
            [{'body_subpart': 'side of front',
              'trait': 'body_subpart', 'start': 10, 'end': 23}]
        )

    def test_body_part_04(self):
        self.assertEqual(
            test('with narrow, unmarked wings'),
            [{'color_mod': 'unmarked',
              'trait': 'color_mod',
              'start': 13,
              'end': 21,
              'body_part': 'wing'},
             {'body_part': 'wing', 'trait': 'body_part', 'start': 22, 'end': 27}]
        )

    def test_body_part_05(self):
        self.assertEqual(
            test('lack stigmas'),
            [{'body_part': 'stigma missing', 'missing': True,
              'trait': 'body_part', 'start': 0, 'end': 12}]
        )

    def test_body_part_06(self):
        self.assertEqual(
            test('S2–10'),
            [{'body_part': ['s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'],
              'trait': 'body_part', 'start': 0, 'end': 5}]
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
            [{'body_part': ['thorax underside', 'abdomen tip'],
              'trait': 'body_part',
              'start': 0,
              'end': 35}]
        )

    def test_body_part_09(self):
        self.assertEqual(
            test('Abdomen with dorsal markings on S3–6 narrow,'),
            [{'body_part': 'abdomen', 'trait': 'body_part', 'start': 0, 'end': 7},
             {'color_mod': 'dorsal markings',
              'trait': 'color_mod',
              'start': 13,
              'end': 28,
              'body_part': ['s3', 's4', 's5', 's6']},
             {'body_part': ['s3', 's4', 's5', 's6'],
              'trait': 'body_part',
              'start': 32,
              'end': 36}]
        )
