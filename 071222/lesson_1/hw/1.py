"""
Написать простой калькулятор с использованием функций.
"""


def plus(a: float, b: float) -> float:
    return a + b


def minus(a: float, b: float) -> float:
    return a - b


def multi(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    return a / b


while True:
    action = input('Введите операцию (с двумя числами через пробел): ').split(' ')
    print()
    if len(action) != 3 and not (action[0].isdigit() and action[-1].isdigit()):
        continue
    if action[1] == '+':
        print('Сумма чисел: {}'.format(plus(float(action[0]), float(action[2]))))
    if action[1] == '-':
        print('Разность чисел: {}'.format(minus(float(action[0]), float(action[2]))))
    if action[1] == '*':
        print('Произведение чисел: {}'.format(multi(float(action[0]), float(action[2]))))
    if action[1] == '/':
        print('Частное чисел: {}'.format(div(float(action[0]), float(action[2]))))
    break
