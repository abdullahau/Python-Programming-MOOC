# 'with' statement Example 1

# The header line opens the file, and the block where the file can be accessed follows. 
# After the block the file is automatically closed, and can no longer be accessed.

with open("Exercise Files\example.txt") as new_file:
    contents = new_file.read()
    print(contents)

# Going through the contents of a file
with open("Exercise Files\example.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        line = line.replace("\n", "")
        count += 1
        print("Line", count, line)
        length = len(line)
        total_length += length

print("Total length of lines:", total_length)


# Largest number - Approach 1
def largest():
    with open('numbers.txt') as new_file:
        largest_number = 0
        
        for line in new_file:
            number = int(line)
            if number > largest_number:
                largest_number = number
        return largest_number

if __name__ == "__main__":
    largest()

# Largest number - Approach 2
def largest():
    with open("numbers.txt") as file:
        start = True
        biggest = 0
        for number in file:
            if start or int(number) > biggest:
                biggest = int(number)
                start = False
        return biggest


# '.split()' string method takes the separator character(s) as a string argument, and returns the contents of the target string as a list of strings, separated at the separator.
text = "monkey,banana,harpsichord"
words = text.split(",")
for word in words:
    print(word)

# Reading CSV files
with open("Exercise Files\grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        print("Name:", name)
        print("Grades:", grades) 
        
# Fruit market
def read_fruits():
    with open('Exercise Files\\fruits.csv') as file:
        fruits = {}
        
        for row in file:
            # split to two pieces
            data = row.split(";")
            # name first, price second
            fruits[data[0]] = float(data[1])
    return fruits

read_fruits()

# Matrix - Approach 1
def matrix_sum():
    with open("Exercise Files\matrix.txt") as matrix:
        sum = 0
        
        for row in matrix:
            row = row.replace("\n", "")
            row = row.split(",")
            for num in row:
                element = int(num)
                sum += element 
        return sum

matrix_sum()

def matrix_max():
    with open("Exercise Files\matrix.txt") as matrix:
        max = 0
        
        for row in matrix:
            row = row.replace("\n", "")
            row = row.split(",")
            for num in row:
                element = int(num)
                if element > max:
                    max = element
        return max

matrix_max()

def row_sums():
    with open("Exercise Files\matrix.txt") as matrix:
        sums = []
        
        for row in matrix:
            row = row.replace("\n", "")
            row = row.split(",")
            sum = 0
            for num in row:
                element = int(num)
                sum += element
            sums.append(sum)
        return sums
    
row_sums()

# Matrix - Approach 2
def read_matrix():
    with open("Exercise Files\matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m
 
# Combines the rows of a matrix into a single list
def combine(matriisi: list):
    mlist = []
    for row in matriisi:
        mlist += row
    
    return mlist
 
def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)
 
def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)
 
def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums

combine(read_matrix())

# Reading the same file multiple times
'''
Peter;40;Helsinki
Emily;34;Espoo
Eric;42;London
Adam;100;Amsterdam
Alice;58;Paris
'''

with open("people.csv") as new_file:
    # print out the names
    for line in new_file:
        parts = line.split(";")
        print("Name:", parts[0])

    # find the oldest
    age_of_oldest = -1
    for line in new_file:
        parts = line.split(";")
        name = parts[0]
        age = int(parts[1])
        if age > age_of_oldest:
            age_of_oldest = age
            oldest = name
    print("the oldest is", oldest)
    
# The latter for loop is not executed at all, beacuse the file can only be processed once.
# Once the last line is read, the file handle rests at the end of the file, and the data in the file can no longer be accessed.

# If we want to access the contents in the second for loop, we will have to open the file a second time:
with open("people.csv") as new_file:
    # print out the names
    for line in new_file:
        parts = line.split(";")
        print("Name:", parts[0])

with open("people.csv") as new_file:
    # find the oldest
    age_of_oldest = -1
    for line in new_file:
        parts = line.split(";")
        name = parts[0]
        age = int(parts[1])
        if age > age_of_oldest:
            age_of_oldest = age
            oldest = name
    print("the oldest is", oldest)

# While the above code would work, it contains unnecessary repetition. 
# It is usually best to read the file just once, and store its contents in an appropriate format for further processing:
people = []
# read the contents of the file and store it in a list
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        people.append((parts[0], int(parts[1]), parts[2]))

# print out the names
for person in people:
    print("Name:", person[0])

# find the oldest
age_of_oldest = -1
for person in people:
    name = person[0]
    age = person[1]
    if age > age_of_oldest:
        age_of_oldest = age
        oldest = name
print("the oldest is", oldest)

# More CSV file processing
grades = {}
with open("Exercise Files\grades.csv") as new_file:
    for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            grades[name] = []
            for grade in parts[1:]:
                grades[name].append(int(grade))
print(grades)

for name, grade_list in grades.items():
    best = max(grade_list)
    average = sum(grade_list) / len(grade_list)
    print(f"{name}: best grade {best}, average {average:.2f}")

# Removing unnecessary lines, spaces and line breaks
'''
first; last
Paul; Python
Jean; Java
Harry; Haskell
'''

last_names = []
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        # ignore the header line
        if parts[0] == "first":
            continue
        last_names.append(parts[1])

print(last_names)

'''
output:
[' Python\n', ' Java\n', ' Haskell']
'''

# A more efficient solution is to use the Python string method 'strip', which removes whitespace from the beginning and end of a string. 
# It removes all spaces, line breaks, tabs and other characters which would not normally be printed out.

'''
>>> " tryout ".strip()
'tryout'
>>> "\n\ntest\n".strip()
'test'
>>>
'''

# Stripping the string requires the following change to the program:
last_names = []
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "first":
            continue # this was the header line, so it is ignored
        last_names.append(parts[1].strip())
print(last_names)

'''
['Python', 'Java', 'Haskell']
'''

# There are also the related string methods 'lstrip' and 'rstrip'. 
# They remove only the leading or trailing unprintable characters, l for the left edge of the string and r for the right:

'''
>>> " teststring  ".rstrip()
' teststring'
>>> " teststring  ".lstrip()
'teststring  '
'''

# Combining data from different files

# employees.csv
'''
pic;name;address;city
080488-123X;Pekka Mikkola;Vilppulantie 7;00700 Helsinki
290274-044S;Liisa Marttinen;Mannerheimintie 100 A 10;00100 Helsinki
010479-007Z;Arto Vihavainen;Pihapolku 4;01010 Kerava
010499-345K;Leevi Hellas;Tapiolantie 11 B;02000 Espoo
'''

# salaries.csv
'''
pic;salary;bonus
080488-123X;3300;0
290274-044S;4150;200
010479-007Z;1300;1200
'''

# Output
'''
incomes:
Pekka Mikkola    3300 euros
Liisa Marttinen  4350 euros
Arto Vihavainen  2500 euros
'''

# This program uses two dictionaries as helper data structures: 'names' and 'salaries'. 
# Both use the PIC as key:

names = {}

with open("employees.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        names[parts[0]] = parts[1]

salaries = {}

with open("salaries.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        salaries[parts[0]] = int(parts[1]) +int(parts[2])

print("incomes:")

for pic, name in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{name:16} {salary} euros")
    else:
        print(f"{name:16} 0 euros")
        
        
# First the program produces the dictionaries names and salaries. They have the following contents:
{
    '080488-123X': 'Pekka Mikkola',
    '290274-044S': 'Liisa Marttinen',
    '010479-007Z': 'Arto Vihavainen',
    '010499-345K': 'Leevi Hellas'
}

{
    '080488-123X': 3300,
    '290274-044S': 4350,
    '010479-007Z': 2500
}

# The for loop at the end of the program combines the names of the employees with their respective salaries.

# The program also takes care of situations where the employee's pic is not present in the salary file.

# Remember, the order in which items are stored in a dictionary does not matter, as the keys are processed based on hash values.

# Course grading, part 1 - Approach 1
if False:
    # Not executed until True
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "Exercise Files\course-grading-part-1\students1.csv"
    exercise_data = "Exercise Files\course-grading-part-1\exercises1.csv"

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

for pic, name in students.items():
    if pic in exercises:
        total_exercises = sum(exercises[pic])
        print(f"{name} {total_exercises}")
    else:
        print(f"{name} 0")
        
# Course grading, part 1  - Approach 2
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
 
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
 
for student_id, name in students.items():
    print(f"{name} {exercises[student_id]}")
    

# Course grading, part 2 - Approach 1
if False:
    # Not executed until True
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "Exercise Files\course-grading-part-2\students1.csv"
    exercise_data = "Exercise Files\course-grading-part-2\exercises1.csv"
    exam_data = "Exercise Files\course-grading-part-2\exam_points1.csv"

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

for pic, name in students.items():
    exercises_points = sum(exercises[pic]) // 4
    exam_points = sum(exams[pic])
    total_points = exercises_points + exam_points
    grades = [0, 1, 2, 3, 4, 5]
    points = [0, 15, 18, 21, 24, 28]
    for point in points[::-1]:
        if total_points >= point:
            grade = grades[points.index(point)]
            print(f"{name} {grade}")
            break
        else:
            continue

# Course grading, part 2 - Approach 2
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
 
for student_id, name in students.items():
    total = exams[student_id] + to_points(exercises[student_id])
    print(f"{name} {grade(total)}")

# Course grading, part 3 - Approach 1
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


'''
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3
'''

# Course grading, part 3 - Approach 2
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


# Spell checker - Approach 1
if False:
    text = input("Write text: ")
else:
    text = "This is acually a good and usefull program"

text = text.split(" ")

with open("Exercise Files\wordlist.txt") as wordlist:
    words = []
    for line in wordlist:
        word = line.strip()
        words.append(word)

sentence = ""
for texts in text:
    if texts.lower() in words:
        sentence += texts + " "
    else:
        sentence += "*" + texts + "* "

print(sentence.strip())

# Spell checker - Approach 2
def wordlist():
    words = []
 
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
 
    return words
 
words = wordlist()
sentence = input("Write text: ")
 
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "* ", end="")
 
print()


# Recipe search - Approach 1

# Part 1 - Search for recipes based on the name of the recipe
with open('Exercise Files/recipes1.txt') as my_recipes:
    recipe_name = []
    counter = 0
    for recipe in my_recipes:
        if counter == 0:
            recipe_name.append(recipe.strip())
            counter += 1
        if recipe == '\n':
            counter = 0
        else:
            counter += 1

print(recipe_name)

for recipe in recipe_name:
    if "cake" in recipe.lower():
        print(recipe)

# Part 2 - Search for recipes based on the preparation time
with open("Exercise Files/recipes1.txt") as new_file:
    prep_time = {}
    recipe = ""
    for line in new_file:
        line = line.strip()
        if line.isnumeric():
            prep_time[int(line)] = recipe
        else:
            recipe = line

prep_time

for time, recipe in prep_time.items():
    if time <= 30:
        print(f"{recipe}, preparation time {time} min")

# Part 3 - Search for recipes based on the ingredients
with open("Exercise Files/recipes1.txt") as new_file:
    prep_time = {}
    recipe = {}
    ingredients = []
    recipe_name = ""
    counter = 0
    for line in new_file:
        line = line.strip()
        if line.isnumeric():
            prep_time[recipe_name] = int(line)
            counter = 1
        elif counter == 1:
            if line == '':
                recipe[recipe_name] = ingredients
                ingredients = []
                counter = 0
                continue
            ingredients.append(line)
        else:
            recipe_name = line
            counter = 0 
    recipe[recipe_name] = ingredients

recipe

prep_time

for recipe_name, ingredients in recipe.items():
    if "milk" in ingredients:
        print(f"{recipe_name}, preparation time {prep_time[recipe_name]} min")
        
for recipe_name, ingredients in recipe.items():
    if "cake" in recipe_name.lower():
        print(recipe_name)


# Combined
def openfile(filename: str):
    with open(filename) as new_file:
        prep_time = {}
        recipe = {}
        ingredients = []
        recipe_name = ""
        counter = 0
        for line in new_file:
            line = line.strip()
            if line.isnumeric():
                prep_time[recipe_name] = int(line)
                counter = 1
            elif counter == 1:
                if line == '':
                    recipe[recipe_name] = ingredients
                    ingredients = []
                    counter = 0
                    continue
                ingredients.append(line)
            else:
                recipe_name = line
                counter = 0 
        recipe[recipe_name] = ingredients
        return prep_time , recipe

def search_by_name(filename: str, word: str):
    prep_time, recipe = openfile(filename)
    recipe_list = []
    for recipe_name, ingredients in recipe.items():
        if word.lower() in recipe_name.lower():
            recipe_list.append(recipe_name)
    return recipe_list

def search_by_time(filename: str, prep_duration: int):
    prep_time, recipe = openfile(filename)
    recipe_list = []
    for recipe_name, duration in prep_time.items():
        if duration <= prep_duration:
            recipe_list.append(f"{recipe_name}, preparation time {duration} min")
    return recipe_list

def search_by_ingredient(filename: str, ingredient: str):
    prep_time, recipe = openfile(filename)
    recipe_list = []
    for recipe_name, ingredients in recipe.items():
        if ingredient in ingredients:
            recipe_list.append(f"{recipe_name}, preparation time {prep_time[recipe_name]} min")
    return recipe_list
        
            
if False:
    search_by_name("recipes1.txt", "milk")
else:
    search_by_name(r"Exercise Files\\recipes1.txt", "cake")
    search_by_time(r"Exercise Files\\recipes1.txt", 30)
    search_by_ingredient(r"Exercise Files\\recipes1.txt", "milk")


# Recipe search - Approach 2
def read_file(filename):
    with open(filename) as file:
        rows = []
        for row in file:
            rows.append(row.strip())
 
    recipes = []
    name_in_row = True
    prep_time_in_row = True
    new = { "ingredients": []}
    for row in rows:
        if name_in_row:
            new["name"] = row
            name_in_row = False
            prep_time_in_row = True
        elif prep_time_in_row:
            new["prep_time"] = int(row)
            prep_time_in_row = False
        elif len(row) > 0:
            new["ingredients"].append(row)
        else:
            recipes.append(new)
            name_in_row = True
            new = {"ingredients": []}
    recipes.append(new)
 
    return recipes
 
def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
 
    return found
 
def search_by_time(filename: str, time: int):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if recipe["prep_time"] <= time:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found
 
def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found

# Recipe search - Approach 2 (To be reviewed)
def read_file(filename):
    with open(filename) as file:
        rows = []
        for row in file:
            rows.append(row.strip())
 
    recipes = []
    name_in_row = True
    prep_time_in_row = True
    new = { "ingredients": []}
    for row in rows:
        if name_in_row:
            new["name"] = row
            name_in_row = False
            prep_time_in_row = True
        elif prep_time_in_row:
            new["prep_time"] = int(row)
            prep_time_in_row = False
        elif len(row) > 0:
            new["ingredients"].append(row)
        else:
            recipes.append(new)
            name_in_row = True
            new = {"ingredients": []}
    recipes.append(new)
 
    return recipes
 
def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
 
    return found
 
def search_by_time(filename: str, time: int):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if recipe["prep_time"] <= time:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found
 
def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found

# City bikes - Approach 1
def get_station_data(filename: str):
    with open(filename) as stations_data:
        station_dict = {}
        for line in stations_data:
            line = line.strip()
            part = line.split(";")
            if part[0] == "Longitude":
                continue
            station_dict[part[3]] = (float(part[0]), float(part[1]))
        return station_dict

def distance(stations: dict, station1: str, station2: str):
    for station, coordinates in stations.items():
        if station == station1:
            longitude1 = coordinates[0]
            latitude1 = coordinates[1]
        elif station == station2:
            longitude2 = coordinates[0]
            latitude2 = coordinates[1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = (x_km**2 + y_km**2)**(1/2)
    return distance_km

def greatest_distance(stations: dict):
    distance = 0 
    station_x = ""
    station_y = ""
    for station1, coordinates1 in stations.items():
        for station2, coordinates2 in stations.items():
            longitude1 = coordinates1[0]
            latitude1 = coordinates1[1]
            longitude2 = coordinates2[0]
            latitude2 = coordinates2[1]
            x_km = (longitude1 - longitude2) * 55.26
            y_km = (latitude1 - latitude2) * 111.2
            distance_km = (x_km**2 + y_km**2)**(1/2)
            if distance_km > distance:
                distance = distance_km
                station_x = station1
                station_y = station2
    return station_x, station_y, distance

stations = get_station_data(r"Exercise Files\stations1.csv")

d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)
d = distance(stations, "Viiskulma", "Kaivopuisto")
print(d)

station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)

for station, tup in stations.items():
    print(f"{station}, long = {tup[0]}, lat = {tup[1]}")


# City bikes - Approach 2
import math
 
def get_station_data(filename:str):
    stations = {}
    with open(filename) as file:
        for row in file:
            parts = row.split(";")
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
 
    return stations
 
def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
 
    # Note, that this
    # longitude2, latitude2 = stations[station2]
    # ...is equivalent to
    #
    # coordinates = stations[station2]
    # longitude2 = coordinates[0]
    # latitude2 = coordinates[0]
 
    x_as_km = (longitude1-longitude2) * 55.26
    y_as_km = (latitude1-latitude2) * 111.2
    return math.sqrt(x_as_km**2 + y_as_km**2)
 
def greatest_distance(stations: dict):
    longest = 0
    for start_station in stations:
        for end_station in stations:
            e = distance(stations, start_station, end_station)
            if e > longest:
                station1 = start_station
                station2 = end_station
                longest = e
 
    return station1, station2, longest