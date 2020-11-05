"""Test the flight period matcher."""

# pylint: disable=missing-function-docstring

import unittest

from src.matchers.pipeline import PIPELINE

NLP = PIPELINE.test_traits


class TestFlightPeriod(unittest.TestCase):
    """Test the plant color trait parser."""

    def test_flight_period_01(self):
        self.assertEqual(
            NLP('FP: mid-June to late Aug.'),
            [
                {'trait': 'flight_period',
                 'from': 'mid June', 'to': 'late August',
                 'start': 0, 'end': 25}]
        )
