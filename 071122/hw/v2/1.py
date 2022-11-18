import datetime

'''Без учёта месяца (without months)'''
# now = int(datetime.date.today().strftime('%Y'))
# y = input('Введите свой год рождения: ').strip()
# while len(y) != 4 or not y.isdigit():
#     y = input('Введите свой год рождения: ').strip()
# print(f'Ваш возраст: {now-int(y)}')


'''С учётом месяца (with months)'''
while True:
    now = datetime.date.today()
    d = input('Введите день своего рождения (числом): ').strip()
    m = input('Введите месяц своего рождения (числом): ').strip()
    y = input('Введите свой год рождения (числом): ').strip()
    try:
        years = 0
        months = 0
        if now.day - int(d) < 0:
            months -= 1
        months += now.month - int(m)
        if -12 < months < 0:
            months += 12
            years -= 1
        elif 0 <= months < 12:
            pass
        else:
            raise ValueError
        years += now.year - int(y)
        print('\nС момента вашего рождения прошло:', end=' ')
        years1 = abs(int(years))
        if 5 <= years1 % 100 <= 20:
            print(f'{years} лет', end='')
        elif 2 <= years1 % 10 <= 4:
            print(f'{years} года', end='')
        elif years1 % 10 == 1:
            print(f'{years} год', end='')
        else:
            print(f'{years} лет', end='')
        if months:
            print(' и ', end='')
            months1 = abs(int(months))
            if 5 <= months1 % 100 <= 20:
                print(f'{months} месяцев\n')
            elif 2 <= months1 % 10 <= 4:
                print(f'{months} месяца\n')
            elif months1 % 10 == 1:
                print(f'{months} месяц\n')
            else:
                print(f'{months} месяцев\n')
    except ValueError:
        print('\nВведите корректное значение\n')
