#| a     | b     | a and b | a or b |
#| ----- | ----- | ------- | ------ |
#| False | False | False   | False  |
#| True  | False | False   | True   |
#| False | True  | False   | True   |
#| True  | True  | True    | True   |

#| a     | not a |
#| ----- | ----- |
#| True  | False |
#| False | True  |

# Python allows for a simplified way of expressing 'x >= a and x <= b'  as 'a <= x <= b'

# Example 1
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f" {greatest} is the greatest of the numbers.")

# Example 2
name = input("Please type in your name: ")

if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")
    
#| points | grade       |
#| ------ | ----------- |
#| < 0    | impossible! |
#| 0-49   | fail        |
#| 50-59  | 1           |
#| 60-69  | 2           |
#| 70-79  | 3           |
#| 80-89  | 4           |
#| 90-100 | 5           |
#| \> 100 | impossible! |

# Example 3
point = int(input("How many points [0-100]: "))

if point > 100 or point < 0:
    grade = "impossible!"
elif point <= 49:
    grade = "fail"
elif point <= 59:
    grade = 1
elif point <= 69:
    grade = 2
elif point <= 79:
    grade = 3
elif point <= 89:
    grade = 4
elif point <= 109:
    grade = 5

print(f"Grade: {grade}")

# Example 4
number = int(input("Number: "))

mod3 = number % 3
mod5 = number % 5

if mod3 == 0 and mod5 ==0:
    print("FizzBuzz")
elif mod3 == 0:
    print("Fizz")
elif mod5 == 0:
    print("Buzz")

# If-Statement Leap Year
year = int(input("Please type in a year: "))
 
# First, we make assumption that a year is not a leap year
leap_year = False
 
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True
 
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# Alphabetically in the middle - 1
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first > second:
    if first < third:
        print(f"The letter in the middle is {first}")
    elif second > third:
        print(f"The letter in the middle is {second}")
    else:
        print(f"The letter in the middle is {third}")
elif first < second:
    if first > third:
        print(f"The letter in the middle is {first}")
    elif second < third:
        print(f"The letter in the middle is {second}")
    else:
        print(f"The letter in the middle is {third}")
        
# Alphabetically in the middle - 2
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
 
if letter1 > letter2 and letter1 > letter3:
    if letter2 > letter3:
        middle = letter2
    else:
        middle = letter3
elif letter2 > letter3:
    if letter3 > letter1:
        middle = letter3
    else:
        middle = letter1
else:
    if letter2 > letter1:
        middle = letter2
    else:
        middle = letter1
 
print("The letter in the middle is " + middle)

# Tax Slabs - Gift Tax Calculator

#| Value of gift       | Tax at the lower limit | Tax rate for the exceeding part (%) |
#| ------------------- | ---------------------- | ----------------------------------- |
#| 5 000 — 25 000      | 100                    | 8                                   |
#| 25 000 — 55 000     | 1 700                  | 10                                  |
#| 55 000 — 200 000    | 4 700                  | 12                                  |
#| 200 000 — 1 000 000 | 22 100                 | 15                                  |
#| 1 000 000 —         | 142 100                | 17                                  |

gift = int(input("Value of gift: "))

if gift >= 1000000:
    tax = 142100 + (gift - 1000000) * 0.17
elif gift >= 200000:
    tax = 22100 + (gift - 200000) * 0.15
elif gift >= 55000:
    tax = 4700 + (gift - 55000) * 0.12
elif gift >= 25000:
    tax = 1700 + (gift - 25000) * 0.10
elif gift >= 5000:
    tax = 100 + (gift - 5000) * 0.08
else:
    tax = 0

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")
    
# Implementation 2:

value = int(input("Value of gift: "))
 
if value < 5000:
    tax = 0
elif value <= 25000:
    tax = 100 + (value - 5000) * 0.08
elif value <= 55000:
    tax = 1700 + (value - 25000) * 0.10
elif value <= 200000:
    tax = 4700 + (value - 55000) * 0.12
elif value <= 1000000:
    tax = 22100 + (value - 200000) * 0.15
else:
    tax = 142100 + (value - 1000000) * 0.17
 
if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")