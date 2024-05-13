# Simple while loop example

while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")

# Example 2
while True:
    code = input("Please type in your PIN: ")
    if code == "1234":
        break
    print("Incorrect...try again")

print("Correct PIN entered!")

# Example 3
while True:
    print("hi")
    response = input("Shall we continue?")
    if response == "no":
        break
print("okay then")

# Input Validation
from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        break
    if number > 0:
        print(sqrt(number))
    else:
        print("Invalid number")
        
print("Exiting...")

# Countdown
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number == 0:
    break

print("Now!")

# Repeat Password
password = input("Password: ")

while True:
    repeat = input("Repeat password: ")
    if password == repeat:
        break
    else:
        print("They do not match!")

print("User account created!")

# Loops with helper variable
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")

# PIN and number of attempts
attempt = 0

while True:
    pin = input("Pin: ")

    attempt += 1

    if pin == "4321":
        break
    else:
        print("Wrong")

if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempt} attempts")

# The next leap year
year = int(input("Year: "))
next = year + 1

while True:
    if next % 100 == 0:
        if next % 400 == 0:
            break
    elif next % 4 == 0:
        break

    next += 1

print(f"The next leap year after {year} is {next}")

# Concatenating strings with the + operator

# Story Example
story = ""
previous = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous:
        break
    story += word + " "
    previous = word
 
print(story)


# Sum, mean, number counter and positives and negatives counter
print("Please type in integer numbers. Type in 0 to finish.")

number = 0
count = 0
sums = 0
positives = 0
negatives = 0

while True:
    number = int(input("Number: "))
    
    if number != 0:
        count += 1
        sums += number
        if number > 0:
            positives += 1
        if number <0:
            negatives += 1
    else:
        break

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sums}")
print(f"The mean of the numbers is {sums/count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")

# Example - Hello Visual Studio Code
while True:
    editor = input("Editor: ").lower()
    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")

# string.lower() method converts the string it is applied on to lowercase entirely