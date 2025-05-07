from aiogram import Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from keyboards import main_menu

from buttons import EXCURSION_BUTTONS

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать! Выберите действие:",
        reply_markup=main_menu
    )


# Обработчики нажатий кнопок меню


@router.message(lambda msg: msg.text == "Открыть карту маршрута в google")
async def menu_map(message: Message):
    await message.answer(
        'Вот [ссылка на карту маршрута](https://www.google.com/maps/d/edit?mid=1LzsQNhwI7wxI9ZatG7Ohu-dyYlFOn-Q&usp=sharing)',
        parse_mode="Markdown"
    )


@router.message(lambda msg: msg.text not in EXCURSION_BUTTONS)
async def fallback(message: Message):
    await message.answer(
        "Пожалуйста, выберите действие:",
        reply_markup=main_menu
    )
