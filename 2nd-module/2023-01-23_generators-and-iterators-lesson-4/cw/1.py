"""↓ collaborations ↓"""
# def func_gen(items):
#     if len(items) == 0:
#         yield []
#     else:
#         pi = items[:]
#         for i in range(len(pi)):
#             pi[0], pi[i] = pi[i], pi[0]
#             for p in func_gen(pi[1:]):
#                 yield [pi[0]] + p
#
#
# for p in func_gen([1, 2, 3]):
#     print(p)


"""↓ personal work ↓"""
'''
Задача №1
Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран
'''
# from functools import reduce
#
# dct = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# print(reduce(lambda x, y: x * y, [dct[i] for i in dct]))


'''
Задача №2
Создайте словарь из строки 'python' следующим образом: в качестве ключей возьмите буквы строки, 
а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
'''
s = 'pythonp'
print({i: s.count(i) for i in set(s)})

