print('Для выхода введите exit.\n')
tmp = input('Введите длины сторон прямоугольника через пробел: ').strip()
while tmp != 'exit':
    if tmp.count(' ') == 1:
        a, b = map(lambda x: x.strip(), tmp.split())
        if a.isdigit() and b.isdigit():
            print(f'Площадь прямоугольника: {int(a) * int(b)}\nПериметр прямоугольника: {2 * (int(a) + int(b))}\n')
        else:
            print('Введите числовое значение.\n')

    else:
        print('Введённое значение некорректно.\n')
    tmp = input('Введите длины сторон прямоугольника через пробел: ').strip()