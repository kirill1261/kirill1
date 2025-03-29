import unittest
from scrapper import get_iphone_prices  # Імпортуємо функцію парсингу

class TestScrapper(unittest.TestCase):
    def test_scrapper_returns_data(self):
        """Перевіряє, що парсер повертає список"""
        data = get_iphone_prices()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_scrapper_has_correct_fields(self):
        """Перевіряє, що кожен об'єкт містить потрібні поля"""
        data = get_iphone_prices()
        if data:
            item = data[0]
            self.assertIn("model", item)
            self.assertIn("price", item)
            self.assertIn("url", item)

if name == '__main__':
    unittest.main()
