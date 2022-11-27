"""
Реализовать программу, которая принимает на вход числа a, b.

Результатом работы должно быть среднее значение всех чисел от a до b включительно, которые делятся на 3,
среднее значение находится, как сумма чисел разделенное на количество.
"""
while True:
    tmp = list(map(lambda x: x.strip(), input('Введите два числа через пробел: ').split()))[:2]
    while not (tmp[0].isdecimal() or tmp[-1].isdecimal()):
        tmp = list(map(lambda x: x.strip(), input('Введите два числа через пробел: ').split()))[:2]
    a, b = map(int, tmp)
    lst = [i for i in range(int(tmp[0]), int(tmp[-1]) + 1) if not (i % 3)]
    try:
        avg = sum(lst) / len(lst)
        print(f'Среднее значение: {avg}')
        break
    except ZeroDivisionError as f:
        print(f'В выбранном промежутке нет чисел, делящихся на три.\nОшибка: {f}\n\n')
