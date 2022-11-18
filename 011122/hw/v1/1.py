print('Для выхода введите exit.\n')
tmp = input('Введите номер месяца (1-12): ').strip()
while tmp != 'exit':
    if not (tmp.isdigit()):
        print('Введите числовое значение.')
    elif int(tmp) == 12 or int(tmp) <= 2:
        print('Зима.')
    elif 3 <= int(tmp) <= 5:
        print('Весна.')
    elif 6 <= int(tmp) <= 8:
        print('Лето.')
    elif 9 <= int(tmp) <= 11:
        print('Осень.')
    else:
        print('Введите корректное значение.')
    tmp = input('Введите номер месяца (1-12): ').strip()
