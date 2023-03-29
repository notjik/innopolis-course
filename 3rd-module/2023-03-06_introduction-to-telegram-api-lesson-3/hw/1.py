"""
Добавить в бота возможности приветствия на команду /start от пользователя, а также вывод справки о боте по команде /help.
"""
# *You need to download: "aiogram", "python-dotenv"*
# *You need to add a token to the environment variable*

# Imports for working with a bot
import os
import re

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Token transfer and class definition
bot = Bot(token=os.getenv('TOKEN_FOURTH'))
dispatcher = Dispatcher(bot)

# ANSI EFFECT CODE
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

# ANSI COLOR CODE
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


def logging(message: types.Message,
            type_content: str,
            content: str) -> None:
    """
    Procedure for logging actions with the bot to the console.
    :param message: message object
    :param type_content: str name type content
    :param content: str content
    :return: None
    """
    log = '{}{}[{}]{} in {}{}{} send {}{}{}: \n{}{}{}\n'.format(ansi_color['blue']['text'] + ansi_effect['bold'],
                                                                message.from_user.username,
                                                                message.from_user.id,
                                                                ansi_effect['break'] + ansi_color['blue']['text'],
                                                                ansi_color['yellow']['text'],
                                                                message.date,
                                                                ansi_effect['break'] + ansi_color['blue']['text'],
                                                                ansi_color['yellow']['text'],
                                                                type_content,
                                                                ansi_effect['break'] + ansi_color['blue']['text'],
                                                                ansi_color['turquoise']['text'] + ansi_effect['italic'],
                                                                content,
                                                                ansi_effect['break'])
    with open('logging.log', 'a', encoding="utf-8") as logfile:
        logfile.writelines(re.sub(r'\033\[\d+m', r'', log))  # Logging message in logfile
    print(log)  # Logging message in console


async def startup(callback):
    """
    Logging the launch of the bot

    :param callback: dispatcher object
    :return: None
    """
    me = await callback.bot.get_me()  # Request information about the bot.
    print('{}The {}{}[{}]{} has been successfully launched.{}\n'.format(
        ansi_color['green']['text'],
        ansi_effect['bold'],
        me.username, me.id,
        ansi_effect['break'] + ansi_color['green']['text'],
        ansi_effect['break']))  # Logging message


async def shutdown(callback):
    """
    Logging off the bot

    :param callback: dispatcher object
    :return: None
    """
    me = await callback.bot.get_me()  # Request information about the bot
    print('\n{}The {}{}[{}]{} is disabled.{}'.format(
        ansi_color['green']['text'],
        ansi_effect['bold'],
        me.username, me.id,
        ansi_effect['break'] + ansi_color['green']['text'],
        ansi_effect['break']))  # Logging message


@dispatcher.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    """
    The starting message of the bot

    :param msg: message object
    :return: answer
    """
    await msg.answer("Hi! Welcome to the bot from the fourth assignment of the Innopolis University course.\n"
                     "It's the echo bot again")  # Request with a message to the user


@dispatcher.message_handler(commands=['help'])
async def help_message(msg: types.Message):
    """
    The help message of the bot

    :param msg: message object
    :return: answer
    """
    await msg.answer("Just send me a message and I'll repeat it!")  # Request with a message to the user


@dispatcher.message_handler(content_types=['any'])
async def echo(msg: types.Message):
    """
    Echo function.

    :param msg: message object
    :return: send message
    """
    logging(msg, msg.content_type, '{}'.format(msg))  # Calling the logger
    await bot.copy_message(chat_id=msg.chat.id,
                           from_chat_id=msg.chat.id,
                           message_id=msg.message_id)  # Request to copy a message


# Entry point
if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=startup, on_shutdown=shutdown)  # Launching the bot