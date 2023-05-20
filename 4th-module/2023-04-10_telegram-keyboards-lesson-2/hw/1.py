"""
Написать бота с клавиатурой для отправки локации.
"""
import os
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
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


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.reply('Send location to get coordinates',
                        reply_markup=ReplyKeyboardMarkup(resize_keyboard=True
                                                         ).add(KeyboardButton('Send location',
                                                                              request_location=True)))


@dp.message_handler(content_types=['location'])
async def geo(message: Message):
    await message.reply("Your coordinates\nLatitude: {}\nLongitude: {}".format(message.location.latitude,
                                                                               message.location.longitude))


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
