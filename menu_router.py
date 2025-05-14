from aiogram import Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from keyboards import main_menu
from media import  text_step0

from buttons import EXCURSION_BUTTONS

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
         text_step0,
        reply_markup=main_menu
    )


# Обработчики нажатий кнопок меню




@router.message(lambda msg: msg.text not in EXCURSION_BUTTONS)
async def fallback(message: Message):
    await message.answer(
         text_step0,
        reply_markup=main_menu
    )
