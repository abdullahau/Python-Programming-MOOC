# Grade statistics

"""

In this exercise you will write a program for printing out grade statistics for a university course.

The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. 
The program then prints out statistics based on the results.

Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.

The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

And example of how the data is typed in:

```python
Exam points and exercises completed: 15 87
Exam points and exercises completed: 10 55
Exam points and exercises completed: 11 40
Exam points and exercises completed: 4 17
Exam points and exercises completed:
Statistics:
```python

When the user types in an empty line, the program prints out statistics. They are formulated as follows:

The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. 
Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.

The grade for the course is determined based on the following table:

| exam points + exercise points | grade         |
| ----------------------------- | ------------- |
| 0–14                          | 0 (i.e. fail) |
| 15–17                         | 1             |
| 18–20                         | 2             |
| 21–23                         | 3             |
| 24–27                         | 4             |
| 28–30                         | 5             |

There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

With the example input from above the program would print out the following statistics:

```sample output
Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
  5:
  4:
  3: *
  2:
  1: **
  0: *
```

Floating point numbers should be printed out with one decimal precision.

"""

def point_split(point_string: str):
    point_string = point_string.split(" ", 2)
    exam_point = int(point_string[0])
    exercise_point = int(point_string[1])
    return exam_point, exercise_point

def exercise_point_conversion(exercises_completed: int) -> int:
    return exercises_completed // 10

def total_point_calculation(exam_point:int, exercise_point: int) -> int:
    return exam_point + exercise_point


def grade_conversion(total_point: int, exam_point: int) -> int:
    grade_list = [0, 1, 2, 3, 4, 5]
    point_list = [0, 15, 18, 21, 24, 28]
    
    if exam_point >= 10:
        for i in range(len(point_list)):
            if total_point >= point_list[i]:
                grade = grade_list[i]
            else:
                grade = grade_list[i-1]
                break
    else:
        grade = 0
        
    return grade

def average_points(student_point_list: list) -> float:
    sum = 0
    for i in student_point_list:
        sum += i
    return sum / len(student_point_list)

def pass_rate(student_grades_list: list):
    failed = 0
    for i in student_grades_list:
        if i == 0:
            failed += 1
    return (len(student_grades_list) - failed) / len(student_grades_list) * 100

def plot_grade_dist(student_grades_list: list):
    grade_list = [5, 4, 3, 2, 1, 0]
    print("Grade distribution:")
    for i in grade_list:
        counter = 0 
        for z in student_grades_list:
            if i == z:
                counter += 1
        print(f"{i:2}: {"*" * counter}")

def main():
    student_points_list = []
    student_grades_list = []
    while True:
        student_input = input("Exam points and exercises completed: ")
        if student_input != "":
            exam_point, exercises_completed = point_split(student_input)
            exercise_point = exercise_point_conversion(exercises_completed)
            total_point = total_point_calculation(exam_point, exercise_point)
            student_points_list.append(total_point)
            grades = grade_conversion(total_point, exam_point)
            student_grades_list.append(grades)
        else:
            break

    print("Statistics:")
    print(f"Points average: {average_points(student_points_list):.1f}")
    print(f"Pass percentage: {pass_rate(student_grades_list):.1f}")
    plot_grade_dist(student_grades_list)
    
main()