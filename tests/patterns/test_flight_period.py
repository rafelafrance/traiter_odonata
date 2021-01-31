# """Test the flight period matcher."""
#
# # pylint: disable=missing-function-docstring
#
# import unittest
#
# from tests.setup import test
#
#
# class TestFlightPeriod(unittest.TestCase):
#     """Test the plant color trait parser."""
#
#     def test_flight_period_01(self):
#         self.assertEqual(
#             test('FP: mid-June to late Aug.'),
#             [{'flight_period_key': 'flight period',
#               'trait': 'flight_period_key', 'start': 0, 'end': 3},
#              {'from': 'mid June', 'to': 'late August',
#               'trait': 'month_range', 'start': 4, 'end': 25}]
#         )
