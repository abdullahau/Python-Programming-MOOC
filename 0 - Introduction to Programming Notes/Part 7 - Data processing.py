# Data processing

# Reading CSV files
# CSV is such a simple format that so far we have accessed the 'with' hand-written code. 
# There is, however, a ready-made module in the Python standard library for working with CSV files: csv. 
# https://docs.python.org/3/library/csv.html
# It works like this:

import csv

with open("test.csv") as my_file:
    for line in csv.reader(my_file, delimiter=";"):
        print(line)

# The above code reads all lines in the CSV file 'test.csv', separates the contents of each line into a list using the delimiter ';', and prints each list. 
# So, assuming the contents of the line are as follows:
'''
012121212;5
012345678;2
015151515;4
'''

# The code would print out this:
'''
['012121212', '5']
['012345678', '2']
['015151515', '4']
'''

# Since the CSV format is so simple, what's the use of having a separate module when we can just as well use the 'split' function? 
# Well, for one, the way the module is built, it will also work correctly if the values in the file are strings, which may also contain the delimiter character. 
# If some line in the file looked like this
'''
"aaa;bbb";"ccc;ddd"
'''
# the above code would produce this:
'''
['aaa;bbb', 'ccc;ddd']
'''
# Using the split function would also split within the strings, which would likely break the data, and our program in the process.

# Reading JSON files
# JSON is used often when data has to be transferred between applications.
# https://www.json.org/json-en.html

# JSON files are text files with a strict format, which is perhaps a little less accessible to the human eye than the CSV format. 
# The following example uses the file courses.json, which contains information about some courses:
'''
[
    {
        "name": "Introduction to Programming",
        "abbreviation": "ItP",
        "periods": [1, 3]
    },
    {
        "name": "Advanced Course in Programming",
        "abbreviation": "ACiP",
        "periods": [2, 4]
    },
    {
        "name": "Database Application",
        "abbreviation": "DbApp",
        "periods": [1, 2, 3, 4]
    }
]
'''

# The JSON file above looks exactly like a Python list, which contains three Python dictionaries.

# The standard library has a module for working with JSON files: 'json'. 
# https://docs.python.org/3/library/json.html
# The function 'loads' takes any argument passed in as JSON format and transforms it into a Python data structure. 
# So, processing the 'courses.json' file with the code below
import json

with open("courses.json") as my_file:
    data = my_file.read()

courses = json.loads(data)
print(courses)

# would print out the following:
'''
[{'name': 'Introduction to Programming', 'abbreviation': 'ItP', 'periods': [1, 3]}, 
{'name': 'Advanced Course in Programming', 'abbreviation': 'ACiP', 'periods': [2, 4]}, 
{'name': 'Database Application', 'abbreviation': 'DbApp', 'periods': [1, 2, 3, 4]}]
'''

# If we also wanted to print out the name of each course, we could expand our program with a 'for' loop:
for course in courses:
    print(course["name"])
    
'''
Introduction to Programming
Advanced Course in Programming
Database Application
'''


# Handling JSON files - review
# Please write a function named 'print_persons(filename: str)', which reads a JSON file, and prints the contents in the below structure. 
# The file may contain any number of entries.
'''
Peter Pythons 27 years (coding, knitting)
Jean Javanese 24 years (coding, rock climbing, reading)
'''
# The hobbies should be listed in the same order as they appear in the JSON file.


# String method "join()" to join elements of a list together
l = ['coding', 'knitting']
print(", ".join(l))



# Handling JSON files - Approach 1
import json


def print_persons(filename: str): 
    with open(filename) as my_file:
        data = json.loads(my_file.read())
        
    for i in data:
        print(f"{i["name"]} {i["age"]} years ({", ".join(i["hobbies"])})")

print_persons("Exercise Files\\file2.json")


# Handing JSON files - Approach 2
import json
def print_persons(filename: str):
    with open(filename) as f:
        content = f.read()
    persons = json.loads(content)
    for person in persons:
        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        print(f"{name} {age} years ({hobbies})")
        
# Retrieving a file from the internet

# The Python standard library also contains modules for dealing with online content, and one useful function is 'urllib.request.urlopen'. 
# https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
# It can be used to retrieve content from the internet, so it can be processed in your programs.

# The following code would print out the contents of the University of Helsinki front page:

import urllib.request

my_request = urllib.request.urlopen("https://helsinki.fi")
print(my_request.read())  

# In the following examples, however, we will work with machine-readable data from an online source. 
# Much of the machine-readable data available online is in JSON format.

# Course statistics - Review

# Part 1 - Retrieving the list of active courses

# At the address https://studies.cs.helsinki.fi/stats-mock/api/courses you will find basic information about some of the courses offered by the University of Helsinki Department of Computer Science, in JSON format.

# Please write a function named 'retrieve_all()', which retrieves the data of all the courses which are currently active (the field 'enabled' has the value 'true'). 
# These should be returned as a list of tuples, in the following format:
'''
[
    ('Full Stack Open 2020', 'ofs2019', 2020, 201),
    ('DevOps with Docker 2019', 'docker2019', 2019, 36),
    ('DevOps with Docker 2020', 'docker2020', 2020, 36),
    ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
]
'''

# Each tuple contains the following fields from the original data:
    # the name of the course: 'fullName'
    # 'name'
    # 'year'
    # the sum of the values listed in 'exercises'

# Import JSON data and load into json module
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())

    retrieved_list = []
    for i in data:
        if i["enabled"] == True:
            retrieved_tuple = i["fullName"], i["name"], i["year"], sum(i["exercises"])
            retrieved_list.append(retrieved_tuple)

    return retrieved_list


# Part 2 - Retrieving the data for a single course

# Each course also has its own URL, where more specific weekly data about the course is available. 
# The URLs follow the format https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats, where you would replace the stars with the contents of the field 'name' for the course you want to access.

# For example, the data for the course 'docker2019' is at the address https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats.

# Please write a function named 'retrieve_course(course_name: str)', which returns statistics for the specified course, in dictionary format.

# For example, the function call 'retrieve_course("docker2019")' would return a dictionary with the following contents:
'''
{
    'weeks': 4,
    'students': 220,
    'hours': 5966,
    'hours_average': 27,
    'exercises': 4988,
    'exercises_average': 22
}
'''

# 'docker2019' json data
'''
{
    '0': {'students': 220, 'hour_total': 286, 'exercise_total': 218, 'hours': [None, 176, 11, 3, 1, 1, None, None, 6]}, 
    '1': {'students': 176, 'hour_total': 2421, 'exercise_total': 2748, 'hours': [None, 6, 3, 3, 4, 9, 5, 8, 13, 4, 28, 1, 14, 2, 3, 20, 2, 4, 3, None, 15, 1, 1, None, 6, 5, None, 1, 2, None, 8, None, None, None, None, 1, None, None, None, None, 2, 2]}, 
    '2': {'students': 143, 'hour_total': 1862, 'exercise_total': 1343, 'hours': [None, 1, 1, 5, 5, 8, 8, 3, 10, 7, 21, 1, 11, 6, 1, 11, 7, 2, 4, None, 10, None, None, None, 4, 3, 1, None, None, None, 3, 2, None, None, None, 5]}, 
    '3': {'students': 99, 'hour_total': 1397, 'exercise_total': 679, 'hours': [None, 1, 2, 1, 2, 4, 7, 5, 10, 1, 17, 1, 3, 3, 5, 7, 2, 1, 1, None, 8, None, 1, None, 3, 3, 1, None, None, None, 1, None, 1, None, None, 8]}
}
'''

# The values in the dictionary are determined as follows:
    # 'weeks': the number of JSON object literals retrieved
    # 'students': the maximum number of students in all the weeks
    # 'hours': the sum of all 'hour_total' values in the different weeks
    # 'hours_average': the 'hours' value divided by the 'students' value (rounded down to the closest integer value)
    # 'exercises': the sum of all 'exercise_total' values in the different weeks
    # 'exercises_average': the 'exercises' value divided by the 'students' value (rounded down to the closest integer value)

test_dict = {
    '0': {'students': 220, 'hour_total': 286, 'exercise_total': 218, 'hours': [None, 176, 11, 3, 1, 1, None, None, 6]}, 
    '1': {'students': 176, 'hour_total': 2421, 'exercise_total': 2748, 'hours': [None, 6, 3, 3, 4, 9, 5, 8, 13, 4, 28, 1, 14, 2, 3, 20, 2, 4, 3, None, 15, 1, 1, None, 6, 5, None, 1, 2, None, 8, None, None, None, None, 1, None, None, None, None, 2, 2]}, 
    '2': {'students': 143, 'hour_total': 1862, 'exercise_total': 1343, 'hours': [None, 1, 1, 5, 5, 8, 8, 3, 10, 7, 21, 1, 11, 6, 1, 11, 7, 2, 4, None, 10, None, None, None, 4, 3, 1, None, None, None, 3, 2, None, None, None, 5]}, 
    '3': {'students': 99, 'hour_total': 1397, 'exercise_total': 679, 'hours': [None, 1, 2, 1, 2, 4, 7, 5, 10, 1, 17, 1, 3, 3, 5, 7, 2, 1, 1, None, 8, None, 1, None, 3, 3, 1, None, None, None, 1, None, 1, None, None, 8]}
}

weeks = len(test_dict)

max = 0
for week in test_dict:
    if test_dict[week]["students"] > max:
        max = test_dict[week]["students"]

print(max)

hour = 0
for week in test_dict:
    hour += test_dict[week]["hour_total"]

print(hour)

hours_average = hour//max
print(hours_average)

exercises = 0
for week in test_dict:
    exercises += test_dict[week]["exercise_total"]

print(exercises)

exercises_average = exercises//max
print(exercises_average)

def retrieve_course(course_name: str) -> dict:
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    my_request = urllib.request.urlopen(url)
    data = json.loads(my_request.read())
    
    course_dict = {}
    students, hours, exercises = 0, 0, 0
    for week in data:
        if data[week]["students"] > students:
            students = data[week]["students"]

        hours += data[week]["hour_total"]
        
        exercises += data[week]["exercise_total"]
    
    course_dict['weeks'] = len(data) 
    course_dict['students'] = students
    course_dict["hours"] = hours
    course_dict["hours_average"] = hours // students
    course_dict["exercises"] = exercises
    course_dict["exercises_average"] = exercises //students
    return course_dict


retrieve_course("docker2019")

# Course statistics - Approach 1
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())

    retrieved_list = []
    for i in data:
        if i["enabled"] == True:
            retrieved_tuple = i["fullName"], i["name"], i["year"], sum(i["exercises"])
            retrieved_list.append(retrieved_tuple)

    return retrieved_list

def retrieve_course(course_name: str) -> dict:
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    my_request = urllib.request.urlopen(url)
    data = json.loads(my_request.read())
    
    course_dict = {}
    students, hours, exercises = 0, 0, 0
    for week in data:
        if data[week]["students"] > students:
            students = data[week]["students"]

        hours += data[week]["hour_total"]
        
        exercises += data[week]["exercise_total"]
    
    course_dict['weeks'] = len(data) 
    course_dict['students'] = students
    course_dict["hours"] = hours
    course_dict["hours_average"] = hours // students
    course_dict["exercises"] = exercises
    course_dict["exercises_average"] = exercises //students
    return course_dict

# Course statistics - Approach 2
import urllib.request
import json
 
def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats/api/courses")
    course_data = json.loads(request.read())
    courses = []
    for course in course_data:
        if not course['enabled']:
            continue
 
        exercises = 0
        for exercise in course['exercises']:
            if exercise:
                exercises += exercise
 
        courses.append((course['fullName'], course['name'], course['year'], exercises))
 
    return courses
 
def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats/api/courses/{course_name}/stats")
    course_weeks = json.loads(request.read())
    students = 1
    exercises = 0
    hours = 0 
    for no, week in course_weeks.items():
        if week['students'] > students:
            students = week['students']
        hours += week['hour_total']
        exercises += week['exercise_total']
 
    return {
        "weeks": len(course_weeks),
        "students": students,
        "hours": hours,
        "hours_average": hours//students,
        "exercises": exercises,
        "exercises_average": exercises//students,
    }

# Who cheated - review
# Exercise Files\start_times.csv
# Exercise Files\submissions.csv

# The file 'start_times.csv' contains individual start times for a programming exam, in the format 'name;hh:mm'. 
# An example:
'''
jarmo;09:00
timo;18:42
kalle;13:23
'''

# Additionally, the file 'submissions.csv' contains points and handin times for individual exercises. 
# The format here is 'name;task;points;hh:mm'. An example:
'''
jarmo;1;8;16:05
timo;2;10;21:22
jarmo;2;10;19:15
jne...
'''

# Your task is to find the students who spent over 3 hours on the exam tasks. 
# That is, any student whose any task was handed in over 3 hours later than their exam start time is labelled a cheater. 
# There may be more than one submission for the same task for each student. 
# You may assume all times are within the same day.

# Please write a function named 'cheaters()', which returns a list containing the names of the students who cheated.

import csv
from datetime import datetime, timedelta

def cheaters():
    student_dict = {}
    with open("Exercise Files\start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            cutoff_time = start_time + timedelta(hours=3)
            student_dict[line[0]] = cutoff_time

    cheater_list = []
    with open("Exercise Files\submissions.csv") as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            end_time = datetime.strptime(line[3], "%H:%M")
            if student_dict[line[0]] < end_time and line[0] not in cheater_list:
                cheater_list.append(line[0])

    return cheater_list

# Who cheated - Approach 2
import csv
from datetime import datetime, timedelta
 
def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
            # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time
        
        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
 
        return cheaters
    
# Who cheated - Output Test
    
list1 = ['matti',
 'antti',
 'henrik',
 'arto',
 'esko',
 'kjell',
 'jyrki',
 'teemu',
 'tiina',
 'virpi',
 'liisa',
 'kotivalo',
 'justiina',
 'luukas',
 'johannes']

list2 = ['justiina',
 'esko',
 'tiina',
 'jyrki',
 'teemu',
 'johannes',
 'kjell',
 'luukas',
 'antti',
 'virpi',
 'kotivalo',
 'matti',
 'arto',
 'henrik',
 'liisa']

for element in list2:
    if element in list1:
        print(True)
        
# Who cheated, version 2

# You have the CSV files from the previous exercise at your disposal again. 
# Please write a function named 'final_points()', which returns the final exam points received by the students, in a dictionary format, following these criteria:
    # If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
    # If the submission was made over 3 hours after the start time, the submission is ignored.

# The tasks are numbered 1 to 8, and each submission is graded with 0 to 6 points.
# In the dicionary returned the key should be the name of the student, and the value the total points received by the student.

# Reviews
points_dict = {'student1': {'exercise': 2, 'exercise2': 3, 'exercise3': 4}, 
               "student2": {'exercise': 5, 'exercise2': 4}}

if "exercise3" in points_dict["student2"]:
    print(True)

len(points_dict["student2"])
if points_dict["student3"] == :
    print(True)
else:
    print(False)


# Who cheated, version 2 - Approach 1
import csv
from datetime import datetime, timedelta

def final_points():
    cutoff_dict = {}
    points_dict = {}
    with open("Exercise Files\start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            cutoff_time = start_time + timedelta(hours=3)
            cutoff_dict[line[0]] = cutoff_time
            points_dict[line[0]] = {}

    with open("Exercise Files\submissions.csv") as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            end_time = datetime.strptime(line[3], "%H:%M")
            grade = int(line[2])
            if cutoff_dict[line[0]] >= end_time: 
                if line[1] not in points_dict[line[0]]:
                    points_dict[line[0]][line[1]] = grade
                elif grade > points_dict[line[0]][line[1]]:
                    points_dict[line[0]][line[1]] = grade
                    
    total_point = {}
    for name, exercises in points_dict.items():
        total_point[name] = 0
        for e, score in exercises.items():
            total_point[name] += score
            
    return total_point
    
final_points()

# Who cheated, version 2 - Approach 2
import csv
from datetime import datetime, timedelta
 
def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student time and points is saved to a dictionary
        # Time and points is saved as tuple.
        points = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            tno = int(row[1])
            p = int(row[2])
            time = datetime.strptime(row[3], "%H:%M")
 
            # If cheating has happened, submission is not handled
            if time - start_times[name] > timedelta(hours=3):
                continue
 
            # If student is not handled yet, add student directly to the dictionary
            if name not in points:
                default_time = datetime(1900, 1, 1)
                points[name] = {}
                for i in range(1, 8+1):
                    points[name][i] = 0
                points[name][tno] = p
 
            # If student already exists, more points than earlier is required
            elif p > points[name][tno]:
                points[name][tno] = p
 
        final_points = {}
        # Iterate through students one by one
        for student in points:
            p = 0
            for exercise in points[student]:
                p += points[student][exercise]
            final_points[student] = p
 
        return final_points
    
# Looking for modules
    # Standard Library - https://docs.python.org/3/library/
    # Third-Party Modules - https://wiki.python.org/moin/UsefulModules


# Spell checker, version 2 - Approach 1
# Just like in the previous version, the program should ask the user to type in a line of text. 
# Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. 
# Additionally, the program should print out a list of suggestions for the misspelled words.

# The suggestions should be determined with the function 'get_close_matches' from the Python standard library module 'difflib'.
# https://docs.python.org/3/library/difflib.html#difflib.get_close_matches
# https://docs.python.org/3/library/difflib.html


from difflib import get_close_matches

if False:
    sentence = input("Write text: ")
else:
    sentence = "We use ptython to make a spell checker"

def words():
    wordlist = []
    with open("Exercise Files\words.txt") as wordfile:
        for word in wordfile:
            wordlist.append(word.strip())
    return wordlist

wordlist = words()

marked_sentence = ""
suggestions = {}
for word in sentence.split(" "):
    if word.lower() in wordlist:
        marked_sentence += word + " "
    else:
        marked_sentence += "*" + word + "* "
        suggestions[word] = get_close_matches(word.lower(), wordlist)

print(marked_sentence.strip())
print("suggestions:")
for word, suggestion in suggestions.items():
    print(word + ": "  + ", ".join(suggestions[word]))
    
# Spell checker, version 2 - Approach 2
import difflib 
 
def wordlist():
    words = []
    with open("wordlist.txt") as file:
        for rivi in file:
            words.append(rivi.strip())
    return words
 
words = wordlist()
sentence = input("write text: ")
error = []
for word in sentence.split(' '):
    if word.lower() in words:
        print(word+ " ", end="")
    else:
        error.append(word)
        print("*" + word+ "* ", end="") 
 
print()
 
print("suggestions:")
for word in error:
    suggestion_list = difflib.get_close_matches(word, words)
    suggestions = ", ".join(suggestion_list)
    print(f"{word}: {suggestions}")