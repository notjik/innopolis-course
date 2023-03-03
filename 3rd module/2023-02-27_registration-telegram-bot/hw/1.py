"""
Зарегистрировать своего бота и реализовать эхо бота в Телеграм.
"""

import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TOKEN_FIRST'))
dispatcher = Dispatcher(bot)

ansi_effect = {
    'break': '\033[0m',
    'bold': '\033[1m',
    'fade': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'rflash': '\033[5m',
    'fflash': '\033[6m',
    'cbgtx': '\033[7m',
    'crossout': '\033[8m',
    'dunderline': '\033[21m',
    'framed': '\033[51m',
    'circled': '\033[52m',
    'overlined': '\033[53m',
}

ansi_color = {
    'black': {
        'text': '\033[30m',
        'background': '\033[40m',
    },
    'red': {
        'text': '\033[31m',
        'background': '\033[41m',
    },
    'green': {
        'text': '\033[32m',
        'background': '\033[42m',
    },
    'yellow': {
        'text': '\033[33m',
        'background': '\033[43m',
    },
    'blue': {
        'text': '\033[34m',
        'background': '\033[44m',
    },
    'purple': {
        'text': '\033[35m',
        'background': '\033[45m',
    },
    'turquoise': {
        'text': '\033[36m',
        'background': '\033[46m',
    },
    'white': {
        'text': '\033[37m',
        'background': '\033[47m',
    },
}


async def startup(callback):
    me = await callback.bot.get_me()
    print('{}The {}{}[{}]{} has been successfully launched.{}\n'.format(
        ansi_color['green']['text'],
        ansi_effect['bold'],
        me.username, me.id,
        ansi_effect['break'] + ansi_color['green']['text'],
        ansi_effect['break']))


async def shutdown(callback):
    me = await callback.bot.get_me()
    print('\n{}The {}{}[{}]{} is disabled.{}'.format(
        ansi_color['green']['text'],
        ansi_effect['bold'],
        me.username, me.id,
        ansi_effect['break'] + ansi_color['green']['text'],
        ansi_effect['break']))


@dispatcher.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    print('{}[{}] in {} send /start'.format(msg.from_user.username, msg.from_user.id, msg.date, msg.text))
    await msg.answer('Hi! Welcome to the bot from the first assignment of the Innopolis University course.\n'
                     'This is an echo bot.')


@dispatcher.message_handler()
async def echo(msg: types.Message):
    print('{}[{}] in {}: {}'.format(msg.from_user.username, msg.from_user.id, msg.date, msg.text))
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=startup, on_shutdown=shutdown)
