# Импортируем встроенные модули Python
import asyncio  # Для работы с асинхронной блокировкой
from functools import wraps  # Чтобы сохранять имя и метаданные функции
from aiogram.types import CallbackQuery  # Тип данных — входящий callback из Telegram

_user_locks: dict[int, asyncio.Lock] = {}

def get_user_lock(user_id: int) -> asyncio.Lock:

    if user_id not in _user_locks:
        _user_locks[user_id] = asyncio.Lock()  # создаём новый "замок"
    return _user_locks[user_id]  # возвращаем замок

def with_lock(func):
    @wraps(func)
    async def wrapper(callback: CallbackQuery, *args, **kwargs):
        user_id = callback.from_user.id
        lock = get_user_lock(user_id)
        if lock.locked():
            await callback.answer("⏳ Подождите, идёт загрузка...", show_alert=True)
            return

        async with lock:
            return await func(callback, *args, **kwargs)
    return wrapper