# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []


def add_course(students: dict, name: str, course: tuple):
    if course[1] != 0:
        if len(students[name]) == 0:
            students[name].append(course)
        elif len(students[name]) > 0:
            courses_enrolled = []
            for courses in students[name]:
                courses_enrolled.append(courses[0])
            if course[0] in courses_enrolled:
                initial_score = students[name][courses_enrolled.index(course[0])][1]
                if initial_score < course[1]:
                    students[name].pop(courses_enrolled.index(course[0]))
                    students[name].append(course)
            else:
                students[name].append(course)

def summary(students:dict):
    print(f"students {len(students)}")
    max_courses = 0
    for student in students:
        if len(students[student]) > max_courses:
            max_courses = len(students[student])
            max_courses_student = student
    print(f"most courses completed {max_courses} {max_courses_student}")
    max_average = 0
    for student in students:
        sum = 0
        for course in students[student]:
            sum += course[1]
        student_average = sum / len(students[student])
        if student_average > max_average:
            max_average = student_average
            max_average_student = student
    print(f"best average grade {max_average} {max_average_student}")


def print_student(students: dict, name: str):
    if name in students:
        if students[name] == []:
            print(f"{name}:\n no completed courses")
        else:
            print(f"{name}:\n {len(students[name])} completed courses:")
            sum = 0
            for courses in students[name]:
                print(f"  {courses[0]} {courses[1]}")
                sum += courses[1]
            print(f" average grade {sum / len(students[name])}")
    else:
        print(f"{name}: no such person in the database")


if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    print_student(students, "Emily")
    print_student(students, "Peter")