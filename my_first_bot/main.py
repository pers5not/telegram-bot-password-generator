import asyncio
import aiogram
from aiogram import Bot, Dispatcher, executor
from pip import main
from config import BOT_TOKEN

# Создаем поток в котором будут обрабатываться все события
# Обязательно для работы с асинхронной библиотекой
loop = asyncio.get_event_loop()
# Создаем бота и передаем в него BOT_TOKEN
# Передаем parse_mode="HTML" для форматирования текста
# <i>....</i> - писать курсивом
# <b>....</b> - жирый текст
# Подробнее о форматировании смотреть html (тэги)
bot = Bot(BOT_TOKEN, parse_mode="HTML")
# Создаем обработчик и доставщи Dispatcher
dp = Dispatcher(bot, loop=loop)


if __name__ == "__main__":
    from handlers import dp, send_to_admin
    # Функция aiogram которая делает get_Updates offset ... и прочее
    # Доставляет нам сообщения
    executor.start_polling(dp, on_startup=send_to_admin)
