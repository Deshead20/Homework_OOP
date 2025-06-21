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
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        total_sum = 0
        count = 0
        for grades_list in self.grades.values():
            total_sum += sum(grades_list)
            count += len(grades_list)
        return round(total_sum / count, 1) if count > 0 else 0

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating() == other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating() < other.average_rating()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating() <= other.average_rating()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating() > other.average_rating()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating() >= other.average_rating()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating() != other.average_rating()

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет"
        avg_grade = self.average_rating()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        total_sum = 0
        count = 0
        for grades_list in self.grades.values():
            total_sum += sum(grades_list)
            count += len(grades_list)
        return round(total_sum / count, 1) if count > 0 else 0

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_rating() == other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_rating() < other.average_rating()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_rating() <= other.average_rating()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_rating() > other.average_rating()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_rating() >= other.average_rating()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_rating() != other.average_rating()

    def __str__(self):
        avg_rating = self.average_rating()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_rating}")


class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Иван', 'Петров', 'male')
student_1.courses_in_progress += ['Python', 'GIT', 'OOP']
student_1.finished_courses = ['Введение в программирование']

student_2 = Student('Оксана', 'Любовна', 'female')
student_2.courses_in_progress += ['Python', 'OOP']
student_2.finished_courses = ['Введение в программирование', 'API']

reviewer_1 = Reviewer('Петр', 'Иванов')
reviewer_1.courses_attached += ['Python', 'GIT', 'OOP']

reviewer_1.rate_homework(student_1, 'Python', 10)
reviewer_1.rate_homework(student_1, 'GIT', 5)
reviewer_1.rate_homework(student_1, 'OOP', 6)

reviewer_1.rate_homework(student_2, 'Python', 9)
reviewer_1.rate_homework(student_2, 'OOP', 8)

lecturer_1 = Lecturer('Ольга', 'Алехина')
lecturer_1.courses_attached += ['Python', 'GIT', 'OOP']

lecturer_2 = Lecturer('Алекcей', 'Пчелкин')
lecturer_2.courses_attached += ['Python', 'OOP']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'GIT', 8)
student_1.rate_lecturer(lecturer_1, 'OOP', 5)

student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'OOP', 7)

print("=" * 50)
print("Инфо о студентах:")
print("Студент 1:")
print(student_1)
print("\nСтудент 2:")
print(student_2)
print()
print("Инфо о проверяющих:")
print(reviewer_1)
print()
print("Инфо о лекторах:")
print("Лектор 1:")
print(lecturer_1)
print("\nЛектор 2:")
print(lecturer_2)
print()
print("Сравнение студентов:")
print("Студент 1 > Студент 2:", student_1 > student_2)
print("Студент 1 < Студент 2:", student_1 < student_2)
print("Студент 1 == Студент 2:", student_1 == student_2)
print()
print("Сравнение лекторов:")
print("Лектор 1 > Лектор 2:", lecturer_1 > lecturer_2)
print("Лектор 1 < Лектор 2:", lecturer_1 < lecturer_2)
print("Лектор 1 == Лектор 2:", lecturer_1 == lecturer_2)