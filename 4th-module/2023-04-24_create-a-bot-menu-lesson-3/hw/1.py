"""
Реализовать простого бота который выводит курс рубля по отношению к юаню.
"""
import os
import logging
import aiohttp

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from dotenv import load_dotenv

logging.basicConfig(level='INFO')
load_dotenv()

try:
    WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
    WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')
    WEBHOOK_URL = WEBHOOK_HOST + WEBHOOK_PATH
    WEBAPP_HOST = os.getenv('WEBAPP_HOST')
    WEBAPP_PORT = os.getenv('WEBAPP_PORT')
    bot = Bot(token=os.getenv('TOKEN'))
except TypeError as e:
    exit('Create local variables: {}'.format(e))
dp = Dispatcher(bot=bot)


async def startup(callback):
    await bot.set_webhook(WEBHOOK_URL)


async def shutdown(callback):
    await bot.delete_webhook()


async def get_exchange(f_val, s_val):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://open.er-api.com/v6/latest/{}'.format(f_val)) as response:
            resp = await response.json()
            return resp['rates'][s_val]


@dp.message_handler(commands=['exchange'])
async def exchange_RUB_CNY(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    exchange = await get_exchange('RUB', 'CNY')
    await bot.send_message(message.chat.id, 'For 1 ruble you will get {} yuan'.format(exchange) if exchange >= 1
    else 'For 1 yuan you will get {} rubles'.format(1 / exchange))


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        on_startup=startup,
        on_shutdown=shutdown,
        skip_updates=True,
    )  # Launching webhook