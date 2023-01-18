from functools import reduce

"""
Найдите сумму и произведение элементов списка. Результаты вывести в консоль.
"""

def check(lst: list) -> bool:
    for i in lst:
        if not (i.isdigit()):
            return False
    return True


if __name__ == '__main__':
    print('Для выхода введите exit.\n')
    tmp = input('Введите числа через пробел для получения суммы и произведения списка: ').strip()
    while tmp != 'exit':
        if ' ' in tmp:
            lst = list(map(lambda x: x.strip(), tmp.split()))
            if check(lst):
                print(f'Сумма элементов списка: {sum(map(int, lst))}\n'
                      f'Произведение элементов списка: {reduce(lambda a, b: a * b, map(int, lst))}\n')
            else:
                print('Введите числовое значение.\n')

        else:
            print('Введённое значение некорректно.\n')
        tmp = input('Введите числа через пробел для получения суммы и произведения списка: ').strip()
