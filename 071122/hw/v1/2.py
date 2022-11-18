def check(lst: list) -> bool:
    for i in lst:
        if not (i.isdigit()):
            return False
    return True


if __name__ == '__main__':
    print('Для выхода введите exit.\n')
    tmp = input('Введите числа через пробел для получения четных чисел: ').strip()
    while tmp != 'exit':
        if ' ' in tmp:
            lst = list(map(lambda x: x.strip(), tmp.split()))
            if check(lst):
                lst = list(map(int, lst))
                print('Чётные числа: ', end='')
                for i in lst:
                    if i == 237:
                        break
                    if not (i % 2):
                        print(i, end=' ')
                print('\n')
            else:
                print('Введите числовое значение.\n')

        else:
            print('Введённое значение некорректно.\n')
        tmp = input('Введите числа через пробел для получения четных чисел: ').strip()
