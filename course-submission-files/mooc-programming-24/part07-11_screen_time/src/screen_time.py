# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date_string = input("Starting date: ")
num_days = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile): ")

start = datetime.strptime(starting_date_string, "%d.%m.%Y")
start_string = datetime.strftime(start, "%d.%m.%Y")

screen_log = {}
for i in range(num_days):
    string_date = datetime.strftime(start, "%d.%m.%Y")
    line = input(f"Screen time {string_date}:")
    line = list(map(int, line.split(" ")))
    screen_log[string_date] = line
    start += timedelta(days=1)
    
with open(filename, "w") as file:
    file.write(f"Time period: {start_string}-{string_date}\n")
    
    total = 0
    string = ""
    for i, l in screen_log.items():
        string += f"{i}: {l[0]}/{l[1]}/{l[2]}\n"
        total += sum(l)
    
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {total/num_days}\n")
    file.write(string)
    print(f"Data stored in file {filename}")