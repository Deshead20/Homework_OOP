class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
                return None
            else:
                lecturer.grades[course] = [grade]
                return None
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за ДЗ: {self.average_grade()}\n"
                f"Курсы в процессе: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}")

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count else 0


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
                return None
            else:
                student.grades[course] = [grade]
                return None
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def average_grade_hw(students: list, course: str) -> float | int:
    total = 0
    count = 0
    for student in students_list:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count else 0

def average_grade_lecture(lecturers: list, course: str):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count else 0


student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Git']

student2 = Student('Vlad', 'Kolov', 'male')
student2.courses_in_progress = ['Python', 'Git']
student2.finished_courses = ['Введение в программирование']

lecturer1 = Lecturer('Иван', 'Петров')
lecturer1.courses_attached = ['Python', 'Git']

lecturer2 = Lecturer('smith', 'Agent')
lecturer2.courses_attached = ['Python', 'Git']

reviewer1 = Reviewer('Петр', 'Иванов')
reviewer1.courses_attached = ['Python', 'Git']

reviewer2 = Reviewer('Kirill', 'Ayrovski')
reviewer2.courses_attached = ['Python', 'Git']

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 10)

reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Git', 10)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Git', 9)
student2.rate_lecturer(lecturer1, 'Python', 8)

student1.rate_lecturer(lecturer2, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Git', 10)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("student1:")
print(student1)
print()
print("student2:")
print(student2)
print()
print("lecturer1:")
print(lecturer1)
print()
print("lecturer2:")
print(lecturer2)
print()
print("reviewer1:")
print(reviewer1)
print()
print("reviewer2:")
print(reviewer2)

print()
print("Средняя оценка за ДЗ по курсу:", average_grade_hw(students_list, 'Python'))
print("Средняя оценка за лекции по курсу:", average_grade_lecture(lecturers_list, 'Python'))