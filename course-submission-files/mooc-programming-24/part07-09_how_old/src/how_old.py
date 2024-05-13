# Write your solution here
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