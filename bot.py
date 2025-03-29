import telebot
import os
from scrapper import get_iphone_prices  # Імпортуємо парсер

# Отримуємо токен із змінної середовища (безпека)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def process_command(command):
    """Функція для обробки команд (використовується у тестах)"""
    if command == "/start":
        return "Привіт! Я бот для моніторингу цін на iPhone. Використовуй /price, щоб дізнатися актуальні ціни."
    elif command == "/price":
        data = get_iphone_prices()
        if not data:
            return "На жаль, зараз немає доступних даних."
        return "\n".join([f"{item['model']}: {item['price']} ({item['url']})" for item in data])
    else:
        return "Невідома команда. Спробуй /start або /price."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Відповідає на /start"""
    bot.reply_to(message, process_command("/start"))

@bot.message_handler(commands=['price'])
def send_prices(message):
    """Відповідає на /price"""
    bot.reply_to(message, process_command("/price"))

@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    """Обробляє невідомі команди"""
    bot.reply_to(message, process_command("unknown"))

if name == "__main__":
    print("Бот запущено!")
    bot.polling(none_stop=True)
