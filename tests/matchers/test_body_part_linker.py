"""Test the link matcher."""

# pylint: disable=missing-function-docstring

import unittest

from tests.setup import test_traits


class TestColor(unittest.TestCase):
    """Test the link trait parser."""

    def test_linker_01(self):
        self.assertEqual(
            test_traits('Large metallic green damselfly,'),
            [{'body_part': 'damselfly', 'color': 'metallic green',
              'trait': 'color', 'start': 6, 'end': 20},
             {'body_part': 'damselfly', 'trait': 'body_part', 'start': 21, 'end': 30}]
        )
