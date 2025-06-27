import asyncio
import logging
import os
from handlers import common_handlers, crypto_handlers, weather_handlers
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from utils.commands import set_bot_commands

# --- Конфигурация логирования ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Получение токена из переменных окружения ---
# Пользователю нужно будет создать файл .env и поместить туда свой токен
# TELEGRAM_BOT_TOKEN='ВАШ_ТОКЕН_ЗДЕСЬ'
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def main():
    if not BOT_TOKEN:
        logging.error("Токен не найден. Убедитесь, что TELEGRAM_BOT_TOKEN установлен в .env файле.")
        return

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # --- Регистрация обработчиков ---
    logging.info("Регистрация обработчиков...")
    dp.include_router(common_handlers.router)
    dp.include_router(weather_handlers.router)
    dp.include_router(crypto_handlers.router)
    
    # --- Установка команд бота ---
    await set_bot_commands(bot)
    
    logging.info("Бот запускается...")
    # Удаляем вебхук перед запуском, если он был установлен
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен.")
    except Exception as e:
        logging.error(f"Произошла критическая ошибка: {e}", exc_info=True)
