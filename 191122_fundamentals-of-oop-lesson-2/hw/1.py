"""
Реализовать родительский класс человека, а также дочерние классы директора, преподавателя и ученика. Описать для каждого
класса необходимые свойства и методы.

Важно: директор помимо своих обязанностей может также и преподавать (множественное наследование).
"""


class Human:
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, skills: str = None,
                 hobbies: str = None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight
        self.skills = skills
        self.hobbies = hobbies

    def __call__(self, *args, **kwargs) -> str:
        return '{} {}, {} years\nAnthropometry: {} cm, {} kg\nSkills: {}\nHobbies: {}'.format(self.firstname,
                                                                                              self.lastname,
                                                                                              self.age,
                                                                                              self.height,
                                                                                              self.weight,
                                                                                              self.skills,
                                                                                              self.hobbies)

    def __str__(self) -> str:
        return '{} {}, {} years\nAnthropometry: {} cm, {} kg\nSkills: {}\nHobbies: {}'.format(self.firstname,
                                                                                              self.lastname,
                                                                                              self.age,
                                                                                              self.height,
                                                                                              self.weight,
                                                                                              self.skills,
                                                                                              self.hobbies)

    def __len__(self) -> int:
        return self.height

    def set_skills(self, skills: str) -> None:
        if self.skills:
            self.skills += '\n{}'.format(skills)
        else:
            self.skills = skills

    def set_hobbies(self, hobbies: str) -> None:
        if self.hobbies:
            self.hobbies += '\n{}'.format(hobbies)
        else:
            self.hobbies = hobbies

    def clear_skills(self) -> None:
        self.skills = None

    def clear_hobbies(self) -> None:
        self.hobbies = None


class Student(Human):
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, school: str,
                 grades: list = None, skills: str = None, hobbies: str = None):
        super().__init__(firstname, lastname, age, height, weight, skills, hobbies)
        self.school = school
        if grades:
            self.grades = grades
            self.avg_grades = sum(self.grades) / len(self.grades)
        else:
            self.grades = []
            self.avg_grades = 0

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

    def __str__(self) -> str:
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

    def set_grades(self, grades: list) -> None:
        self.grades += grades
        if self.grades:
            self.avg_grades = sum(self.grades) / len(self.grades)

    def clear_grades(self) -> None:
        self.grades = []
        self.avg_grades = 0


class Teacher(Human):
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, school: str,
                 subjects: list, seniority: int, skills: str = None, hobbies: str = None):
        super().__init__(firstname, lastname, age, height, weight, skills, hobbies)
        self.school = school
        self.subjects = subjects
        self.seniority = seniority

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

    def __str__(self) -> str:
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

    def set_subjects(self, subjects: list) -> None:
        self.subjects += subjects

    def clear_subjects(self) -> None:
        self.subjects = []

    def __add__(self, other: int):
        if type(other) == int:
            self.seniority += other

    def __radd__(self, other: int):
        self.__add__(other)

    def __sub__(self, other: int):
        if type(other) == int:
            self.seniority -= other

    def __rsub__(self, other: int):
        self.__sub__(other)


class Director(Teacher):
    def __init__(self, firstname: str, lastname: str, age: int, height: int, weight: int, school: str, subjects: list,
                 seniority: int, todo: list = None, skills: str = None, hobbies: str = None):
        super().__init__(firstname, lastname, age, height, weight, school, subjects, seniority, skills, hobbies)
        if todo:
            self.todo = todo
        else:
            self.todo = []

    def __add__(self, other: list):
        if type(other) == list:
            self.todo += other

    def __radd__(self, other: list):
        self.__add__(other)

    def __sub__(self, other: list):
        if type(other) == list:
            self.todo = [x for x in other if x not in self.todo]

    def __rsub__(self, other: list):
        self.__sub__(other)

    def view_todo(self):
        print(*self.todo)
