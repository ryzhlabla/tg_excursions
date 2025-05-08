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




@router.message(lambda msg: msg.text not in EXCURSION_BUTTONS)
async def fallback(message: Message):
    await message.answer(
        "Пожалуйста, выберите действие:",
        reply_markup=main_menu
    )
