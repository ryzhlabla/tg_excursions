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
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[5], callback_data="Rathaus"),       #"5. Ратуша"
            InlineKeyboardButton(text=EXCURSION_BUTTONS[7], callback_data="Weiter"),        # 7. Далее.. (Конпки с 6 по 10)
          #  InlineKeyboardButton(text=EXCURSION_BUTTONS[12], callback_data="Zuruck"),       # 12. Назад.. (Возврат в меню)
           # InlineKeyboardButton(text=EXCURSION_BUTTONS[9], callback_data="Plan")           # 9. Карта
        ]
    ]
)




# Меню экскурсии 2 часть на инлайнах

excursion_menu2  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[6], callback_data="StadtMuseum"),        # "6. Городской музей"
            InlineKeyboardButton(text=EXCURSION_BUTTONS[13], callback_data="StadtSchloss")     #"7. Городской дворец"
        ],
        [ 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[14], callback_data="Neueplatz") ,    #"8. Новая площадь" 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[15], callback_data="Picasso")       # "9. Музей Пикассо"
        ],
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[21], callback_data="Zuruck2"),       # 21. Назад (к кнопкам 1-5)
            InlineKeyboardButton(text=EXCURSION_BUTTONS[20], callback_data="Weiter2"),        # 20. Далее... (Конпки с 10 по 12)
           
        ]
    ]
)

# Меню экскурсии 3 часть на инлайнах

excursion_menu3  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[16], callback_data="StPaul"),        # "⛪ 10. Церковь Св. Павла" ,                    #16
            InlineKeyboardButton(text=EXCURSION_BUTTONS[17], callback_data="Aasee")     #"🌊 11. Озеро Аазее" ,                          #17
        ],
        [ 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[18], callback_data="Hafen") ,    #"⚓ 12. Порт" ,                                 #18
            InlineKeyboardButton(text=EXCURSION_BUTTONS[19], callback_data="Ende")       # "🔚 13. Заключение",                            #19
        ],
        [
          #  InlineKeyboardButton(text=EXCURSION_BUTTONS[20], callback_data="Weiter2"),        # 20. Далее... (Конпки с 10 по 12)
            InlineKeyboardButton(text=EXCURSION_BUTTONS[22], callback_data="Zuruck3"),       # "⬅️ Назад...."         (Конпки с 6 по 10)                         #22
          
        ]
    ]
)

