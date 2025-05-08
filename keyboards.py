from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from buttons import EXCURSION_BUTTONS   

# Основное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=EXCURSION_BUTTONS[0])],
        [KeyboardButton(text=EXCURSION_BUTTONS[10])],
        [KeyboardButton(text=EXCURSION_BUTTONS[11])]
    ],
    resize_keyboard=True
)


# Меню экскурсии 1 часть
excursion_menu1  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[1], callback_data="intro"),         # 1. Вступление
            InlineKeyboardButton(text=EXCURSION_BUTTONS[2], callback_data="SchlossM")     #"2. Замок Мюнстера",
        ],
        [ 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[3], callback_data="Prinzipal") ,    #"3. Главная площадь"
            InlineKeyboardButton(text=EXCURSION_BUTTONS[4], callback_data="Stein")       # "4. Камни"
        ],
        # [    
        #     
        #     InlineKeyboardButton(text=EXCURSION_BUTTONS[5], callback_data="Rathaus"),       #"5. Ратуша"
        #     InlineKeyboardButton(text=EXCURSION_BUTTONS[5], callback_data="Rathaus"),       #"5. Ратуша"
        # ],
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[5], callback_data="Rathaus"),       #"5. Ратуша"
            InlineKeyboardButton(text=EXCURSION_BUTTONS[7], callback_data="Weiter"),        # 7. Далее.. (Конпки с 6 по 10)
          #  InlineKeyboardButton(text=EXCURSION_BUTTONS[12], callback_data="Zuruck"),       # 12. Назад.. (Возврат в меню)
           # InlineKeyboardButton(text=EXCURSION_BUTTONS[9], callback_data="Plan")           # 9. Карта
        ]
    ]
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