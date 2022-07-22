from cgitb import text
from requests import request
from main import bot, dp
from aiogram.types import Message
from config import admin_id


async def send_to_admin(dp):
    # аналог request.get("....")
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


# Декоратор который будет доставлять нам сообщения
@dp.message_handler()
async def echo(message: Message):
    text = f"Привет ты написал {message.text}"
    # await bot.send_message(chat_id=admin_id,
    #                        text=text)
# Вместо того чтоб постоянно прописывать  
# await bot.send_message(chat_id=admin_id,text=text)
# Пишем await message.answer(text=text) одно и тоже с верхней строчкой
    await message.answer(text=text)
                           
