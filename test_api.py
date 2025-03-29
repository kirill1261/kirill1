import unittest
from api import app  # Імпортуємо Flask API

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_get_iphone_prices(self):
        """Перевіряє, що API повертає список iPhone"""
        response = self.client.get("/iphones")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_invalid_endpoint(self):
        """Перевіряє, що API повертає 404 на невідомий запит"""
        response = self.client.get("/wrong_url")
        self.assertEqual(response.status_code, 404)

if name == '__main__':
    unittest.main()
