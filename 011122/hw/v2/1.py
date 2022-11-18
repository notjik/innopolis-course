if __name__ == '__main__':
    login = input('Введите логин: ').strip()
    while not login:
        login = input('Введите логин: ').strip()
    password = input('Введите пароль: ').strip()
    while not password:
        password = input('Введите пароль: ').strip()
    print(f'{login}: {password}')