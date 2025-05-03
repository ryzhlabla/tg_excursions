import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup


# Токен бота
from Config import TOKEN

# Точки экскурсии


# Тексты для кнопок

    #Музей Пикассо
from app.step8 import txt1 as txt1








txt2 = "Это текст для Button2"
txt3 = "Это текст для Button3"
txt4 = "Это текст для Button4"
txt5 = "Это текст для Button5"
txt6 = "Это текст для Button6"

# Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Музей Пикассо"),
            KeyboardButton(text="Button2"),
            KeyboardButton(text="Button3"),
        ],
        [
            KeyboardButton(text="Button4"),
            KeyboardButton(text="Button5"),
            KeyboardButton(text="Button6"),
        ],
    ],
    resize_keyboard=True
)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))  # <-- ВОТ так теперь правильно писать
async def start_handler(message: Message):
    await message.answer("Выберите кнопку:", reply_markup=keyboard)

# Хэндлер на нажатие кнопок
@dp.message()
async def button_handler(message: Message):
    if message.text == "Музей Пикассо":
        await message.answer(txt1, parse_mode="Markdown")
    elif message.text == "Button2":
        await message.answer(txt2, parse_mode="Markdown")
    elif message.text == "Button3":
        await message.answer(txt3)
    elif message.text == "Button4":
        await message.answer(txt4)
    elif message.text == "Button5":
        await message.answer(txt5)
    elif message.text == "Button6":
        await message.answer(txt6)
    else:
        await message.answer("Пожалуйста, выберите кнопку.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
