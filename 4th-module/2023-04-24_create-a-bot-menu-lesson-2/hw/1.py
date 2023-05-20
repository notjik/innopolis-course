"""
Создать бота по опросу любимых жанров фильма.
"""
import os
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
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
dp = Dispatcher(bot=bot, storage=MemoryStorage())


class MovieAnswersFSM(StatesGroup):
    action = State()
    drama = State()
    comedy = State()
    documentary = State()


async def startup(callback):
    await bot.set_webhook(WEBHOOK_URL)


async def shutdown(callback):
    await bot.delete_webhook()


@dp.message_handler(commands=['start'])
async def start(message: Message, state: FSMContext):
    await bot.delete_message(message.chat.id, message.message_id)
    call = CallbackQuery()
    call.message = await bot.send_message(message.chat.id, 'Вы начали опрос.')
    await action(call=call, state=state)


@dp.callback_query_handler(lambda call: call.data and call.data.startswith('action'))
async def action(call: CallbackQuery, state: FSMContext):
    await call.bot.edit_message_text(text='Rate the last watched movie in the genre of "Action" from 1 to 5, where\n\n'
                                          '1 - terrible\n5 - a masterpiece',
                                     chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=InlineKeyboardMarkup(row_width=5).add(
                                         InlineKeyboardButton('1', callback_data='from_action:1'),
                                         InlineKeyboardButton('2', callback_data='from_action:2'),
                                         InlineKeyboardButton('3', callback_data='from_action:3'),
                                         InlineKeyboardButton('4', callback_data='from_action:4'),
                                         InlineKeyboardButton('5', callback_data='from_action:5'),
                                     ))
    await MovieAnswersFSM.action.set()


@dp.callback_query_handler(lambda call: call.data and call.data.startswith('from_action'), state=MovieAnswersFSM.action)
async def drama(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['action'] = int(call.data.split(':')[-1])
    await call.bot.edit_message_text(text='Rate the last watched movie in the genre of "Drama" from 1 to 5, where\n\n'
                                          '1 - terrible\n5 - a masterpiece',
                                     chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=InlineKeyboardMarkup(row_width=5).add(
                                         InlineKeyboardButton('1', callback_data='from_drama:1'),
                                         InlineKeyboardButton('2', callback_data='from_drama:2'),
                                         InlineKeyboardButton('3', callback_data='from_drama:3'),
                                         InlineKeyboardButton('4', callback_data='from_drama:4'),
                                         InlineKeyboardButton('5', callback_data='from_drama:5'),
                                     ))
    await MovieAnswersFSM.next()


@dp.callback_query_handler(lambda call: call.data and call.data.startswith('from_drama'), state=MovieAnswersFSM.drama)
async def comedy(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['drama'] = int(call.data.split(':')[-1])
    await call.bot.edit_message_text(text='Rate the last watched movie in the genre of "Comedy" from 1 to 5, where\n\n'
                                          '1 - terrible\n5 - a masterpiece',
                                     chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=InlineKeyboardMarkup(row_width=5).add(
                                         InlineKeyboardButton('1', callback_data='from_comedy:1'),
                                         InlineKeyboardButton('2', callback_data='from_comedy:2'),
                                         InlineKeyboardButton('3', callback_data='from_comedy:3'),
                                         InlineKeyboardButton('4', callback_data='from_comedy:4'),
                                         InlineKeyboardButton('5', callback_data='from_comedy:5'),
                                     ))
    await MovieAnswersFSM.next()


@dp.callback_query_handler(lambda call: call.data and call.data.startswith('from_comedy'), state=MovieAnswersFSM.comedy)
async def documentary(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['comedy'] = call.data.split(':')[-1]
    await call.bot.edit_message_text(text='Rate the last watched movie in the genre of "Documentary" '
                                          'from 1 to 5, where\n\n'
                                          '1 - terrible\n5 - a masterpiece',
                                     chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=InlineKeyboardMarkup(row_width=5).add(
                                         InlineKeyboardButton('1', callback_data='from_documentary:1'),
                                         InlineKeyboardButton('2', callback_data='from_documentary:2'),
                                         InlineKeyboardButton('3', callback_data='from_documentary:3'),
                                         InlineKeyboardButton('4', callback_data='from_documentary:4'),
                                         InlineKeyboardButton('5', callback_data='from_documentary:5'),
                                     ))
    await MovieAnswersFSM.next()


@dp.callback_query_handler(lambda call: call.data and call.data.startswith('from_documentary'),
                           state=MovieAnswersFSM.documentary)
async def result(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['documentary'] = call.data.split(':')[-1]
        await call.bot.edit_message_text(text='Ratings:\n'
                                              'Action — {}\n'
                                              'Drama — {}\n'
                                              'Comedy — {}\n'
                                              'Documentary — {}'.format(data['action'],
                                                                        data['drama'],
                                                                        data['comedy'],
                                                                        data['documentary']),
                                         chat_id=call.message.chat.id,
                                         message_id=call.message.message_id)
    await state.finish()


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
