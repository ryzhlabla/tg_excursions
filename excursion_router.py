from aiogram import Router
from aiogram.types import Message
import asyncio
from keyboards import excursion_menu
from media import audio_step1, photo_step1_1, text_step1
from buttons import EXCURSION_BUTTONS

router = Router()

@router.message(lambda msg: msg.text in (EXCURSION_BUTTONS[0], EXCURSION_BUTTONS[1]))
async def intro(message: Message):
    await message.answer_voice(voice=audio_step1, caption="Вступление. Аудиоверсия")
    await asyncio.sleep(1)
    await message.answer_photo(photo_step1_1, caption="Рис1. Вид Мюнстера, 1881 год")
    await asyncio.sleep(2)
    await message.answer(text_step1, parse_mode="Markdown", reply_markup=excursion_menu)
