from unittest import TestCase
from models.engine import WilloughbyEngine


class TestWilloughbyEngine(TestCase):
    def test_engine(self):
        test_case = [
            (
                120_000,
                60_000,
                True,
                "Engine needs servicing"
            ),
            (
                179_999,
                120_000,
                False,
                "Engine does not need servicing"
            )
        ]
        for current_mileage, last_service_mileage, test_result, test_description in test_case:
            with self.subTest(test_description):
                engine = WilloughbyEngine(current_mileage, last_service_mileage)
                self.assertEqual(engine.needs_service(), test_result)
