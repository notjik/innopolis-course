"""
Реализовать родительский класс человека, а также дочерние классы директора, преподавателя и ученика. Описать для каждого
класса необходимые свойства и методы.

Важно: директор помимо своих обязанностей может также и преподавать (множественное наследование).
"""


class Human:
    """Инициирование"""
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, skills: str = None,
                 hobbies: str = None):
        self.firstname = firstname  # Имя
        self.lastname = lastname  # Фамилия
        self.age = age  # Возраст
        self.height = height  # Рост
        self.weight = weight  # Вес
        self.skills = skills  # Навыки
        self.hobbies = hobbies  # Хобби

    """Вызов со скобками"""
    def __call__(self, *args, **kwargs) -> str:
        return '{} {}, {} years\nAnthropometry: {} cm, {} kg\nSkills: {}\nHobbies: {}'.format(self.firstname,
                                                                                              self.lastname,
                                                                                              self.age,
                                                                                              self.height,
                                                                                              self.weight,
                                                                                              self.skills,
                                                                                              self.hobbies)

    """Вызвать без скобок"""
    def __str__(self) -> str:
        return self.__call__()

    """Длина"""
    def __len__(self) -> int:
        return self.height

    """Задать навыки"""
    def set_skills(self, skills: str) -> None:
        if self.skills:
            self.skills += '\n{}'.format(skills)
        else:
            self.skills = skills

    """Задать хобби"""
    def set_hobbies(self, hobbies: str) -> None:
        if self.hobbies:
            self.hobbies += '\n{}'.format(hobbies)
        else:
            self.hobbies = hobbies

    """Отчистить навыки"""
    def clear_skills(self) -> None:
        self.skills = None

    """Отчистить хобби"""
    def clear_hobbies(self) -> None:
        self.hobbies = None


class Student(Human):
    """Инициирование"""
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, school: str,
                 grades: list = None, skills: str = None, hobbies: str = None):
        super().__init__(firstname, lastname, age, height, weight, skills, hobbies)  # Наследование
        self.school = school  # Название школы
        if grades:
            self.grades = grades  # Оценки
            self.avg_grades = sum(self.grades) / len(self.grades)  # Средний балл
        else:
            self.grades = []
            self.avg_grades = 0

    """Вызов функции со скобками"""
    def __call__(self) -> str:
        return '{} {}, {} years\nAnthropometry: {} cm, {} kg\n' \
               'School: {}\nGrade point average: {}\nSkills: {}\nHobbies: {}'.format(self.firstname,
                                                                                     self.lastname,
                                                                                     self.age,
                                                                                     self.height,
                                                                                     self.weight,
                                                                                     self.school,
                                                                                     self.avg_grades,
                                                                                     self.skills,
                                                                                     self.hobbies)

    """Вызов функции без скобок"""
    def __str__(self) -> str:
        return self.__call__()

    """Передать оценки"""
    def set_grades(self, grades: list) -> None:
        self.grades += grades
        if self.grades:
            self.avg_grades = sum(self.grades) / len(self.grades)

    """Отчистить оценки"""
    def clear_grades(self) -> None:
        self.grades = []
        self.avg_grades = 0


class Teacher(Human):
    """Инициирование"""
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, school: str,
                 subjects: list, seniority: int, skills: str = None, hobbies: str = None):
        super().__init__(firstname, lastname, age, height, weight, skills, hobbies)
        self.school = school  # Название школы
        self.subjects = subjects  # Предметы, которые ведут учитель
        self.seniority = seniority  # Стаж работы

    """Вызов функции со скобками"""
    def __call__(self) -> str:
        return '{} {}, {} years\nAnthropometry: {} cm, {} kg\n' \
               'School: {}\nSubjects: {}\nWork experience: {}\nSkills: {}\nHobbies: {}'.format(self.firstname,
                                                                                               self.lastname,
                                                                                               self.age,
                                                                                               self.height,
                                                                                               self.weight,
                                                                                               self.school,
                                                                                               self.subjects,
                                                                                               self.seniority,
                                                                                               self.skills,
                                                                                               self.hobbies)

    """Вызов функции без скобок"""
    def __str__(self) -> str:
        return self.__call__()

    """Задать предметы"""
    def set_subjects(self, subjects: list) -> None:
        self.subjects += subjects

    """Отчистить предметы"""
    def clear_subjects(self) -> None:
        self.subjects = []

    """Увеличить стаж"""
    def __add__(self, other: int):
        if type(other) == int:
            self.seniority += other

    """Увеличить стаж если цифра слева"""
    def __radd__(self, other: int):
        self.__add__(other)

    """Уменьшить стаж"""
    def __sub__(self, other: int):
        if type(other) == int:
            self.seniority -= other

    """Увеличить стаж если цифра слева"""
    def __rsub__(self, other: int):
        self.__sub__(other)


class Director(Teacher):
    """Инициирование"""
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, school: str, subjects: list,
                 seniority: int, todo: list = None, skills: str = None, hobbies: str = None):
        super().__init__(firstname, lastname, age, height, weight, school, subjects, seniority, skills, hobbies)
        # Наследование
        if todo:
            self.todo = todo  # Обязанности (список дел)
        else:
            self.todo = []

    """Добавить обязанности (список дел)"""
    def __add__(self, other: list):
        if type(other) == list:
            self.todo += other

    """Добавить обязанности (список дел) если список справа"""
    def __radd__(self, other: list):
        self.__add__(other)

    """Снять обязанности (список дел)"""
    def __sub__(self, other: list):
        if type(other) == list:
            self.todo = [x for x in other if x not in self.todo]

    """Снять обязанности (список дел) если цифра справа"""
    def __rsub__(self, other: list):
        self.__sub__(other)

    """Вывод списка дел"""
    def view_todo(self) -> None:
        print(*self.todo)
