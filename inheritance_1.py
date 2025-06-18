class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
                return None
            else:
                student.grades[course] = [grade]
                return None
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    pass
if __name__ == "__main__":

    best_student = Student('Ольга', 'Алехина', 'female')
    best_student.courses_in_progress += ['Python']


    cool_reviewer = Reviewer('Петр', 'Петров')
    cool_reviewer.courses_attached += ['Python']

    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)

    print(f"Оценки студента: {best_student.grades}")

    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')

    print(f"Лектор является ментором? {isinstance(lecturer, Mentor)}")
    print(f"Проверяющий является ментором? {isinstance(reviewer, Mentor)}")
    print(f"Курсы лектора: {lecturer.courses_attached}")
    print(f"Курсы проверяющего: {reviewer.courses_attached}")