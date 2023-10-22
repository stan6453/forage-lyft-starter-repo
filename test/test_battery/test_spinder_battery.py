from unittest import TestCase
from models.battery import SpindlerBattery
from datetime import datetime


class TestNubbinBattery(TestCase):
    def test_battery(self):
        test_case = [
            (
                datetime(2023, 10, 21),
                datetime(2020, 10, 21),
                True,
                "Battery needs servicing test1"
            ),
            (
                datetime(2023, 10, 21, 23, 46),
                datetime(2020, 10, 21, 23, 45),
                True,
                "Battery needs servicing test2"
            ),
            (
                datetime(2023, 10, 21),
                datetime(2020, 10, 22),
                False,
                "Battery does not need servicing test1"
            ),
            (
                datetime(2023, 10, 21, 16, 30),
                datetime(2020, 10, 21, 23, 45),
                False,
                "Battery does not need servicing test2"
            )
        ]
        for current_date, last_service_date, test_result, test_description in test_case:
            with self.subTest(test_description):
                battery = SpindlerBattery(current_date, last_service_date)
                self.assertEqual(battery.needs_service(), test_result)
