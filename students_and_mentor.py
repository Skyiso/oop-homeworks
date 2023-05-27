class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_rating(self):
        # # Использование цикла
        # sum_v = 0
        # len_v = 0
        # for value in self.grades.values():
        #     sum_v += sum(value)
        #     len_v += len(value)
        # avg = round(sum_v / len_v, 1)
        # return avg

        # Короткое решение
        list_of_raiting = sum(self.grades.values(), start=[])
        avg = round(sum(list_of_raiting) /
                    len(list_of_raiting), 1)
        return avg

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._avg_rating()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._avg_rating() < other._avg_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_rating(self):
        list_of_raiting = sum(self.grades.values(), start=[])
        avg = round(sum(list_of_raiting) /
                    len(list_of_raiting), 1)
        return avg

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._avg_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._avg_rating() < other._avg_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


first_student = Student('Ruoy', 'Eman', 'Male')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Git', 'SQL']
second_student = Student('Jennifer', 'Stevenson', 'Female')
second_student.courses_in_progress += ['Python', 'Git']
second_student.finished_courses += ['SQL']

first_lecturer = Lecturer('Anthony', 'Merritt')
first_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Susan', 'Sherman')
second_lecturer.courses_attached += ['Git']

first_reviewer = Reviewer('Edmund', 'Porter')
first_reviewer.courses_attached += ['Python']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 10)

first_student.rate_lec(first_lecturer, 'Python', 10)
first_student.rate_lec(first_lecturer, 'Python', 10)
first_student.rate_lec(first_lecturer, 'Python', 10)
second_student.rate_lec(first_lecturer, 'Python', 9)
second_student.rate_lec(second_lecturer, 'Git', 10)
second_student.rate_lec(second_lecturer, 'Git', 10)

print(first_student.grades)
print(second_student.grades)
print(first_lecturer.grades)
print(second_lecturer.grades)

print(first_student)
print(second_student)
print(first_student < second_student)
print(first_student < second_lecturer)
print(first_lecturer)
print(second_lecturer)
print(first_lecturer < second_lecturer)
print(first_lecturer < second_student)
print(first_reviewer)