print('Для выхода введите exit.\n')
tmp = input('Пользователь ввел число ').strip()
while tmp != 'exit':
    if not (tmp.lstrip('-').isdigit()):
        print('Введите число\n')
    else:
        tmp1 = abs(int(tmp))
        if 5 <= tmp1 % 100 <= 20:
            print(f'{tmp} компьютеров\n')
        elif 2 <= tmp1 % 10 <= 4:
            print(f'{tmp} компьютера\n')
        elif tmp1 % 10 == 1:
            print(f'{tmp} компьютер\n')
        else:
            print(f'{tmp} компьютеров\n')

    tmp = input('Пользователь ввел число ').strip()
