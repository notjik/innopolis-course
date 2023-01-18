"""↓ collaborations ↓"""
import sys
import os

# file = open('example.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()

# file = open('example.txt', 'a')
# file.write('\npython')
# file.close()
# file = open('example.txt', 'r')
# print(file.read())
# file.close()

# os.rename("example2.txt", "example3.txt")


# def read_file(file_name):
#     with open(file_name, 'r') as lines:
#         line = lines.readline()
#         os.rename(file_name, 'example4.txt')
#         return line
#
#
# file_name = input()
# print(read_file(file_name))


"""↓ personal work ↓"""
'''
Задача 1
Написать функцию, которая принимает у пользователя имя файла example3.txt. Заранее
стоит создать данный файл и записать туда несколько строк. Функция должна вернуть
первую строку записанную в данный файл, а после переименовать его в example4.txt
'''


def func(s):
    while True:
        try:
            with open(s, encoding='utf-8') as f:
                data = f.readlines()
            with open(s, 'w', encoding='utf-8') as f:
                f.writelines(data + [i for i in sys.stdin])
            os.rename(s, 'example4.txt')
            return 'done'
        except FileNotFoundError:
            return 'Некорректный ввод'


print(func(input()))
