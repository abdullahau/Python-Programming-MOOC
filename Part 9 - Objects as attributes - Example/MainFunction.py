from completedcourse import CompletedCourse
from course import Course
from student import Student

# Create a list of students
students = []
students.append(Student("Ollie", "1234", 10))
students.append(Student("Peter", "3210", 23))
students.append(Student("Lena", "9999", 43))
students.append(Student("Tina", "3333", 8))

# Create a course named Introduction to Programming
itp = Course("Introduction to Programming", "itp1", 5)

# Add completed courses for each student, with grade 3 for all
completed = []
for student in students:
    completed.append(CompletedCourse(student, itp, 3))

# Print out the name of the student for each completed course
for course in completed:
    print(course.student.name)
