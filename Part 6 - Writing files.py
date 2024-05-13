# Writing files

# Create a new file
# The 'open' function with the additional argument 'w', to signify that the file should be opened in write mode.

with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")
    my_file.write("This is the second line")
    my_file.write("This is the last line")
    
'''
output: 
Hello there!This is the second lineThis is the last line
'''

# Line breaks are achieved by adding new line characters \n to the argument strings:
with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!\n")
    my_file.write("This is the second line\n")
    my_file.write("This is the last line\n")
    
'''
output:
Hello there!
This is the second line
This is the last line
'''

# Appending data to an existing file
# 'open' file in append mode with argument 'a'
with open("new_file.txt", "a") as my_file:
    my_file.write("This is the 4th line\n")
    my_file.write("And yet another line.\n")

'''
output:
Hello there!
This is the second line
This is the last line
This is the 4th line
And yet another line.
'''

# More often a file is read, processed and overwritten in its entirety. 
# For example, when the contents should change in the middle of the file, it is usually easiest to overwrite the entire file.

# Writing CSV files
# CSV files can be written line by line with the 'write' method just like any other file.
with open("coders.csv", "w") as my_file:
    my_file.write("Eric;Windows;Pascal;10\n")
    my_file.write("Matt;Linux;PHP;2\n")
    my_file.write("Alan;Linux;Java;17\n")
    my_file.write("Emily;Mac;Cobol;9\n")
    
'''
Output:
Eric;Windows;Pascal;10
Matt;Linux;PHP;2
Alan;Linux;Java;17
Emily;Mac;Cobol;9
'''

# What if the data to be written is stored in computer memory in a list?
coders = []
coders.append(["Eric", "Windows", "Pascal", 10])
coders.append(["Matt", "Linux", "PHP", 2])
coders.append(["Alan", "Linux", "Java", 17])
coders.append(["Emily", "Mac", "Cobol", 9])

# We can build the string we want to write as an f-string, and write the ready line to the file like so:
with open("coders.csv", "w") as my_file:
    for coder in coders:
        line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
        my_file.write(line+"\n")
        
# If each list of coder data was very long, with many more items, building the string by hand would be quite cumbersome. 
# We can use a 'for' loop to build the string instead:
with open("coders.csv", "w") as my_file:
    for coder in coders:
        line = ""
        for value in coder:
            line += f"{value};"
        line = line[:-1]
        my_file.write(line+"\n")

# Clearing file contents and deleting files
with open("file_to_be_cleared.txt", "w") as my_file:
    pass

# Now the 'with' block only contains the command 'pass', which doesn't actually do anything. 
# Python does not allow empty blocks, so the command is necessary here.

# It is possible to also bypass the 'with' block by using the following oneliner:
open('file_to_be_cleared.txt', 'w').close()

# Deleting files
# You can also delete a file entirely. We will have to ask for help from the operating system to achieve this:
# the command to delete files is in the os module
import os

os.remove("unnecessary_file.csv")  

# Handling data in CSV format
# Let's write a program which assesses students' performance on a course. 
# The program reads a CSV file, which contains weekly exercise points received by the students. 
# The program then calculates the points total and determines the grade attained by each student. 
# Finally, the program creates a CSV file containing the points total and grade for each student.

# The CSV file given as input to the program looks like this:
'''
Sample data:
Peter;4;2;3;5;4;0;0
Paula;7;2;8;3;5;4;5
Susan;3;4;3;5;3;4;4
Emily;6;6;5;5;0;4;8
'''

# The program logic is divided into three functions: 
# reading the file and processing the contents into an accessible format, 
# determining the grade, and 
# writing the file.

# The file is read following the principles covered in the previous section. 
# The data is stored in a dictionary, where the key is the student's name, and the value is a list of the points received by the student, in integer format:
def read_weekly_points(filename):
    weekly_points = {}
    with open(filename) as my_file:
        for line in my_file:
            parts = line.split(";")
            point_list = []
            for points in parts[1:]:
                point_list.append(int(points))
            weekly_points[parts[0]] = point_list

    return weekly_points

# The second function is for determining the grade based on the points received. 
# This function is in turn used by the third function, which writes the results to the file.
def grade(points):
    if points < 20:
        return 0
    elif points < 25:
        return 1
    elif points < 30:
        return 2
    elif points < 35:
        return 3
    elif points < 40:
        return 4
    else:
        return 5

def save_results(filename, weekly_points):
    with open(filename, "w") as my_file:
        for name, point_list in weekly_points.items():
            point_sum = sum(point_list)
            my_file.write(f"{name};{point_sum};{grade(point_sum)}\n")

# This structure lets us write a very simple main function. 
# Notice how the filenames for the files whch are read and written are given as arguments in the main function:
weekly_points = read_weekly_points("weekly_points.csv")
save_results("results.csv", weekly_points)

# When the main function is executed, the contents of the file 'results.csv' created as a result looks like this:
'''
Peter;18;0
Paula;34;3
Susan;26;2
Emily;41;5
'''

# Notice how each function defined above is relatively simple, and they all have a single responsibility. 
# This is a common and advisable approach when programming larger wholes. 
# The single reponsibility principle makes verifying functionality easier. 
# It also makes it easier to make changes to the program later, and to add new features.

# Say we wanted to add a function for printing out the grade for a single student. 
# We already have a function which determines the student's grade, so we can use this in our new function:
def get_grade(student_name, weekly_points):
    for name, point_list in weekly_points.items():
        if name == student_name:
            return grade(sum(point_list))


weekly_points = read_weekly_points("weekly_points.csv")
print(get_grade("Paula", weekly_points))

# If we determine a certain functionality in the program needs fixing, in a well designed program the change will affect only some select sections of code, and it will be easier to determine where the changes should be made. 
# For example, if we wanted to change the grade boundaries, we'd only need to implement the change in the function for determining the grade, and it would work also in all the other functions utilizing this function. 
# If the code for this single functionality was implemented in multiple places, there would be a definite risk that we would not remember to change all the instances when changing the functionality.

# Inscription
sign = input("Whom should I sign this to: ")
file = input("Where shall I save it: ")

with open(file, "w") as inscription:
    inscription.write(f"Hi {sign}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

# Diary - Approach 1
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        entry = input("Diary entry: ")
        
        with open("diary.txt", "a") as diary:
            diary.write(f"{entry}\n")
        
        print("Diary saved")
    
    if function == 2:
        with open("diary.txt") as diary:
            print("Entries:")
            for line in diary:
                line = line.strip()
                print(line)
    
    if function == 0:
        print("Bye now!")
        break

# Diary - Approach 2
# Read the markings first
with open("diary.txt") as file:
    content = []
    for row in file:
        content.append(row.replace("\n",""))
 
# Open file for appending
with open("diary.txt", "a") as file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")
        if function == "1":
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            content.append(entry)
            print("Diary saved")
        elif function == "2":
            print("Entries:")
            for entry in content:
                print(entry)
        elif function == "0":
            print("Bye now!")
            break

# Diary - Approach 2
# Read the markings first
with open("diary.txt") as file:
    content = []
    for row in file:
        content.append(row.replace("\n",""))
 
# Open file for appending
with open("diary.txt", "a") as file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")
        if function == "1":
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            content.append(entry)
            print("Diary saved")
        elif function == "2":
            print("Entries:")
            for entry in content:
                print(entry)
        elif function == "0":
            print("Bye now!")
            break
        
# Filtering the contents of a file - Approach 1
def filter_solutions():
    with open("Exercise Files/solutions.csv") as calculations:
        correct_list = []
        incorrect_list = []
        for line in calculations:
            line = line.strip()
            parts = line.split(";")
            result = int(parts[2])
            if parts[1].find("+") > 0:
                index = parts[1].find("+")
                operand1 = parts[1][:index]
                operand2 = parts[1][index+1:]
                correct = int(operand1) + int(operand2)
            if parts[1].find("-") > 0:
                index = parts[1].find("-")
                operand1 = parts[1][:index]
                operand2 = parts[1][index+1:]
                correct = int(operand1) - int(operand2)
            row = []
            if result == correct:
                for part in parts:
                    row.append(part)
                correct_list.append(row)
            else:
                for part in parts:
                    row.append(part)
                incorrect_list.append(row)

    with open("Exercise Files/correct.csv", "w") as my_file:
        for result in correct_list:
            line = ""
            for value in result:
                line += f"{value};"
            line = line[:-1]
            my_file.write(line+"\n")
            
    with open("Exercise Files/incorrect.csv", "w") as my_file:
        for result in incorrect_list:
            line = ""
            for value in result:
                line += f"{value};"
            line = line[:-1]
            my_file.write(line+"\n")

filter_solutions()

# ⭐ ⭐ Filtering the contents of a file - Approach 2
def filter_solutions():
    # Open all files -> Done on a single line
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")
 
            calculation = pieces[1]
            result = pieces[2]
 
            # Addition or subtraction?
            if "+" in calculation:
                operands = calculation.split("+")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) - int(operands[1]) == int(result)
 
            # Write to file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)

# Approach 2 - Analysis
test = "4-5"
result = "-1"
# if-in condition statement checks whether the character can be found in the string.
if "+" in test:
    operand = test.split("+")
    print(operand)
    # Saves either True or False in the 'correct' variable for further conditional flow.
    correct = int(operand[0]) + int(operand[1]) == int(result)
    print(correct)
else:
    operand = test.split("-")
    print(operand)
    # Saves either True or False in the 'correct' variable for further conditional flow.
    correct = int(operand[0]) - int(operand[1]) == int(result)
    print(correct)

# Store personal data - Approach 1
def store_personal_data(person: tuple):
    with open("Exercise Files\people.csv", "a") as database:
        line = ""
        for data in person:
            line += f"{data};"
        line = line[:-1]
        database.write("\n" + line)
        
store_personal_data(("Paul Paulson", 37, 175.5))

# Store personal data - Approach 2
def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        row = person[0] + ";"
        row += str(person[1]) + ";"
        row += str(person[2])
 
        file.write(row + "\n")

# Handling data in a CSV format

# Program assesses students' performance on a course
# The program reads a CSV file, which contains weekly exercise points received by the students. 
# The program then calculates the points total and determines the grade attained by each student. 
# Finally, the program creates a CSV file containing the points total and grade for each student.

'''
The CSV file given as input to the program looks like this:

Peter;4;2;3;5;4;0;0
Paula;7;2;8;3;5;4;5
Susan;3;4;3;5;3;4;4
Emily;6;6;5;5;0;4;8
'''

# The program logic is divided into three functions: reading the file and processing the contents into an accessible format, determining the grade, and writing the file.

# The data is stored in a dictionary, where the key is the student's name, and the value is a list of the points received by the student, in integer format:
def read_weekly_points(filename):
    weekly_points = {}
    with open(filename) as my_file:
        for line in my_file:
            parts = line.split(";")
            point_list = []
            for points in parts[1:]:
                point_list.append(int(points))
            weekly_points[parts[0]] = point_list

    return weekly_points

# The second function is for determining the grade based on the points received. 
# This function is in turn used by the third function, which writes the results to the file.

def grade(points):
    if points < 20:
        return 0
    elif points < 25:
        return 1
    elif points < 30:
        return 2
    elif points < 35:
        return 3
    elif points < 40:
        return 4
    else:
        return 5

def save_results(filename, weekly_points):
    with open(filename, "w") as my_file:
        for name, point_list in weekly_points.items():
            point_sum = sum(point_list)
            my_file.write(f"{name};{point_sum};{grade(point_sum)}\n")
            

# This structure lets us write a very simple main function. 
# Notice how the filenames for the files whch are read and written are given as arguments in the main function:
weekly_points = read_weekly_points("weekly_points.csv")
save_results("results.csv", weekly_points)


'''
When the main function is executed, the contents of the file results.csv created as a result looks like this:

Peter;18;0
Paula;34;3
Susan;26;2
Emily;41;5
'''

# Notice how each function defined above is relatively simple, and they all have a single responsibility.
# This is a common and advisable approach when programming larger wholes. 
# The single reponsibility principle makes verifying functionality easier. 
# It also makes it easier to make changes to the program later, and to add new features.

# Say we wanted to add a function for printing out the grade for a single student. 
# We already have a function which determines the student's grade, so we can use this in our new function:
def get_grade(student_name, weekly_points):
    for name, point_list in weekly_points.items():
        if name == student_name:
            return grade(sum(point_list))


weekly_points = read_weekly_points("weekly_points.csv")
print(get_grade("Paula", weekly_points))

# If we determine a certain functionality in the program needs fixing, in a well designed program the change will affect only some select sections of code, and it will be easier to determine where the changes should be made.
# For example, if we wanted to change the grade boundaries, we'd only need to implement the change in the function for determining the grade, and it would work also in all the other functions utilizing this function. 
# If the code for this single functionality was implemented in multiple places, there would be a definite risk that we would not remember to change all the instances when changing the functionality.

# Course grading, part 4

# RECAP: Course grading, part 3 - Approach 1
if False:
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
print(students)

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
            
print(exercises)

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

print(exams)

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
            print(f"{name:30}{sum(exercises[pic]):<10}{exercises_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")
            break
        else:
            continue 


# RECAP: Course grading, part 3 - Approach 2
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
 
def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
 
    return a
 
def to_points(number):
    return number // 4
 
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum
 
exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        esum = 0
        for i in range(1, 4):
            esum += int(parts[i])
        exams[parts[0]] = esum
 
print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for eid, name in students.items():
    exec_nbr = exercises[eid]
    exec_score = to_points(exec_nbr)
    exam_points = exams[eid]
    total_points = exec_score + exam_points
    print(f"{name:30}{exec_nbr:<10}{exec_score:<10}{exam_points:<10}{total_points:<10}{grade(total_points):<10}")

# Course grading, part 4 - Approach 1

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
if False:
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


# Course grading, part 4 - Approach 2
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
course_data = input("Course information: ")
 
def get_grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
    return a
 
def as_score(number):
    return number // 4
 
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum
 
exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        esum = 0
        for i in range(1, 4):
            esum += int(parts[i])
        exams[parts[0]] = esum
 
with open(course_data) as file:
    rows = []
    for row in file:
        rows.append(row)
 
    course_name = rows[0][5:].strip()
    credits = int(rows[1][14:])
 
with open("results.txt", "w") as file:
    header = f"{course_name}, {credits} credits\n"
    file.write(header)
    separator = "="*(len(header)-1)
    file.write(f"{separator}\n")
    file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for student_id, name in students.items():
        exer = exercises[student_id]
        exer_score = as_score(exer)
        exam_pts = exams[student_id]
        tot_score = exer_score + exam_pts
        file.write(f"{name:30}{exer:<10}{exer_score:<10}{exam_pts:<10}{tot_score:<10}{get_grade(tot_score):<10}\n")
 
with open("results.csv", "w") as file:
    for student_id, name in students.items():
        exer = exercises[student_id]
        exer_score = as_score(exer)
        exam_pts = exams[student_id]
        tot_score = exer_score + exam_pts
        row = ";".join([student_id, name, str(get_grade(tot_score))])
        file.write(f"{row}\n")
        
# Word search - Approach 1
def find_words(search_term: str) -> list:
    return wildcard(search_term)

# Identify wildcard in search_term
def wildcard(search_term: str) -> list:
    if "." in search_term:
        index = 0
        search_term_dict = {}
        for letter in search_term:
            if letter != ".":
                search_term_dict[index] = letter
            index += 1
        return dot_search(search_term, search_term_dict)
    
    if search_term[0] == "*":
        return end_search(search_term[1:])
    
    if search_term[len(search_term) - 1] == "*":
        return start_search(search_term[:-1])
    
    else:
        return exact_search(search_term)
    
# Conduct search based on wildcard feature 
def dot_search(search_term: str, search_term_dict: dict) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if len(word) == len(search_term):
                z = True
                helper = ""
                for index, letter in search_term_dict.items():
                    if word[index] == letter and z:
                        helper = word
                    else:
                        helper = ""
                        z = False
                if z:
                    match.append(helper)
    return match

def end_search(search_term_suffix: str) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if word.endswith(search_term_suffix):
                match.append(word)
    return match

def start_search(search_term_prefix: str) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if word.startswith(search_term_prefix):
                match.append(word)
    return match

def exact_search(search_term: str) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if word == search_term:
                match.append(word)
    return match

match = find_words('india')
print(match)

# Word search - Approach 2
def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        # This will be needed later
        search_without_asterisk = search_term.replace("*","")
 
        for word in file:
            word = word.replace("\n","")
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(search_without_asterisk):
                        results.append(word)
                else:
                    if word.startswith(search_without_asterisk):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results

# Dictionary stored in a file - Approach 1
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish};{english}\n")
            print("Dictionary entry added")
        continue
    if function == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                parts = line.strip()
                part = parts.split(";")
                if search in part[0] or search in part[1]:
                    print(f"{part[0]} - {part[1]}")
        continue
    else:
        print("Bye!")
        break

# Dictionary stored in a file - Approach 2
def read_dictionary():
    # Words are stored in a list. If the translation would always
    # be to same direction (e.g. from English to Finnish),
    # using dictionary as a data structure would be a good idea
    dictionary = []
 
    with open("dictionary.txt") as file:
        # In the example file, word pair is at one line as
        # finnish;english, for example
        # auto;car
        for row in file:
            row = row.replace("\n","")
            dictionary.append(tuple(row.split(";")))
 
    return dictionary
 
def add_word(dictionary: list):
    word_fi = input("The word in Finnish: ")
    word_en = input("The word in English: ")
    # Add to list
    dictionary.append((word_fi, word_en))
 
    # Write to file
    with open("dictionary.txt", "a") as file:
        file.write(word_fi + ";" + word_en + "\n")
        print("Dictionary entry added")
 
def search_word(dictionary: list):
    word = input("Search term: ")
    for word_fi, word_en in dictionary:
        if word in word_fi or word in word_en:
            print(f"{word_fi} - {word_en}")
 
 
dictionary = read_dictionary()
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        add_word(dictionary)
    elif function == "2":
        search_word(dictionary)
    elif function == "3":
        print("Bye!")
        break