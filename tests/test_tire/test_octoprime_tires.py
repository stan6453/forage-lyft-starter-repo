from unittest import TestCase
from models.tire.octoprime_tires import OctoprimeTire


class TestOctoprimeTire(TestCase):
    def test_tire_does_not_need_service(self):
        tires_wear = [1, 1, 0.5, 0.1]
        tire = OctoprimeTire(tires_wear)
        self.assertFalse(tire.needs_service())

    def test_tire_needs_service(self):
        tires_wear = [0.7, 0.9, 0.6, 1]
        tire = OctoprimeTire(tires_wear)
        self.assertTrue(tire.needs_service())
