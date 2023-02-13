"""
Написать модуль с функциями суммы, вычитания, умножения, деления.

В основном файле создать консольную программу калькулятор и воспользоваться для расчета функциями из модуля.
"""
import os
from sys import platform
from package1.module1 import *


class Calculator:
    def __init__(self) -> None:
        self.window()

    def window(self) -> None:
        while True:
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
            print('\nОперации:\n 1: +\n 2: -\n 3: *\n 4: /\n 5: //\n 6: %\n 7: ^\n 0: Выход\n')
            choice = input('Выберите операцию: ')
            if choice.isdigit():
                choice = int(choice)
            match ''.join(choice.lower().replace('ё', 'е').split()) if isinstance(choice, str) else choice:
                case 'esc' | 'escape' | 'выход' | 0:
                    print(platform.lower().startswith('win'))
                    os.system('cls') if platform.lower().startswith('win') else os.system('clear')
                    break
                case '+' | 'add' | 'addition' | 'сложение' | 'плюс' | 1:
                    print('Результат:', add(num1, num2))
                case '-' | 'sub' | 'subtraction' | 'вычитание' | 'минус' | 2:
                    print('Результат:', sub(num1, num2))
                case '*' | 'mul' | 'multiplication' | 'умножение' | 'звездочка' | 3:
                    print('Результат:', mul(num1, num2))
                case '/' | 'div' | 'division' | 'деление' | 'слэш' | 4:
                    print('Результат:', div(num1, num2))
                case '//' | 'fdiv' | 'floordivision' | 'целочисленноеделение' | 'слэшслэш' | 5:
                    print('Результат:', div(num1, num2))
                case '%' | 'mod' | 'modulardivision' | 'делениесостатком' | 'процент' | 6:
                    print('Результат:', div(num1, num2))
                case '^' | 'pow' | 'power' | 'степень' | 'карет' | 7:
                    print('Результат:', power(num1, num2))
                case _:
                    print('Некорректный выбор')


if __name__ == '__main__':
    run = Calculator()
