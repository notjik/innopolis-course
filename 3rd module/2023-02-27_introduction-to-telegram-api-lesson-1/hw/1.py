"""
Реализовать запрос на отправку копии сообщения пользователю, который отправил его боту.
"""
# *You need to download: "aiogram", "python-dotenv"*
# *You need to add a token to the environment variable*

# Imports for working with a bot
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Token transfer and class definition
bot = Bot(token=os.getenv('TOKEN_SECOND'))
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
    print('{}{}[{}]{} in {}{}{} send {}{}{}: \n{}{}{}\n'.format(ansi_color['blue']['text'] + ansi_effect['bold'],
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
                                                                ansi_effect['break']))  # Logging message


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
    await msg.answer('Hi! Welcome to the bot from the second assignment of the Innopolis University course.\n'
                     'This is an improved echo bot.')  # Request with a message to the user


@dispatcher.message_handler(content_types=['text'])
async def echo_text(msg: types.Message):
    """
    Echo text function.

    :param msg: message object
    :return: send message
    """
    logging(msg, 'text', msg.text)  # Calling the logger
    await bot.copy_message(chat_id=msg.chat.id,
                           from_chat_id=msg.chat.id,
                           message_id=msg.message_id)  # Request with text to the user


@dispatcher.message_handler(content_types=['sticker'])
async def echo_sticker(msg: types.Message):
    """
    Echo sticker function.

    :param msg: message object
    :return: send sticker
    """
    logging(msg, 'sticker', '{}'.format(msg.sticker.file_id))  # Calling the logger
    await bot.send_sticker(chat_id=msg.chat.id,
                           sticker=msg.sticker)  # Request with a sticker to the user


@dispatcher.message_handler(content_types=['audio'])
async def echo_audio(msg: types.Message):
    """
    Echo audio function.

    :param msg: message object
    :return: send audio
    """
    logging(msg, 'audio', '{}'.format(msg.audio.file_id))  # Calling the logger
    await bot.send_audio(chat_id=msg.chat.id,
                         audio=msg.audio.file_id,
                         caption=msg.caption)  # Request with audio to the user


@dispatcher.message_handler(content_types=['photo'])
async def echo_photo(msg: types.Message):
    """
    Echo photo function.

    :param msg: message object
    :return: send photo
    """
    logging(msg, 'photo', '{}'.format(msg.photo[-1].file_id))  # Calling the logger
    await bot.send_photo(chat_id=msg.chat.id,
                         photo=msg.photo[-1].file_id,
                         caption=msg.caption)  # Request with photo to the user


@dispatcher.message_handler(content_types=['document'])
async def echo_document(msg: types.Message):
    """
    Echo document function.

    :param msg: message object
    :return: send document
    """
    logging(msg, 'document', '{}'.format(msg.document.file_id))  # Calling the logger
    await bot.send_document(chat_id=msg.chat.id,
                            document=msg.document.file_id,
                            caption=msg.caption)  # Request with document to the user


@dispatcher.message_handler(content_types=['voice'])
async def echo_voice(msg: types.Message):
    """
    Echo voice function.

    :param msg: message object
    :return: send voice
    """
    logging(msg, 'voice', '{}'.format(msg.voice.file_id))  # Calling the logger
    await bot.send_voice(chat_id=msg.chat.id,
                         voice=msg.voice.file_id)  # Request with voice to the user


@dispatcher.message_handler(content_types=['location'])
async def echo_location(msg: types.Message):
    """
    Echo location function.

    :param msg: message object
    :return: send location
    """
    logging(msg, 'location',
            'lat {}\n lon{}'.format(msg.location.latitude, msg.location.longitude))  # Calling the logger
    await bot.send_location(chat_id=msg.chat.id,
                            longitude=msg.location.longitude,
                            latitude=msg.location.latitude)  # Request with location to the user


@dispatcher.message_handler(content_types=['contact'])
async def echo_contact(msg: types.Message):
    """
    Echo contact function.

    :param msg: message object
    :return: send contact
    """
    logging(msg,
            'contact',
            'First Name: {}\nLast Name: {}\nPhone Number: {}\nVCard: {}\n'.format(
                msg.contact.first_name,
                msg.contact.last_name,
                msg.contact.phone_number,
                msg.contact.vcard)
            )  # Calling the logger
    await bot.send_contact(chat_id=msg.chat.id,
                           phone_number=msg.contact.phone_number,
                           first_name=msg.contact.first_name,
                           last_name=msg.contact.last_name,
                           vcard=msg.contact.vcard)  # Request with contact to the user


@dispatcher.message_handler(content_types=['video'])
async def echo_video(msg: types.Message):
    """
    Echo video function.

    :param msg: message object
    :return: send video
    """
    logging(msg, 'video', '{}'.format(msg.video.file_id))  # Calling the logger
    await bot.send_video(chat_id=msg.chat.id,
                         video=msg.video.file_id,
                         caption=msg.caption)  # Request with video to the user


@dispatcher.message_handler(content_types=['video_note'])
async def echo_video_note(msg: types.Message):
    """
    Echo video note function.

    :param msg: message object
    :return: send video note
    """
    logging(msg, 'video_note', '{}'.format(msg.video_note.file_id))  # Calling the logger
    await bot.send_video_note(chat_id=msg.chat.id,
                              video_note=msg.video_note.file_id)  # Request with video note to the user


# Entry point
if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=startup, on_shutdown=shutdown)  # Launching the bot
