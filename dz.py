class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.courses_attached = []
    self.student_grade = [] 
    self.ass = {}

  def __str__(self):
    return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{sum(self.student_grade) / len(self.student_grade)}"

  def __lt__(self, other):   #<
    return (sum(self.student_grade) / len(self.student_grade)) < (sum(other.student_grade) / len(other.student_grade))

  def __gt__(self, other):   #>
    return (sum(self.student_grade) / len(self.student_grade)) > (sum(other.student_grade) / len(other.student_grade))

  

class Reviewer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.courses_attached = []
    
  def __str__(self):
    return f"Имя: {self.name}\nФамилия: {self.surname}"

  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'


class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def assessment(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
      lecturer.student_grade += [grade]
      if course in lecturer.ass:
        lecturer.ass[course] += [grade]
      else:
        lecturer.ass[course] = [grade]
    else:
      return 'Ошибка'

  def average(self,grade):
    avg_grade = []
    for grade in self.grades.values():
      avg_grade += grade
    return sum(avg_grade)/len(avg_grade)

  def __str__(self):
    return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average(10)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
   

  def __lt__(self, other):   #<
    return self.average(10) < other.average(10)

  def __gt__(self, other):   #>
    return self.average(10) > other.average(10)



man_student = Student('Evgeny', 'Zhukovets', 'man')
man_student.finished_courses += ['Введение в программирование']
man_student.courses_in_progress += ['Python', 'Git']

woman_student = Student('Katya', 'Sculkina', 'woman')
woman_student.finished_courses += ['Введение в программирование']
woman_student.courses_in_progress += ['Python', 'Git']

picky_rew = Reviewer('Vera','Komarova')
picky_rew.courses_attached += ['Python', 'Git']

good_rew = Reviewer('Sergey','Makeev')
good_rew.courses_attached += ['Python', 'Git']

picky_lec = Lecturer('Ivan','Ivanov')
picky_lec.courses_attached += ['Python', 'Git']

good_lec = Lecturer('Vadim','Sergeev')
good_lec.courses_attached += ['Python', 'Git']


woman_student.assessment(good_lec, 'Python', 10)
woman_student.assessment(picky_lec, 'Git', 6)
woman_student.assessment(good_lec, 'Git', 10)
man_student.assessment(picky_lec, 'Python', 8)
man_student.assessment(good_lec, 'Git', 8)
man_student.assessment(picky_lec, 'Python', 7)

picky_rew.rate_hw(woman_student, 'Git', 4)
good_rew.rate_hw(man_student,'Python', 6)
good_rew.rate_hw(woman_student,'Python', 9)
picky_rew.rate_hw(woman_student, 'Git', 6)
good_rew.rate_hw(man_student,'Python', 5)
good_rew.rate_hw(man_student,'Python', 8)
good_rew.rate_hw(man_student,'Git', 10)

  
def avg_grade_course(students, course):
  all_grades = []
  for student in students: 
    all_grades += student.grades[course]
  return sum(all_grades)/len(all_grades)


def avg_assessment_course(lecturers, course):
  assessments = []
  for lecturer in lecturers: 
    assessments += lecturer.ass[course]
  return sum(assessments)/len(assessments)


print(avg_grade_course([woman_student,man_student], 'Git'))

print(picky_lec.ass)


print(avg_assessment_course([good_lec, picky_lec], 'Git'))