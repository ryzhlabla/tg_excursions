import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import FSInputFile


# Токен бота
from Config import TOKEN

# Точки экскурсии (пока только одна)


# Тексты для кнопок
    #Вступление
from app.step1_intro.step1 import txt1 as button1_Intro
    #Музей Пикассо
from app.step8_Picasso.step8 import txt1 as button8_Picasso



# Файлы с аудиотекстами
    #Вступление
audio_step1 = FSInputFile("app/step1_intro/step1.mp3")  # <-- путь к файлу


# Фоточки
photo_step1_1 = FSInputFile("app/step1_intro/Munster,_Germany_1881.jpg")


txt2 = "Это текст для Button2"
txt3 = "Это текст для Button3"
txt4 = "Это текст для Button4"
txt5 = "Это текст для Button5"
txt6 = "Это текст для Button6"

# Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1. Вступление"),
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
    if message.text == "1. Вступление":
        await message.answer_voice(voice=audio_step1, caption="Вступление. Аудиоверсия")  # <-- ОБЯЗАТЕЛЬНО указать voice=
        # Делаем паузу 1 секунда
        await asyncio.sleep(1)
        await message.answer_photo(photo_step1_1, caption="Вид Мюнстера, 1881 год")
        await message.answer(button1_Intro, parse_mode="Markdown")
        
    elif message.text == "Музей Пикассо":
        await message.answer(button8_Picasso, parse_mode="Markdown")
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
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot остановлен!")
