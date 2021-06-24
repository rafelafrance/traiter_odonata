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
