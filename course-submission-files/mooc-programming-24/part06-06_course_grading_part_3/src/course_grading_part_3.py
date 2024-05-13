# tee ratkaisu tänne
if True:
    # Not executed until True
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "Exercise Files\course-grading-part-3\students1.csv"
    exercise_data = "Exercise Files\course-grading-part-3\exercises1.csv"
    exam_data = "Exercise Files\course-grading-part-3\exam_points1.csv"

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


print(f"{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}")
for pic, name in students.items():
    exercises_points = sum(exercises[pic]) // 4
    exam_points = sum(exams[pic])
    total_points = exercises_points + exam_points
    grades = [0, 1, 2, 3, 4, 5]
    points = [0, 15, 18, 21, 24, 28]
    for point in points[::-1]:
        if total_points >= point:
            grade = grades[points.index(point)]
            print(f"{name:<30}{sum(exercises[pic]):<10}{exercises_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")
            break
        else:
            continue 