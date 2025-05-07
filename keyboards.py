from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from buttons import EXCURSION_BUTTONS   

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=EXCURSION_BUTTONS[0])],
        [KeyboardButton(text=EXCURSION_BUTTONS[10])],
        [KeyboardButton(text=EXCURSION_BUTTONS[11])]
    ],
    resize_keyboard=True
)


# Меню экскурсии
excursion_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=EXCURSION_BUTTONS[1]),  # 1. Вступление
            KeyboardButton(text=EXCURSION_BUTTONS[2]),  # 2. Музей Пикассо
            KeyboardButton(text=EXCURSION_BUTTONS[3]),   # 3. Button3
            KeyboardButton(text=EXCURSION_BUTTONS[4]),   # 4. Button4
        ],
        [
            KeyboardButton(text=EXCURSION_BUTTONS[5]),   # 5. Button5
            KeyboardButton(text=EXCURSION_BUTTONS[6]),   # 6. Button6
            KeyboardButton(text=EXCURSION_BUTTONS[7]),   # 7. Далее
            KeyboardButton(text=EXCURSION_BUTTONS[9])   # 9. Карта
        ],
    ],
    resize_keyboard=True
)