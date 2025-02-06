class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and  0 < grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        return sum(sum(rates) for rates in self.grades.values()) / sum(len(rates) for rates in self.grades.values())

    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за домашнее задание: {self.avg_rate()}
Курсы в процессе изучения: {', '.join(cours for cours in self.courses_in_progress)}
Завершенные курсы: {', '.join(cours for cours in self.finished_courses)}'''

    def __eq__(self, other):
        return (self.avg_rate() == other.avg_rate())

    def __gt__(self, other):
        return (self.avg_rate() > other.avg_rate())

    def __lt__(self, other):
        return (self.avg_rate() < other.avg_rate())
        
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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}'

    def avg_rate(self):
        return sum(sum(rates) for rates in self.grades.values()) / sum(len(rates) for rates in self.grades.values())

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
 
best_student = Student('Helena', 'Carter', 'f')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['git']
best_student.finished_courses += ['Exel']

worst_student = Student('Jack', 'Daniels', 'm')
worst_student.courses_in_progress += ['Python']
 
lecturer1 = Lecturer('Jon', 'Caneghem')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['C++']

lecturer2 = Lecturer('Abraham', 'VanHelsing')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['C++']

reviewer1 = Reviewer('Charles', 'Darwin')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['git']

reviewer2 = Reviewer('Kurt', 'Cobein')
reviewer2.courses_attached += ['Python']
 
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'git', 8)

reviewer1.rate_hw(worst_student, 'Python', 1)
reviewer1.rate_hw(worst_student, 'Python', 3)

worst_student.rate_lect(lecturer1, 'Python', 8)
worst_student.rate_lect(lecturer1, 'Python', 9)
best_student.rate_lect(lecturer1, 'Python', 10)
best_student.rate_lect(lecturer1, 'Python', 10)

worst_student.rate_lect(lecturer2, 'Python', 6)
best_student.rate_lect(lecturer2, 'Python', 7)
print(best_student)
print('\n')
print(lecturer1)
print('\n')
print(reviewer1)
print('\n')

if best_student > worst_student:
    print(f'{best_student.name} {best_student.surname} studies better than {worst_student.name} {worst_student.surname}')
elif best_student < worst_student:
    print(f'{best_student.name} {best_student.surname} studies worse than {worst_student.name} {worst_student.surname}')
elif best_student == worst_student:
    print(f'{best_student.name} {best_student.surname} studies the same way as {worst_student.name} {worst_student.surname}')

def students_avg_rate_for_course(students_list: list, course_name: str) -> float:
    sum_rate = 0
    len_rate = 0
    for student in students_list: 
        if isinstance(student, Student):      
            if course_name in student.grades.keys():
                sum_rate += sum(student.grades[course_name])
                len_rate += len(student.grades[course_name])
        else:
            return'Ошибка ввода'
    return(sum_rate/len_rate)

def lecturers_avg_rate_for_course(lecturers_list: list, course_name: str) -> float:
    sum_rate = 0
    len_rate = 0
    for lecturer in lecturers_list: 
        if isinstance(lecturer, Lecturer):      
            if course_name in lecturer.grades.keys():
                sum_rate += sum(lecturer.grades[course_name])
                len_rate += len(lecturer.grades[course_name])
        else:
            return'Ошибка ввода'
    return(sum_rate/len_rate)

print(students_avg_rate_for_course([best_student, worst_student],'Python'))
print(lecturers_avg_rate_for_course([lecturer1, lecturer2],'Python'))

