import Student
import Grades

p1=Student.Student("Jerome Flow G Vasuqez", 23)
p2=Grades.Grades("CPE 028", 3, 1.25)
print(p1)
print("Name:", p1.name)
print("Age:", p1.age)

p2=Grades.Grades("CPE 028", 3, 1.25)
print(p2)
print("Course Code:", p2.code)
print("Course Units:", p2.unit)
print("Course Grades:", p2.grade)
