"""↓ collaborations ↓"""
# def get_type(func):
#     def wrapper(*args, **kwargs):
#         print('Вызываем функцию')
#         result = func()
#         print(result)
#         print(f'Тип данных, возвращаемый функцией {type(result)}')
#
#     return wrapper()
#
#
# @get_type
# def func():
#     return None

import datetime

print(datetime.datetime.astimezone(datetime.datetime.now()))