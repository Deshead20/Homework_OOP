class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return None
        if course not in self.courses_in_progress:
            return None
        if course not in lecturer.courses_attached:
            return None
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
            return None
        else:
            lecturer.grades[course] = [grade]
            return None

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка'
        if course not in self.courses_attached:
            return 'Ошибка'
        if course not in student.courses_in_progress:
            return 'Ошибка'
        if course in student.grades:
            student.grades[course].append(grade)
            return None
        else:
            student.grades[course] = [grade]
            return None


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алехина', 'Female')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))
print(student.rate_lecture(lecturer, 'Java', 8))
print(student.rate_lecture(lecturer, 'C++', 8))
print(student.rate_lecture(reviewer, 'Python', 6))

print(lecturer.grades)