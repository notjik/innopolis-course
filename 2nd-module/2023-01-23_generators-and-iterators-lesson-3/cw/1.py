"""↓ collaborations ↓"""
# def gen1(stop):
#     n = 1
#     while n <= stop:
#         yield n
#         n += 1
#
#
# def gen2(start):
#     n = start
#     while n > 0:
#         yield n
#         n -= 1
#
#
# def func(n):
#     yield from gen1(n)
#     yield from gen2(n)
#
#
# for n in func(10):
#     print(n, end=' ')


# numbers = [1, 2, [3, [4, 5, 6, 7], 8, 9], 10]
#
# def func(n):
#    for i in n:
#        if isinstance(i, list):
#            yield from func(i)
#        else:
#            yield i
#
# for i in func(numbers):
#    print(i, end=' ')


# def func():
#     while True:
#         n = yield
#         print(n)
#
#
# r = func()
# r.send(None)
# r.send(1)
# # r.close()
# r.send(2)
#
# r = func()
# r.throw(RuntimeError, "Ошибка")


# class MyClass:  # создание класса MyClass
#     def __init__(self):
#         self.data = bytearray()
#         self.linecount = 0
#
#     def send(self, part):  # функция отправки send()
#         self.linecount += part.count(b'\n')
#         self.data.extend(part)
#         if self.linecount > 0:
#             index = self.data.index(b'\n')
#             line = bytes(self.data[:index + 1])
#             self.data = self.data[index + 1:]
#             self.linecount -= 1
#             return line
#         else:
#             return None
#
#
# def func():
#     data = bytearray()
#     line = None
#     linecount = 0
#     while True:
#         part = yield line
#         linecount += part.count(b'\n')
#         data.extend(part)
#         if linecount > 0:
#             index = data.index(b'\n')
#             line = bytes(data[:index + 1])
#             data = data[index + 1:]
#             linecount -= 1
#         else:
#             line = None
#
#
# r = func()
# print(r.send(None))
# print(r.send(b'hello'))
# print(r.send(b'world\nit '))
# print(r.send(b'works!'))
# print(r.send(b'\n'))


"""↓ personal work ↓"""
"""
Задача 1
Написать генератор кортежа чисел от 5 до 25 включительно. Вывести весь кортеж, первое число, 
последнее число и последние 5 чисел
"""
# a = tuple(i for i in range(5, 26))
# print(a, a[0], a[-1], a[-5:])


"""
Задача 2
Написать программу, которая считываем числа с консоли через запятую 
и выводит только числа кратные 3 или 5 через запятую в одну строку
"""
print(*[i for i in map(int, input().split(',')) if not i % 3 or not i % 5], sep=', ')
