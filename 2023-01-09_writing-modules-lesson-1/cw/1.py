"""↓ collaborations ↓"""
# from random import randint as rint
#
# print(rint(1, 10))


# from math import pi
#
# print(pi)


# from test import *
# print(func())
# obj = MyClass()
# print(number) # ошибка


# from calc import add, sub, mul, div
#
#
# class Calculator:
#     """"""
#     def __init__(self) -> None:
#         self.main()
#
#     def main(self):
#         print('Это калькулятор')
#         while True:
#             num1 = int(input('Введите первое число: '))
#             num2 = int(input('Введите второе число: '))
#             choice = int(input('Выберите необходимое действие 1: +, 2: -, 3: *, 4: /, 0: Выход\n'))
#             match choice:
#                 case 0:
#                     print('Для завершения нажмите Enter')
#                     input()
#                     break
#                 case 1:
#                     print(add(num1, num2))
#                 case 2:
#                     print(sub(num1, num2))
#                 case 3:
#                     print(mul(num1, num2))
#                 case 4:
#                     print(div(num1, num2))
#                 case _:
#                     print('Неверный выбор')
#
#
# obj = Calculator()

"""↓ personal work ↓"""
from calc import *


class Calculator:
    """"""
    def __init__(self) -> None:
        self.main()

    def main(self) -> None:
        print('Это калькулятор')
        while True:
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
            print('\nВозможные действия:\n 1: +\n 2: -\n 3: *\n 4: /\n 5: ^\n 0: Выход\n')
            choice = input('Выберите необходимое действие:')
            if choice.isdigit():
                choice = int(choice)
            match choice:
                case 'esc' | 0:
                    print('Для завершения нажмите Enter')
                    input()
                    break
                case '+' | 1:
                    print('Результат:', add(num1, num2))
                case '-' | 2:
                    print('Результат:', sub(num1, num2))
                case '*' | 3:
                    print('Результат:', mul(num1, num2))
                case '/' | 4:
                    print('Результат:', div(num1, num2))
                case '^' | 4:
                    print('Результат:', power(num1, num2))
                case _:
                    print('Неверный выбор')


obj = Calculator()