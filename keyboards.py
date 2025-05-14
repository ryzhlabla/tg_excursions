from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from buttons import EXCURSION_BUTTONS   

# Основное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=EXCURSION_BUTTONS[0])],
      #  [KeyboardButton(text=EXCURSION_BUTTONS[10])],
        [KeyboardButton(text=EXCURSION_BUTTONS[21])]
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
            InlineKeyboardButton(text=EXCURSION_BUTTONS[3], callback_data="UberWasser") ,    #"3. Убервасеркирхе"
            InlineKeyboardButton(text=EXCURSION_BUTTONS[4], callback_data="MunsterDom")       # "4. Мюнстерский собор"
        ],
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[5], callback_data="Prinzipal"),       #". Принципалмаркт"
            InlineKeyboardButton(text=EXCURSION_BUTTONS[18], callback_data="Weiter"),        # 7. Далее.. (Конпки с 6 по 10)
        ]
    ]
)




# Меню экскурсии 2 часть на инлайнах

excursion_menu2  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[6], callback_data="Stein"),        # "6. Камни преткновения"
            InlineKeyboardButton(text=EXCURSION_BUTTONS[7], callback_data="StLambert")     #"7. Церковь Святого Ламберта"
        ],
        [ 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[8], callback_data="Rathaus") ,    #"8. Историческая Ратуша" 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[9], callback_data="StadtMuseum")       # " 9. Городской музей"
        ],
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[24], callback_data="Zuruck2"),       # 21. Назад (к кнопкам 1-5)
            InlineKeyboardButton(text=EXCURSION_BUTTONS[25], callback_data="Weiter2"),        # 20. Далее... (Конпки с 10 по 12)
           
        ]
    ]
)

# Меню экскурсии 3 часть на инлайнах

excursion_menu3  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[10], callback_data="StCliment"),        # "10. Церковь Святого Климента" ,                    #16
            InlineKeyboardButton(text=EXCURSION_BUTTONS[11], callback_data="Neueplatz")     #"11. Новая площадь" ,                          #17
        ],
        [ 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[12], callback_data="StadtSchloss") ,    #"12. Ротенбург (дворец)" ,                                 #18
            InlineKeyboardButton(text=EXCURSION_BUTTONS[13], callback_data="Picasso")       # "13. Музей Пикассо",                            #19
        ],
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[26], callback_data="Zuruck3"),        # 20. Далее... (Конпки с 10 по 12)
            InlineKeyboardButton(text=EXCURSION_BUTTONS[27], callback_data="Weiter3"),       # "⬅️ Назад...."         (Конпки с 6 по 10)                         #22
          
        ]
    ]
)


# Меню экскурсии 4 часть на инлайнах

excursion_menu4  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[14], callback_data="WestValMuseum"),        # "14. Вестфальский музей" ,                    #16
            InlineKeyboardButton(text=EXCURSION_BUTTONS[15], callback_data="Aasee")     #"15. Озеро Аазее" ,                          #17
        ],
        [ 
            InlineKeyboardButton(text=EXCURSION_BUTTONS[16], callback_data="Hafen") ,    #"16. Порт Мюнстера" ,                                 #18
            InlineKeyboardButton(text=EXCURSION_BUTTONS[17], callback_data="Ende")       # "17. Заключение",                            #19
        ],
        [
            InlineKeyboardButton(text=EXCURSION_BUTTONS[28], callback_data="Zuruck4"),        # 20. Назад.... (Конпки с 10 по 12)
         #   InlineKeyboardButton(text=EXCURSION_BUTTONS[22], callback_data="Weiter3"),       # "⬅️ Далее...."         (Конпки с 6 по 10)                         #22
          
        ]
    ]
)

