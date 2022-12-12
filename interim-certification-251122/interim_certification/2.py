from sys import stdin

"""
Реализовать программу, которая принимает от пользователя на ввод бесконечно целые числа.  
Если сумма введённых чисел равна нулю, программа выводит сумму квадратов введённых чисел.
"""
while True:
    print('Введите целые числа. Каждое новое число с новой строчки.\nДля остановки ввода: Ctrl+D\n\n')
    try:
        stream = [int(i.strip()) for i in stdin]
        if sum(stream) == 0:
            print(f'\nСумма квадратов чисел: {sum(map(lambda x: x**2, stream))}')
        else:
            print(f'\nСумма чисел: {sum(stream)}')
        break
    except ValueError as f:
        print(f'\nВведите корректное значение.\nКод ошибки: {f}\n\n')
