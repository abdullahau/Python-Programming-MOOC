class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Part 1 - Accepted attempts
def accepted(attempts: list):
    return list(filter(lambda c: c.grade >= 1, attempts))

# Part 2 - Attempts with grade
def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda c: c.grade == grade, attempts))

# Part 3 - Students who passed the course
def passed_students(attempts: list, course: str):
    return sorted(list(map(lambda x: x.student_name, filter(lambda c: c.grade > 0 and c.course_name == course, attempts))))