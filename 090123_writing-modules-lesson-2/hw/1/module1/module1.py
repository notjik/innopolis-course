"""
Есть список:

a = [1, 2, 3, 3, 4, 5]


Требуется написать функцию в отдельном модуле, которая проверяет все ли числа в данном списке, являются уникальными.
"""


def unique(lst: list) -> str:
    return 'Все числа уникальные' if len(lst) == len(set(lst)) else 'Не все числа уникальные'


if __name__ == '__main__':
    raise SystemExit('Используйте файл как модуль с функциями.')