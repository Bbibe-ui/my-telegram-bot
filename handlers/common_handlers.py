from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def handle_start(message: Message):
    """
    Обработчик команды /start. Приветствует пользователя.
    """
    welcome_message = (
        f"<b>Привет, {message.from_user.full_name}!</b>\n\n"
        "Я многофункциональный бот-помощник.\n\n"
        "<b>Доступные команды:</b>\n"
        "/weather <code>Город</code> - узнать погоду\n"
        "/crypto <code>СИМВОЛ</code> - узнать курс криптовалюты (например, /crypto BTC)"
    )
    await message.answer(welcome_message)

@router.message(Command("help"))
async def handle_help(message: Message):
    """
    Обработчик команды /help. Показывает список доступных команд.
    """
    help_text = (
        "<b>Список доступных команд:</b>\n\n"
        "/start - Начало работы\n"
        "/help - Показать это сообщение\n"
        "/weather <code>Город</code> - Узнать погоду в указанном городе. Пример: <code>/weather Лондон</code>\n"
        "/crypto <code>СИМВОЛ</code> - Получить курс криптовалюты к USD. Пример: <code>/crypto ETH</code>"
    )
    await message.answer(help_text)

from utils.core_logic import process_ambient_data

@router.message()
async def handle_text(message: Message):
    response = await process_ambient_data(message.text)
    if response:
        await message.answer(response)
