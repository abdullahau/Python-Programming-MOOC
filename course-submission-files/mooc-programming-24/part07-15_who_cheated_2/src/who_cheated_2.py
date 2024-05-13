# Write your solution here
import csv
from datetime import datetime, timedelta

def final_points():
    cutoff_dict = {}
    points_dict = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            cutoff_time = start_time + timedelta(hours=3)
            cutoff_dict[line[0]] = cutoff_time
            points_dict[line[0]] = {}

    with open("submissions.csv") as sub_file:
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