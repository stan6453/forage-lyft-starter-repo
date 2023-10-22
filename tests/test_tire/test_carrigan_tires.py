from unittest import TestCase
from models.tire.carrigan_tires import CarriganTire


class TestCarriganTire(TestCase):
    def test_tire_does_not_need_service(self):
        tires_wear = [0.3, 0.4, 0.3, 0.8]
        tire = CarriganTire(tires_wear)
        self.assertFalse(tire.needs_service())

    def test_tire_needs_service(self):
        tires_wear = [0.3, 0.9, 0.3, 0.8]
        tire = CarriganTire(tires_wear)
        self.assertTrue(tire.needs_service())
