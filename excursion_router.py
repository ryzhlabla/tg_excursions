from aiogram import Router
from aiogram.types import Message
import asyncio
from aiogram.types import CallbackQuery
from keyboards import excursion_menu1, excursion_menu2, excursion_menu3, excursion_menu4, main_menu
from media import audio_step1, photo_step1_1, text_step1, text_step1_1  # 1 intro
from media import audio_step2,photo_step2_1, text_step2,  text_step2_1  #Schloss Munster
from media import audio_step3, photo_step3_1, text_step3,  text_step3_1  #Uberwasserkirche
from buttons import EXCURSION_BUTTONS
from app.lock import with_lock

router = Router()

# ------------------ Обработчики кнопок маршрута (все подряд) ------------------------

# Обработчик инлайн кнопки "Вступление"  
@router.callback_query(lambda c: c.data == "intro")
@with_lock
async def handle_intro(callback: CallbackQuery):
    await callback.message.answer_voice(voice=audio_step1, caption="Вступление. Аудиоверсия")
    await asyncio.sleep(1)
    await callback.message.answer_photo(photo_step1_1, caption="Рис1. Вид Мюнстера, 1881 год")
    await asyncio.sleep(2)
    await callback.message.answer(text_step1, parse_mode="Markdown")
    await asyncio.sleep(1)
    await callback.message.answer(text_step1_1, parse_mode="Markdown", reply_markup=excursion_menu1)
    await callback.answer()


# Обработчик кнопки "Вступление" из основного меню keyboards 
@router.message(lambda msg: msg.text in (EXCURSION_BUTTONS[0], EXCURSION_BUTTONS[1]))
async def intro(message: Message):
    await message.answer_voice(voice=audio_step1, caption="Вступление. Аудиоверсия")
    await asyncio.sleep(1)
    await message.answer_photo(photo_step1_1, caption="Рис1. Вид Мюнстера, 1881 год")
    await asyncio.sleep(2)
    await message.answer(text_step1, parse_mode="Markdown")
    await asyncio.sleep(1)
    await message.answer(text_step1_1, parse_mode="Markdown", reply_markup=excursion_menu1)


# Обработчик инлайн кнопки "Замок Мюнстер"  
@router.callback_query(lambda c: c.data == "SchlossM")
@with_lock
async def handle_intro(callback: CallbackQuery):
    await callback.message.answer_voice(voice=audio_step2, caption="Замок Мюнстера. Аудиоверсия")
    await asyncio.sleep(1)
    await callback.message.answer_photo(photo_step2_1, caption="Рис1. Замок Мюнстера")
    await asyncio.sleep(2)
    await callback.message.answer(text_step2, parse_mode="Markdown")
    await asyncio.sleep(1)
    await callback.message.answer(text_step2_1, parse_mode="Markdown", reply_markup=excursion_menu1)
    await callback.answer()


# Обработчик инлайн кнопки "Юбервассеркирхе"  
@router.callback_query(lambda c: c.data == "UberWasser")
@with_lock
async def handle_intro(callback: CallbackQuery):
    await callback.message.answer_voice(voice=audio_step3, caption="Юбервассеркирхе. Аудиоверсия")
    await asyncio.sleep(1)
    await callback.message.answer_photo(photo_step3_1, caption="Рис1. Юбервассеркирхе")
    await asyncio.sleep(2)
    await callback.message.answer(text_step3, parse_mode="Markdown")
    await asyncio.sleep(1)
    await callback.message.answer(text_step3_1, parse_mode="Markdown", reply_markup=excursion_menu1)
    await callback.answer()


# ------------------ Конец обработки кнопок маршрута (все подряд) ------------------------











#### -------------------Два обработчика вызова карты google (inline , keyboards) -----------###

#Вызов карты экскурсии (Google maps) через основное меню keyboards
@router.message(lambda msg: msg.text  in (EXCURSION_BUTTONS[21]))
async def menu_map(message: Message):
    await message.answer(
        ' [Google maps](https://www.google.com/maps/d/edit?mid=1LzsQNhwI7wxI9ZatG7Ohu-dyYlFOn-Q&usp=sharing)',
        parse_mode="Markdown", reply_markup=excursion_menu1
    )



# #Посмотреть точки маршрута  (кнопка 10)
# @router.message(lambda msg: msg.text  in (EXCURSION_BUTTONS[10]))
# async def menu_back(message: Message):
#     await message.answer( "Первые 5 точек маршрута",
#          reply_markup=excursion_menu1
#     )
#### -------------------Два обработчика вызова карты google (inline , keyboards) -----------###

####################------------------Обработка кнопок "Вперед"--------------#######################
#Вперед к кнопкам 6-9  (кнопка 18)

@router.callback_query(lambda c: c.data == "Weiter")
@with_lock
async def show_excursion_menu2(callback: CallbackQuery):
    await callback.message.answer(
        "Следующие 5 точек маршрута",
        reply_markup=excursion_menu2
    )
    #print("Нажата кнопка Weiter")
    await callback.answer()

#Вперед к кнопкам 10-13  (кнопка 25)

@router.callback_query(lambda c: c.data == "Weiter2")
@with_lock
async def show_excursion_menu3(callback: CallbackQuery):
    await callback.message.answer(
        "Последние точки маршрута",
        reply_markup=excursion_menu3
    )
    await callback.answer()

#Вперед к кнопкам 14-17  (кнопка 27)

@router.callback_query(lambda c: c.data == "Weiter3")
@with_lock
async def show_excursion_menu3(callback: CallbackQuery):
    await callback.message.answer(
        "Последние точки маршрута",
        reply_markup=excursion_menu4
    )
    await callback.answer()

####################------------------Обработка кнопок "Назад"--------------#######################
# #Назад к кнопкам 1-5  (кнопка 24)

@router.callback_query(lambda c: c.data == "Zuruck2")
@with_lock
async def back_excursion_menu1(callback: CallbackQuery):
    await callback.message.answer(
        "Предыдушие 5 точек маршрута",
        reply_markup=excursion_menu1
    )
    await callback.answer()

# #Назад к кнопкам 6-9  (кнопка 26)

@router.callback_query(lambda c: c.data == "Zuruck3")
@with_lock
async def back_excursion_menu2(callback: CallbackQuery):
    await callback.message.answer(
        "Предыдушие 5 точек маршрута",
        reply_markup=excursion_menu2
    )
    await callback.answer()

# #Назад к кнопкам 10-13  (кнопка 28)

@router.callback_query(lambda c: c.data == "Zuruck4")
@with_lock
async def back_excursion_menu2(callback: CallbackQuery):
    await callback.message.answer(
        "Предыдушие 5 точек маршрута",
        reply_markup=excursion_menu3
    )
    await callback.answer()


