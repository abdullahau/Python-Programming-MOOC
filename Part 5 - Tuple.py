# Tuples are enclosed in parentheses (), while lists are enclosed in square brackets []
# Tuples are immutable, while the contents of a list may change

# The following bit of code creates a tuple containing the coordinates of a point:
point = (10, 20)

# The items stored in a tuple are accessed by index, just like the items stored in a list:
point = (10, 20)
print("x coordinate:", point[0])
print("y coordinate:", point[1])

# The values stored in a tuple cannot be changed after the tuple has been defined. The following will not work:
point = (10, 20)
point[0] = 15

# What is the purpose of a tuple?

# Tuples are ideal for when there is a set collection of values which are in some way connected. 
# For example, when there is a need to handle the x and y coordinates of a point, a tuple is a natural choice, because coordinates will always consist of two values:
point = (10, 20)

# Technically it is of course possible to also use a list to store these:
point = [10, 20]

# A list is a collection of consecutive items in a certain order. The size of a list may also change. 
# When we are storing the coordinates of a point, we want to store the x and y coordinates specifically, not an arbitrary list containing those values.

# Because tuples are immutable, unlike lists, they can be used as keys in a dictionary. 
# The following bit of code creates a dictionary, where the keys are coordinate points:
points = {}
points[(3, 5)] = "monkey"
points[(5, 0)] = "banana"
points[(1, 2)] = "harpsichord"
print(points[(3, 5)])

# Attempting a similar dictionary definition using lists would not work:
points = {}
points[[3, 5]] = "monkey"
points[[5, 0]] = "banana"
points[[1, 2]] = "harpsichord"
print(points[[3, 5]])

# Tuples without parentheses
numbers = (1, 2, 3)

numbers = 1, 2, 3

# This means we can also easily return multiple values using tuples. Let's have alook at he following example:
def minmax(my_list):
  return min(my_list), max(my_list)

my_list = [33, 5, 21, 7, 88, 312, 5]

min_value, max_value = minmax(my_list)
print(f"The smallest item is {min_value} and the greatest item is {max_value}")

# This function returns two values in a tuple. The return value is assigned to two variables at once:
min_value, max_value = minmax(my_list)

# Using parentheses may make the notation more clear. On the left hand side of the assignment statement we also have a tuple, which contains two variable names. 
# The values contained within the tuple returned by the function are assigned to these two variables.
(min_value, max_value) = minmax(my_list)

# You may remember the dictionary method 'items' in the previous section. 
# We used it to access all the keys and values stored in a dictionary:
my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)

# Tuples are at work here, too. The method my_dictionary.items() returns each key-value pair as a tuple, where the first item is the key and the second item is the value.

# Another common use case for tuples is swapping the values of two variables:
number1, number2 = number2, number1

# The assignment statement above swaps the values stored in the variables number1 and number2. 
# The result is identical to what is achieved with the following bit of code, using a helper variable:
helper_var = number1
number1 = number2
number2 = helper_var


# Create a tuple - Approach 1
def create_tuple(x: int, y: int, z: int):
    my_tuple = (min(x, y, z), max(x, y, z), (x + y + z))
    return my_tuple

print(create_tuple(5, 3, -1))

# Create a tuple - Approach 2
def create_tuple(x: int, y: int, z: int):
    """ The function returns a tuple formed from the parameters (smallest, greatest, sum) """
    smallest = min([x, y, z])
    greatest = max([x, y, z])
    sum = x + y + z # sum([x, y, z]) also works
 
    return (smallest, greatest, sum)


# The oldest person - Approach 1
def oldest_person(people: list):
    ref = 0
    index = 0
    for person in people:
        if person[1] < ref or ref == 0:
            ref = person[1]
            index = people.index(person)
    return people[index][0]

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))

# The oldest person - Approach 2
def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        # comparing the year of birth of the oldest known person and the person in turn
        if person[1] < oldest[1]:
            oldest = person
 
    return oldest[0]

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))

# Older people - Approach 1
def older_people(people: list, year: int):
    shortlist = []
    for person in people:
        if person[1] < year:
            shortlist.append(person[0])
    return shortlist

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)

# Student database - Approach 1
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
summary(students)
        
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
summary(students)

# A square of letters - Approach 1

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

width_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27,
              29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]

width_list = []
for i in range(1, 52, 2):
    width_list.append(i)


layer = 4
width = (1 + (layer - 1) * 2 )

index = layer
line = ""
index2 = 0
index3 = layer
fix = ""
inverted = []

for i in range(layer-1, -1, -1):
    for z in range(0, index2):
        fix += letters[index3]
        index3 -= 1
    line = fix + letters[index - 1] * width_list[index-1] + fix[::-1]
    print(line)
    inverted.append(line)
    line = ""
    fix = ""
    index -= 1
    index2 += 1
    index3 = layer - 1
for i in inverted[layer-2::-1]:
    print(i)
    
# A square of letters - Submission - 1
layer = int(input("Layers: "))
width = (1 + (layer - 1) * 2 )

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

width_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27,
              29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]

index = layer
line = ""
index2 = 0
index3 = layer
fix = ""
inverted = []

for i in range(layer-1, -1, -1):
    for z in range(0, index2):
        fix += letters[index3]
        index3 -= 1
    line = fix + letters[index - 1] * width_list[index-1] + fix[::-1]
    print(line)
    inverted.append(line)
    line = ""
    fix = ""
    index -= 1
    index2 += 1
    index3 = layer - 1
for i in inverted[layer-2::-1]:
    print(i)


# Practice - Approach 1

# Layers: 1
# A

# Layers: 2
# BBB
# BAB
# BBB

# Layers: 3
# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC

# Layers: 4
# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD

# Layers: 5
# EEEEEEEEE
# EDDDDDDDE
# EDCCCCCDE
# EDCBBBCDE
# EDCBABCDE
# EDCBBBCDE
# EDCCCCCDE
# EDDDDDDDE
# EEEEEEEEE

level1 = letters[layer-1] * width
level2 = letters[layer-1] + letters[layer-2] * (width-2) + letters[layer-1]
level3 = letters[layer-1] + letters[layer-2] + letters[layer-3] * (width-4) + letters[layer-2] + letters[layer-1]
level4 = letters[layer-1] + letters[layer-2] + letters[layer-3] + letters[layer-4] * (width-6)  + letters[layer-3] + letters[layer-2] + letters[layer-1]

square = f"{level1}\n{level2}\n{level3}\n{level4}\n{level3}\n{level2}\n{level1}"

print(square)


# A square of letters - Approach 2
n = int(input("Layers: "))
 
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
left = ""    # section, that goes downwards
right = ""    # section, that goes upwards
k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between
while k >= 1:
    left = left + alphabets[k]
    right = alphabets[k] + right
    m -= 2
    print(left + alphabets[k] * m + right)
    k -= 1
while k <= n-1:
    print(left + alphabets[k] * m + right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1