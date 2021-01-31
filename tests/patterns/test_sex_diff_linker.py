"""Test the sex diff linker."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test


class TestSexDiffLinker(unittest.TestCase):
    """Test the sex trait parser."""

    def test_sex_diff_linker_01(self):
        self.assertEqual(
            test('Female: Colored and shaped as male but face lighter reddish.'),
            [{'sex': 'female', 'trait': 'sex', 'start': 0, 'end': 6},
             {'sex_diff': 'as male but', 'trait': 'sex_diff', 'start': 27, 'end': 38},
             {'body_part': 'face', 'sex_diff': 'as male but',
              'trait': 'body_part', 'start': 39, 'end': 43},
             {'color': 'red', 'body_part': 'face', 'sex_diff': 'as male but',
              'trait': 'color', 'start': 52, 'end': 59}]
        )
