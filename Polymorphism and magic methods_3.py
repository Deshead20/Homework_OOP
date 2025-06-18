class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")

class Lecturer(Mentor):
    grades = {}


class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Иван', 'Петров', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['GIT']
student_1.courses_in_progress += ['OOP']

reviewer_1 = Reviewer('Петр', 'Иванов')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['GIT']
reviewer_1.courses_attached += ['OOP']
print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {" ".join(reviewer_1.courses_attached)}\n')
print()
reviewer_1.rate_homework(student_1, 'Python', 10)
reviewer_1.rate_homework(student_1, 'GIT', 5)
reviewer_1.rate_homework(student_1, 'OOP', 6)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')
print()

lecturer_1 = Lecturer('Ольга', 'Алехина')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['GIT']
lecturer_1.courses_attached += ['OOP']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'GIT', 8)
student_1.rate_lecturer(lecturer_1, 'OOP', 5)
print(f'Оценки лектору: {lecturer_1.name} {lecturer_1.surname}\n{lecturer_1.grades}')


print(student_1)

print(reviewer_1)

print(lecturer_1)

