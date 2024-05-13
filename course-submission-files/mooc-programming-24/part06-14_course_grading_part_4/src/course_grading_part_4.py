# tee ratkaisu tänne
# Title & Header
def title_header(filename: str):
    course = []
    with open(filename) as course_detail:
        for line in course_detail:
            parts = line.split(":")
            course.append(parts[1].strip())
    
    title = course[0] + ", " + course[1] + " credits" + "\n"
    border = (len(title)-1) * "=" + "\n"
    header = f'{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}' + "\n"
    return title, border, header

# Grader, Point Conversion & Report Builder
def grader(points: int):
    grades = [0, 1, 2, 3, 4, 5]
    limits = [0, 15, 18, 21, 24, 28]
    for limit in limits[::-1]:
        if points >= limit:
            grade = grades[limits.index(limit)]
            break
        else:
            continue
    return grade


def to_point(exercises: list):
    return sum(exercises) // 4


def report(students: dict, exercises: dict, exams: dict):
    line = ""
    csv = ""
    for pic, name in students.items():
        exercises_points = to_point(exercises[pic])
        total_exercises = sum(exercises[pic])
        exam_points = sum(exams[pic])
        total_points = exercises_points + exam_points
        grade = grader(total_points)
        line += f'{name:30}{total_exercises:<10}{exercises_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}\n'
        csv += f'{pic};{name};{grade}\n'
    return line, csv

# Main Function
if True:
    # Not executed until True
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_info = input("Course information: ")
else:
    # hard-coded input
    student_info = "Exercise Files\course-grading-part-4\students4.csv"
    exercise_data = "Exercise Files\course-grading-part-4\exercises4.csv"
    exam_data = "Exercise Files\course-grading-part-4\exam_points4.csv"
    course_info = "Exercise Files\course-grading-part-4\course4.txt"

students = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = []
        for part in parts[1:]:
            part = part.strip()
            part = int(part)
            exercises[parts[0]].append(part)

exams = {}
with open(exam_data) as new_file:
    for line in new_file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exams[parts[0]] = []
            for part in parts[1:]:
                part = part.strip()
                part = int(part)
                exams[parts[0]].append(part)

with open("results.txt", "w") as text_result, open("results.csv","w") as csv_result:
    
    title, border, header = title_header(course_info)
    text_result.write(title)
    text_result.write(border)
    text_result.write(header)
    line, csv = report(students, exercises, exams)
    text_result.write(line)
    csv_result.write(csv)
    