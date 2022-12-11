"""↓ collaborations ↓"""

# x = 5
#
#
# def func():
#     global x
#     x += 1
#
#
# func()
# print(x)


# def func():
#     x = 5
#     y = 10
#     return x, y
#
#
# result1, result2 = func()
# print(result1, result2)


# result = lambda x, y: x + y
# print(result(4, 5))

# def get_year(n):
#     if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
#         return 'Високосный'
#     else:
#         return 'Обычный'
#
#
# print(get_year(2000))

"""↓ personal work ↓"""


# Задача №1
def f(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return 'Високосный'
    return 'Обычный'


while True:
    try:
        print(f(int(input('Введите год для проверки: '))))
        break
    except ValueError:
        print('Введите корректное значение')
