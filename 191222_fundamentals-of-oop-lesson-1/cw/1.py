"""↓ collaborations ↓"""


# def func():
#     pass
#
#
# class Test:
#     pass
#
#
# print(type(5))
# print(type('a'))
# print(type(5.5))
# print(type(True))
# print(type([1, 2]))
# print(type((5, 4)))
# print(type({1, 2}))
# print(type({'a': 2}))
# print(type(Test))
# print(type(func))


# class Person:
#     name = 'Иван'
#     age = 'Иванов'
#
#     def say(self):
#         print('Hello')
#
#
# person1 = Person()
# print(person1.name)
# person1.say()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Меня зовут {self.name}'


person1 = Person('Иван', 15)
person2 = Person('Петр', 14)
print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)
print(person1)


class Person:
    def __init__(self, name, last_name, age, num_class, level):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.num_class = num_class
        self.level = level

    def do_homework(self):
        print('Делаю уроки')

    def answer_in_class(self):
        print('Отвечаю на уроке')


person1 = Person('Иван', 'Иванов', 15, '7A', 'Excellent student')
