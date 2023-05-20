import logging
import sqlite3
import os

from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text, Command
from aiogram.types import BotCommandScopeDefault, BotCommand, BotCommandScopeChat
from dotenv import load_dotenv

load_dotenv()

# Объект бота
bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


class Database:
    def __init__(self, path_to_db='test.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_users(self):
        sql = """
       CREATE TABLE Users(
       id int NOT NULL,
       name varchar(255) NOT NULL,
       email varchar(255),
       PRIMARY KEY (id)
       );
       """
        return self.execute(sql)

    def add_user(self, id: int, name: str, email: str = None):
        sql = "INSERT INTO Users (id, name, email) VALUES (?, ?, ?)"
        parameters = (id, name, email)
        self.execute(sql, parameters=parameters, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_email(self, email, id):
        sql = "UPDATE Users SET email=? WHERE id=?"
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_all_users(self):
        self.execute("DELETE FROM Users WHERE TRUE")


def logger(statement):
    print(f"""
___________________________
EXECUTING
{statement}
___________________________
""")


db = Database()

try:
    db.create_table_users()
    print('Таблица создана')
except Exception as e:
    print(e)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count_users = db.count_users()[0]
    await message.answer(
        '\n'.join([
            f'Привет, {message.from_user.full_name}!',
            'Ты был занесен в базу данных',
            f'В базе данных {count_users} пользователей'
        ])
    )


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
