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


# Меню экскурсии 1 часть
excursion_menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=EXCURSION_BUTTONS[1]),     # 1. Вступление
            KeyboardButton(text=EXCURSION_BUTTONS[2]),     # 2. Музей Пикассо
            KeyboardButton(text=EXCURSION_BUTTONS[3]),     # 3. Button3
            KeyboardButton(text=EXCURSION_BUTTONS[4]),     # 4. Button4
        ],
        [
            KeyboardButton(text=EXCURSION_BUTTONS[5]),     # 5. Button5
            KeyboardButton(text=EXCURSION_BUTTONS[7]),     # 7. Далее.. (Конпки с 6 по 10)
            KeyboardButton(text=EXCURSION_BUTTONS[12]),    # 12. Назад.. (Возврат в меню)
            KeyboardButton(text=EXCURSION_BUTTONS[9])      # 9. Карта
        ],
    ],
    resize_keyboard=True
)

# Меню экскурсии 2 часть
excursion_menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=EXCURSION_BUTTONS[6]),     # "6. Городской музей"
            KeyboardButton(text=EXCURSION_BUTTONS[13]),     # "7. Городской дворец"
            KeyboardButton(text=EXCURSION_BUTTONS[14]),     # "8. Новая площадь" 
            KeyboardButton(text=EXCURSION_BUTTONS[15]),     # "9. Музей Пикассо"
        ],
        [
            KeyboardButton(text=EXCURSION_BUTTONS[16]),     # "10. Церковь Св. Павла"
            KeyboardButton(text=EXCURSION_BUTTONS[20]),     # 20. Далее...
            KeyboardButton(text=EXCURSION_BUTTONS[21]),    # 21. Назад (к кнопкам 1-5)
            KeyboardButton(text=EXCURSION_BUTTONS[9])      # 9. Карта
        ],
    ],
    resize_keyboard=True
)

# Меню экскурсии 3 часть
excursion_menu3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=EXCURSION_BUTTONS[17]),     # "11. Озеро Аазее"
            KeyboardButton(text=EXCURSION_BUTTONS[18]),     # "12. Порт"
            KeyboardButton(text=EXCURSION_BUTTONS[19]),     # "13. Заключение" 
            KeyboardButton(text=EXCURSION_BUTTONS[22]),     # "Назад...."
        ],
        [
         #   KeyboardButton(text=EXCURSION_BUTTONS[16]),     # "10. Церковь Св. Павла"
         #   KeyboardButton(text=EXCURSION_BUTTONS[20]),     # 20. Далее...
         #   KeyboardButton(text=EXCURSION_BUTTONS[21]),    # 21. Назад (к кнопкам 1-5)
         #   KeyboardButton(text=EXCURSION_BUTTONS[9])      # 9. Карта
        ],
    ],
    resize_keyboard=True
)