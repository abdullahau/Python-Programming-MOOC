# Student database - Approach 1

# Student database - Data Type: Dictionary
# Course Collection - Data Type: List
# Individual Course Details - Data Type: Tuple


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


students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
add_course(students, "Peter", ("Data Structures and Algorithms", 1))
add_course(students, "Peter", ("Introduction to Programming", 1))
add_course(students, "Peter", ("Advanced Course in Programming", 1))
add_course(students, "Eliza", ("Introduction to Programming", 5))
add_course(students, "Eliza", ("Introduction to Computer Science", 4))
summary(students)



students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")



students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
print_student(students, "Peter")

students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")


# Student database - Approach 2
def add_student(students: dict, name: str):
    students[name] = {}
 
def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
 
    students_completed_courses = students[name]
 
    print(f"{name}:")
    if len(students_completed_courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(students_completed_courses):} completed courses:")
        sum = 0
        for course, grade in students_completed_courses.items():
            course_grade = grade[1]
            print(f"  {course} {course_grade}")
            sum += course_grade
 
        print(f" average grade {sum/len(students_completed_courses):.1f}")
 
def add_course(students: dict, name: str, completion: tuple):
    students_completed_courses = students[name]
    course_name = completion[0]
    course_grade = completion[1]
 
    # failed course is not recorded in the database
    if course_grade==0:
        return
 
    # if previous grade is higher, new grade is not recorded in the database
    if course_name in students_completed_courses:
        if students_completed_courses[course_name][1] > course_grade:
            return
 
    students_completed_courses[course_name] = completion
 
def summary(students: dict):
    print(f"students {len(students)}")
    most_courses_count = 0
    best_avg_grade = 0
    for name, completions in students.items():
        if len(completions) > most_courses_count:
            most_courses = name
            most_courses_count = len(students[most_courses])
 
        sum = 0
        for course, grade in completions.items():
            sum += grade[1]
 
        if len(completions)==0:
            avg = 0
        else:
            avg = sum/len(completions)
 
        if avg>best_avg_grade:
            best_avg_grade = avg
            best = name
 
    print(f"most courses completed {most_courses_count} {most_courses}")
    print(f"best average grade {best_avg_grade:.1f} {best}")
