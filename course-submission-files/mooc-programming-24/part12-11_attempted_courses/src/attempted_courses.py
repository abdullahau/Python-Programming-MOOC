class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here

# Part 1 - Names of Students

def names_of_students(attempts: list):
    return list(map(lambda c: c.student_name, attempts))

# Part 2 - Courses

def course_names(attempts: list):
    return sorted(list(set(map(lambda c: c.course_name, attempts))))
