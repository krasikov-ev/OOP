class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за домашнее задание: {sum(sum(rates) for rates in self.grades.values())/sum(len(rates) for rates in self.grades.values())}
Курсы в процессе изучения: {', '.join(cours for cours in self.courses_in_progress)}
Завершенные курсы: {', '.join(cours for cours in self.finished_courses)}'''

        
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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(sum(rates) for rates in self.grades.values())/sum(len(rates) for rates in self.grades.values())}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['git']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['IZO']
 
cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['C++']
some_mentor = Reviewer('Jack', 'Daniels')
some_mentor.courses_attached += ['Python']
some_mentor.courses_attached += ['C++']
 
some_mentor.rate_hw(best_student, 'Python', 10)
some_mentor.rate_hw(best_student, 'Python', 10)
some_mentor.rate_hw(best_student, 'Python', 10)


some_mentor.rate_hw(best_student, 'C++', 5)
some_mentor.rate_hw(best_student, 'C++', 5)
some_mentor.rate_hw(best_student, 'C++', 5)

best_student.rate_lect(cool_mentor, 'Python', 9)
best_student.rate_lect(cool_mentor, 'Python', 10)

 
# print(best_student.grades)
# print(cool_mentor.grades)
# print(best_student)
# print(some_mentor)
print(cool_mentor)