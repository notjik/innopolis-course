"""
Написать модуль с функциями суммы, вычитания, умножения, деления.

В основном файле создать консольную программу калькулятор и воспользоваться для расчета функциями из модуля.
"""


def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2


def sub(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2


def mul(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2


def div(num1: int | float, num2: int | float) -> float:
    try:
        return num1 / num2
    except ZeroDivisionError:
        return float("inf")


def mod(num1: int | float, num2: int | float) -> float:
    try:
        return num1 % num2
    except ZeroDivisionError:
        return float("inf")


def floordiv(num1: int | float, num2: int | float) -> float:
    try:
        return num1 // num2
    except ZeroDivisionError:
        return float("inf")


def power(num1: int | float, num2: int | float) -> int | float:
    return num1 ** num2


if __name__ == '__main__':
    raise SystemExit('Используйте файл как модуль с функциями.')
