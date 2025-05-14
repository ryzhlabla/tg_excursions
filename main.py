from aiogram import Bot, Dispatcher
import asyncio
from menu_router import router as menu_router
from excursion_router import router as excursion_router
#from map_router import router as map_router

# Токен бота
from Config import TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Регистрируем все роутеры
    dp.include_router(menu_router)
    dp.include_router(excursion_router)
  #  dp.include_router(map_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot остановлен!")
