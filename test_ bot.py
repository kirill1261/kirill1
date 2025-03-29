import unittest
from bot import process_command  # Імпортуємо функцію обробки команд

class TestTelegramBot(unittest.TestCase):
    def test_start_command(self):
        """Перевіряє, що /start повертає привітання"""
        response = process_command("/start")
        self.assertIn("Привіт!", response)

    def test_price_command(self):
        """Перевіряє, що /price повертає список цін"""
        response = process_command("/price")
        self.assertIn("Ось актуальні ціни на iPhone", response)

    def test_unknown_command(self):
        """Перевіряє поведінку на невідому команду"""
        response = process_command("/unknown")
        self.assertIn("Невідома команда", response)

if name == '__main__':
    unittest.main()
