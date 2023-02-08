"""
Реализовать программу, которая рассчитывает площадь и периметр прямоугольника и обработать все возможные ошибки
с помощью try..except.
"""
process = True
while process:
    try:
        a, b = map(float, input('Введите стороны прямоугольника через ";": ').split(';'))
        if a <= 0 or b <= 0:
            raise ValueError('Введены некорректные значения')
        operations = input('Введите, какую операцию хотите произвести\nПлощадь – s\tПериметр – p\nОперация: ')
        match operations.lower():
            case 's' | 'площадь' | 'area':
                print(f'Площадь прямоугольника: {a * b}')
            case 'p' | 'периметр' | 'perimeter':
                print(f'Периметр прямоугольника: {a * 2 + b * 2}')
            case _:
                raise ValueError('Введены некорректные значения')
        process = False
    except ValueError:
        print('Введены некорректные значения')
    except Exception as e:
        print(f'Непредвиденная ошибка: {e}')
