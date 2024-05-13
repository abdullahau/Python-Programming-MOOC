# Write your solution here

year = int(input("Please type in a year: "))

mod4 = year % 4
mod100 = year % 100
mod400 = year % 400

if mod100 == 0:
    if mod400 == 0:
        print("This year is a leap year.")
    else:
        print("That year is not a leap year.")
elif mod4 == 0:
    print("This year is a leap year.")
else:
    print("That year is not a leap year.")