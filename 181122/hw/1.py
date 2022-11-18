from math import factorial

tmp = input('Введите число для поиска факториала: ')
while not tmp.isdecimal():
    tmp = input('Введите число для поиска факториала: ')
print(factorial(int(tmp)))
