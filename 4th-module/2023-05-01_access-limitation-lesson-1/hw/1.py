"""
Реализовать бота с возможностью бана пользователя.
"""
import os
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import BadRequest
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


@dp.message_handler(commands=['ban'])
async def ban(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    users = message.get_args().split()
    success_ban = []
    error_ban = []
    for user in map(int, users):
        try:
            await bot.ban_chat_member(message.chat.id, user)
            success_ban.append(user)
        except BadRequest:
            error_ban.append(user)
    await bot.send_message(message.chat.id,
                           'Successfully' if len(users) == success_ban
                           else 'Successfully with errors' if success_ban
                           else 'Unsuccessful',
                           reply_markup=InlineKeyboardMarkup(row_width=1).add(
                               InlineKeyboardButton('Delete this message', callback_data='delete')))


@dp.callback_query_handler(text='delete')
async def delete_message(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


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
