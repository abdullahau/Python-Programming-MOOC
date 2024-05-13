# WRITE YOUR SOLUTION HERE:
class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade_list = [grade1, grade2, grade3]

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')

def best_results(results: list) -> list:
    return [max(result.grade_list) for result in results]