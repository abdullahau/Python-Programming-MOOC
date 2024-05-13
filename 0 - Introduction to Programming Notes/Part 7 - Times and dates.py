# Times and dates

# 'datetime' module consists of the following types:
# 'date', 'time', 'datetime', 'timedelta', 'tzinfo', 'timezone' 

# The Python 'datetime' module includes the function 'now', which returns a datetime object containing the current date and time. 
# https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime
# https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.now

# The default printout of a datetime object looks like this:
from datetime import datetime

my_time = datetime.now()
print(my_time)

# Datetime object
type(my_time)

my_time
# datetime.datetime(2024, 4, 18, 16, 49, 7, 194227)

# You can also define the object yourself:
from datetime import datetime

my_time = datetime(2024, 4, 12)
print(my_time)

# By default, the time is set to midnight, as we did not give a time of day in the example above.

# Different elements of the datetime object can be accessed in the following manner:
from datetime import datetime

my_time = datetime(1952, 12, 24)
print("Day:", my_time.day)
print("Month:", my_time.month)
print("Year:", my_time.year)

# A time of day can also be specified. The precision can vary, as you can see below:
from datetime import datetime

pv1 = datetime(2021, 6, 30, 13)     # 30.6.2021 at 1PM
print(pv1)
pv2 = datetime(2021, 6, 30, 18, 45) # 30.6.2021 at 6.45PM
print(pv2)

# Compare times and calculate differences between them

# The familiar comparison operators work also on datetime objects:
from datetime import datetime

time_now = datetime.now()
midsummer = datetime(2024, 6, 26)

if time_now < midsummer:
    print("It is not yet Midsummer")
elif time_now == midsummer:
    print("Happy Midsummer!")
elif time_now > midsummer:
    print("It is past Midsummer")

# The difference between two datetime objects can be calculated simply with the subtraction operator:
from datetime import datetime

time_now = datetime.now()
midsummer = datetime(2024, 6, 26)

difference = midsummer - time_now
print("Midsummer is", difference.days, "days away")

# The result of the datetime subtraction is a 'timedelta' object.
type(difference)

# NB: The 'timedelta' object is less versatile than the 'datetime' object. 
# For instance, you can access the number of days in a 'timedelta' object, 
# but not the number of years, as the length of a year varies. 
# A 'timedelta' object contains the attributes 'days', 'seconds' and 'microseconds'. 
# Other measures can be passed as arguments, but they will be converted internally.

# Similarly, addition is available between 'datetime' and 'timedelta' objects. 
# The result will be the 'datetime' produced when the specified number of days (or weeks, seconds, etc) is added to a 'datetime' object:
from datetime import datetime, timedelta
midsummer = datetime(2024, 6, 26)

one_week = timedelta(days=7)
week_from_date = midsummer + one_week

print("A week after Midsummer it will be", week_from_date)

long_time = timedelta(weeks=32, days=15)

print("32 weeks and 15 days after Midsummer it will be", midsummer + long_time)

type(one_week)
print(one_week)

# Let's see how a higher precision works:
from datetime import datetime
time_now = datetime.now()
midnight = datetime(2024, 6, 30)
difference = midnight - time_now
print(f"Midnight is still {difference.seconds} seconds away")

# How old
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthdate = datetime(year, month, day)
millennium_eve = datetime(1999, 12, 31)

dayold = millennium_eve - birthdate

if birthdate < millennium_eve:
    print(f"You were {dayold.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
    
# Valid PIC? - Review

# In this exercise you will validate Finnish Personal Identity Codes (PIC).
# Write a function named 'is_it_valid(pic: str)', which returns 'True' or 'False' based on whether the PIC given as an argument is valid or not. 
# Finnish PICs follow the format 'ddmmyyXyyyz', where 'ddmmyy' contains the date of birth, 'X' is the marker for century, 
# 'yyy' is the personal identifier and 'z' is a control character.

# The program should check the validity by these three criteria:
    # The first half of the code is a valid, existing date in the format ddmmyy.
    # The century marker is either + (1800s), - (1900s) or A (2000s).
    # The control character is valid.

# The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31, 
# and selecting the character at the index specified by the remainder from the string '0123456789ABCDEFHJKLMNPRSTUVWXY'. 
# For example, if the remainder was 12, the control character would be 'C'.

# Valid PICs:
# 230827-906F
# 120488+246L
# 310823A9877

# ddmmyy[yyy] -> mod(nine-digit number, 31) -> index of string to return control character.

len("ddmmyyX")
test = "ddmmyyX"
test[0:7]

len("ddmmyyXyyyz")

pic = "120488+246L"

# Valid PIC? - Approach 1

from datetime import datetime

def is_it_valid(pic: str) -> bool:
    
    # check length is 11
    if len(pic) != 11:
        return False
    
    # check dates & personal identifers are ints 
    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year_short = int(pic[4:6])
        identifier = int(pic[7:10])
    except ValueError:
        return False
    
    # check date ints form valid datetime format
    if pic[6] == "+":
        year_century = 1800
    elif pic[6] == "-":
        year_century = 1900
    elif pic[6] == "A":
        year_century = 2000
    else:
        return False
    
    try:
        birthdate = datetime(year_century + year_short, month, day)
    except ValueError:
        return False
    
    # check control character is valid 
    reference = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    num = int((f"{pic[0:2]}{pic[2:4]}{pic[4:6]}{pic[7:10]}"))
    index = num % 31
    if reference[index] == pic[10]:
        return True
    else:
        return False

test_string = ["230827-906F", "120488+246L", "310823A9877"]

for i in test_string:
    print(is_it_valid(i))


# Valid PIC? - Approach 2
from datetime import datetime
 
def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    numbers = pic[:6]+pic[7:10]
    for x in numbers:
        if x not in "0123456789":
            return False
    century_marker = pic[6]
    if century_marker not in "+-A":
        return False
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    if century_marker == "+":
        year += 1800
    if century_marker == "-":
        year += 1900
    if century_marker == "A":
        year += 2000
    try:
        test = datetime(year, month, day)
    except:
        return False
    characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    index = int(numbers)%31
    return characters[index] == pic[-1]

# Formatting times and dates

# The datetime module contains a method 'strftime' for formatting the string representation of a datetime object.

# For example, the following code will print the current date in the format 'dd.mm.yyyy' and 'dd/mm/yyyy HH:MM', and then the date and time in a different format:
from datetime import datetime

my_time = datetime.now()
print(my_time.strftime("%d.%m.%Y"))
print(my_time.strftime("%d/%m/%Y %H:%M"))

# Time formatting uses specific characters to signify specific formats. 
# The following is a list of a few of them:
# Complete list: https://docs.python.org/3/library/time.html#time.strftime

#| Notation | Significance            |
#| -------- | ----------------------- |
#| `%d`     | day (01–31)             |
#| `%m`     | month (01–12)           |
#| `%Y`     | year in 4 digit format  |
#| `%H`     | hours in 24 hour format |
#| `%M`     | minutes (00–59)         |
#| `%S`     | seconds (00–59)         |

# You can also specify the delimiter between the different elements, as seen in the examples above.

# Datetime formatting works in the reverse direction as well, in case you need to parse a datetime object from a string given by the user. 
# The method 'strptime' will do just that:
from datetime import datetime

birthday = input("Please type in your birthday in the format dd.mm.yyyy: ")
my_time = datetime.strptime(birthday, "%d.%m.%Y")

if my_time < datetime(2000, 1, 1):
    print("You were born in the previous millennium")
else:
    print("You were born during this millennium")

# Screen Time - Approach 1

# Please write a program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a specific period of time.
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

# Screen Time - Approach 2
from datetime import datetime, timedelta
 
week = timedelta(days=7)
 
def format(aika):
    return aika.strftime("%d.%m.%Y")
 
file = input("Filename: ")
start = input("Starting date: ").split('.')
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
screen_times = []
total = 0
start = datetime(int(start[2]), int(start[1]), int(start[0]))
 
for i in range(days):
    day = start + timedelta(days=i)
    times = input(f"Screen time {format(day)}: ").split(' ')
    tv = int(times[0])
    pc = int(times[1])
    mobile = int(times[2])
    total += tv + pc + mobile
    screen_times.append((day, tv, pc, mobile) )
 
with open(file, "w") as tdsto:
    tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    tdsto.write(f"Total minutes: {total}\n")
    tdsto.write(f"Average minutes: {total/days:.1f}\n")
    for pv, tv, pc, mob in screen_times:
        tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
 
print(f"Data stored in file {file}")
        