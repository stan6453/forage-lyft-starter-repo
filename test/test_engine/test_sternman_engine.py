from unittest import TestCase
from models.engine import SternmanEngine


class TestSternmanEngine(TestCase):
    def test_service_false(self):
        """SternmanEngine does not need servicing"""
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service(),
                         'needs_service() should return False')

    def test_service_true(self):
        """SternmanEngine needs servicing"""
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service(),
                        'needs_service() should return True')
