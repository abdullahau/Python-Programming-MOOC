# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    student_dict = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            cutoff_time = start_time + timedelta(hours=3)
            student_dict[line[0]] = cutoff_time

    cheater_list = []
    with open("submissions.csv") as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            end_time = datetime.strptime(line[3], "%H:%M")
            if student_dict[line[0]] < end_time and line[0] not in cheater_list:
                cheater_list.append(line[0])

    return cheater_list