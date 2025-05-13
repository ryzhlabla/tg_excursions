from aiogram import Router
from aiogram.types import Message
import asyncio
from aiogram.types import CallbackQuery
from keyboards import excursion_menu1, excursion_menu2, excursion_menu3, main_menu
from media import audio_step1, photo_step1_1, text_step1
from buttons import EXCURSION_BUTTONS

router = Router()

# Обработчик инлайн кнопки "Вступление"  
@router.callback_query(lambda c: c.data == "intro")
async def handle_intro(callback: CallbackQuery):
    await callback.message.answer_voice(voice=audio_step1, caption="Вступление. Аудиоверсия")
    await asyncio.sleep(1)
    await callback.message.answer_photo(photo_step1_1, caption="Рис1. Вид Мюнстера, 1881 год")
    await asyncio.sleep(2)
    await callback.message.answer(text_step1, parse_mode="Markdown", reply_markup=excursion_menu1)
    await callback.answer()


# Вызов первой точки маршрута из основного меню keyboards 
@router.message(lambda msg: msg.text in (EXCURSION_BUTTONS[0], EXCURSION_BUTTONS[1]))
async def intro(message: Message):
    await message.answer_voice(voice=audio_step1, caption="Вступление. Аудиоверсия")
    await asyncio.sleep(1)
    await message.answer_photo(photo_step1_1, caption="Рис1. Вид Мюнстера, 1881 год")
    await asyncio.sleep(2)
    await message.answer(text_step1, parse_mode="Markdown", reply_markup=excursion_menu1)


# Два обработчика вызова карты google (inline , keyboards)

#Вызов карты экскурсии (Google maps) через основное меню keyboards
@router.message(lambda msg: msg.text  in (EXCURSION_BUTTONS[11]))
async def menu_map(message: Message):
    await message.answer(
        ' [Google maps](https://www.google.com/maps/d/edit?mid=1LzsQNhwI7wxI9ZatG7Ohu-dyYlFOn-Q&usp=sharing)',
        parse_mode="Markdown", reply_markup=excursion_menu1
    )

# # Вызов карты экскурсии (Google maps) через инлайн кнопки
# @router.callback_query(lambda c: c.data == "Plan")
# async def show_map(callback: CallbackQuery):
#     await callback.message.answer(
#         ' [Google maps](https://www.google.com/maps/d/edit?mid=1LzsQNhwI7wxI9ZatG7Ohu-dyYlFOn-Q&usp=sharing)',
#         parse_mode="Markdown",
#         reply_markup=excursion_menu1
#     )
#     await callback.answer()  # Убирает "часики" на кнопке


# #  Скорее всего не актуально! Проверить!!!
# #Возврат в основное меню  (кнопка 12)
# @router.message(lambda msg: msg.text  in (EXCURSION_BUTTONS[12]))
# async def menu_back(message: Message):
#     await message.answer( "Вы вернулись в главное меню",
#          reply_markup=main_menu
#     )

#Посмотреть точки маршрута  (кнопка 10)
@router.message(lambda msg: msg.text  in (EXCURSION_BUTTONS[10]))
async def menu_back(message: Message):
    await message.answer( "Первые 5 точек маршрута",
         reply_markup=excursion_menu1
    )


####################------------------Обработка кнопок "Вперед"--------------#######################
#Вперед к кнопкам 6-10  (кнопка 7)

@router.callback_query(lambda c: c.data == "Weiter")
async def show_excursion_menu2(callback: CallbackQuery):
    await callback.message.answer(
        "Следующие 5 точек маршрута",
        reply_markup=excursion_menu2
    )
    #print("Нажата кнопка Weiter")
    await callback.answer()

#Вперед к кнопкам 11-13  (кнопка 20)

@router.callback_query(lambda c: c.data == "Weiter2")
async def show_excursion_menu3(callback: CallbackQuery):
    await callback.message.answer(
        "Последние точки маршрута",
        reply_markup=excursion_menu3
    )
    await callback.answer()

####################------------------Обработка кнопок "Назад"--------------#######################
# #Назад к кнопкам 1-5  (кнопка 21)

@router.callback_query(lambda c: c.data == "Zuruck2")
async def back_excursion_menu1(callback: CallbackQuery):
    await callback.message.answer(
        "Предыдушие 5 точек маршрута",
        reply_markup=excursion_menu1
    )
    await callback.answer()

# #Назад к кнопкам 10-13  (кнопка 21)

@router.callback_query(lambda c: c.data == "Zuruck3")
async def back_excursion_menu2(callback: CallbackQuery):
    await callback.message.answer(
        "Предыдушие 5 точек маршрута",
        reply_markup=excursion_menu2
    )
    await callback.answer()



