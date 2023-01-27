"""↓ collaborations ↓"""
# from calc import add, sub, mul, div
#
#
# class Calculator:
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
# if __name__ == '__main__':
#     obj = Calculator()


# import sys
# sys.path.append('Моя директория/')
# print(sys.path)


# def func(n):
#     n1 = n
#     n2 = int(str(n) * 2)
#     n3 = int(str(n) * 3)
#     print(n1 + n2 + n3)
#
#
# func(5)


"""↓ personal work ↓"""
print(sum([int(input('Введите число: ')) * i for i in range(1, 4)]))
