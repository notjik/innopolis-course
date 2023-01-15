"""↓ collaborations ↓"""


# def get_name(name='Иван'):
#     print(name)
#     get_name()
#     get_name('Петр')


# class Car:
#     def __init__(self, speed, color='Yellow', owner=None) -> None:
#         self.speed = speed
#         self.color = color
#         self.owner = owner
#
#     def say_owner(self):
#         if self.owner:
#             print(f'Владелец {self.owner}')
#         else:
#             print('У данного автомобиля нет владельца')
#
#
# car1 = Car(100, 'green', 'Иван')
# car2 = Car(90, 'Blue')
# car1.say_owner()
# car2.say_owner()


# class MyClass:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#
# a = MyClass('Ivan')
# print(a.name)
# a.name = 'sergey'
# print(a.name)

# class Animal:
#     def __init__(self, name, breed='Без породы') -> None:
#         self.name = name
#         self.breed = breed
#
#     def __say_breed(self):
#         print(self.breed)
#
#
# cat = Animal('Барсик', 'Сибирский')
# cat._Animal__say_breed()
# dog = Animal('Тузик')
# dog._Animal__say_breed()

"""↓ personal work ↓"""
from turtle import *


class Animal:
    # TODO: Инициализирование
    def __init__(self, animal: str, name: str, breed=None) -> None:
        self.animal = animal  # Мы присваиваем аргумент "Название животного"
        self.name = name  # Мы присваиваем аргумент "Имя животного"
        self.breed = breed  # Мы присваиваем аргумент "Порода животного"

    # TODO: Рисование солнышка
    def _paint(self) -> None:
        if self.animal.lower() in ['черепаха', 'turtle']:  # Проверка на черепаху
            shape("turtle")  # Курсор в виде черепахи
            speed(100)  # Скорость
            color('red', 'yellow')  # Цвета
            begin_fill()  # Старт рисования с заливкой
            while True:
                forward(200)
                left(170)
                if abs(pos()) < 1:
                    break
            end_fill()  # Закончил рисовать
            mainloop()  # Окно открыто до нажатия на крестик


turt = Animal('Черепаха', 'Лёшка', breed='Логгерхед')  # Окно открыто до нажатия на крестик
turt._paint()  # Вызов функции рисования
