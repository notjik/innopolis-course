"""↓ collaborations ↓"""
# class Transport:
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#
#     def beep(self):
#         print('beep')
#
#
# class Car(Transport):
#     def __init__(self, speed, color, owner):
#         super().__init__(speed, color)
#         self.owner = owner
#
#     def say_owner(self):
#         print(f'Владелец {self.owner}')
#
#
# class Bus(Transport):
#     def __init__(self, speed, color, seeds):
#         super().__init__(speed, color)
#         self.seeds = seeds
#
#     def say_seeds(self):
#         print(f'Кол-во мест {self.seeds}')
#
#
# class SportCar(Car, Transport):
#     pass
#
#
# car1 = Car(100, 'yellow', 'Василий')
# print(car1.color)
# print(car1.speed)
# print(car1.owner)
# car1.beep()
# car1.say_owner()
# bus1 = Bus(60, 'green', 33)
# bus1.say_seeds()
# car2 = SportCar(100, 'yellow', 'Иван')
# car2.beep()
# car2.say_owner()

"""↓ personal work ↓"""
class Person:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

    def say_name(self):
        print(f'Привет меня зовут {self.lname} {self.name}')

    def say_age(self):
        print(f'Мой возраст {self.age}')


class Student(Person):
    def __init__(self, name, lname, age, class_num):
        super().__init__(name, lname, age)
        self.class_num = class_num

    def say_class_num(self):
        print(f'Я учюсь в {self.class_num} классе')


student1 = Student('Иван', 'Петров', 14, 9)
student1.say_class_num()
