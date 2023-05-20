"""
Реализовать многоуровневое меню в боте.
"""
import os
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
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


menu_callbackdata = CallbackData('menu', 'lvl', 'row')


@dp.message_handler(commands=['start'])
async def start(message: Message):
    print('start cb')
    await bot.send_message(message.chat.id,
                           'Press some button',
                           reply_markup=InlineKeyboardMarkup(row_width=1).add(
                               InlineKeyboardButton('First', callback_data=menu_callbackdata.new(lvl=1, row=1)),
                               InlineKeyboardButton('Second', callback_data=menu_callbackdata.new(lvl=1, row=2)),
                               InlineKeyboardButton('Third', callback_data=menu_callbackdata.new(lvl=1, row=3)),
                               InlineKeyboardButton('Fourth', callback_data=menu_callbackdata.new(lvl=1, row=4))))
    await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(text='Home')
async def start_callback(call: CallbackQuery):
    await start(call.message)


@dp.callback_query_handler(menu_callbackdata.filter())
async def menu_callback(call: CallbackQuery, callback_data: dict):
    inline = InlineKeyboardMarkup(row_width=1)
    inline.add(InlineKeyboardButton('First',
                                    callback_data=menu_callbackdata.new(
                                        lvl=int(callback_data['lvl']) + 1,
                                        row=1)),
               InlineKeyboardButton('Second',
                                    callback_data=menu_callbackdata.new(
                                        lvl=int(callback_data['lvl']) + 1,
                                        row=2)),
               InlineKeyboardButton('Third',
                                    callback_data=menu_callbackdata.new(
                                        lvl=int(callback_data['lvl']) + 1,
                                        row=3)),
               InlineKeyboardButton('Fourth',
                                    callback_data=menu_callbackdata.new(
                                        lvl=int(callback_data['lvl']) + 1,
                                        row=4)),
               )
    if int(callback_data['lvl']) > 1:
        inline.add(
            InlineKeyboardButton('Back',
                                 callback_data=menu_callbackdata.new(
                                     lvl=int(callback_data['lvl']) - 1,
                                     row=callback_data['row'])),
            InlineKeyboardButton('Home', callback_data='Home'))
    elif int(callback_data['lvl']) == 1:
        inline.add(InlineKeyboardButton('Home', callback_data='Home'))
    await bot.send_message(call.message.chat.id,
                           'This is the {}th button of the {}th level.'.format(callback_data['row'],
                                                                               callback_data['lvl']),
                           reply_markup=inline)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


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
