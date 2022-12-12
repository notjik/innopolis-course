"""
Написать программу список дел, которая спрашивает у пользователя значение n, после этого запрашивает на ввод n строк
различных дел и сохраняет их в список, а после записывает значения из списка через одно в файл в одну строку.
"""
while True:
    try:
        n = int(input('Введите количество дел: '))
        cases = []
        while n:
            cases.append(input('Введите дело: '))
            n -= 1
        with open('cases.txt', 'w') as f:
            f.write(''.join([case for i, case in enumerate(cases) if not(i % 2)]))
            print('Done!')
            exit(0)
    except ValueError:
        print('Вводите корректные значения')
    except Exception as e:
        print(e)
