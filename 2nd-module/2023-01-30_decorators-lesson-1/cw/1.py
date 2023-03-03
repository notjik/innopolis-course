"""↓ collaborations ↓"""


def decorator(func):
    def wrapper():
        print('функция-оболочка')
        func()

    return wrapper


def basic():
    print('основная функция')


wrapped = decorator(basic)
print('старт программы')
basic()
wrapped()
print('конец программы')
