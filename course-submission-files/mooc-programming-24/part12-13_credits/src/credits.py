from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

# Part 1 - The sum of all credits
def sum_of_all_credits(credit_list: list[CourseAttempt]):
    return reduce(lambda x, y: x + y.credits, credit_list, 0)

# Part 2 - The sum of passed credits
def sum_of_passed_credits(credit_list: list[CourseAttempt]):
    return reduce(lambda x, y: x + y.credits, filter(lambda x: x.grade > 1, credit_list), 0)

# Part 3 - Average grade for passed courses
def average(credit_list: list[CourseAttempt]):
    passed_grades = list(filter(lambda x: x.grade > 0, credit_list))
    sum_of_passed_grades = reduce(lambda x, y: x + y.grade, passed_grades, 0)
    return sum_of_passed_grades / len(passed_grades)