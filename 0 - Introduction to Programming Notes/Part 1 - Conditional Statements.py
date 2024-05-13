#| Operator | Purpose                  | Example  |
#|:--------:|--------------------------|----------|
#| `==`     | Equal to                 | `a == b` |
#| `!=`     | Not equal to             | `a != b` |
#| `>`      | Greater than             | `a > b`  |
#| `>=`     | Greater than or equal to | `a >= b` |
#| `<`      | Less than                | `a < b`  |
#| `<=`     | Less than or equal to    | `a <= b` |

# Example 1
number = int(input("Please type in a number: "))
absolute_value = number
if number < 0:
    absolute_value = number * -1
print("The absolute value of this number is", absolute_value)

number = int(input("Please type in a number: "))
if number < 0:
    print(f"The absolute value of this number is {number * -1}")
if number >= 0:
    print(f"The absolute value of this number is {number}")
    
# Example 2
number = int(input("Please type in a number: "))

if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
print("Thank you!")

# Boolean Expression & Boolean Value
a = 3
condition = a < 5
print(condition)
if condition:
    print("a is less than 5")

# Example 3
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{n1} + {n2} = {n1 + n2}")
if operation == "multiply":
    print(f"{n1} * {n2} = {n1 * n2}")
if operation == "subtract":
    print(f"{n1} - {n2} = {n1 - n2}")
    
    
# Fahrenheit to Celsius
fahrenheit = float(input("Please type in a temperature (F): "))
celsius = (fahrenheit - 32)/1.8

print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")

# Hourly Rate
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
weekday = input("Day of the week: ")
 
if weekday == "Sunday":
    # The salary is double on Sundays
    hourly_wage *= 2
 
total_wage = hourly_wage * hours_worked
print(f"Daily wages: {total_wage} euros")

# Example 4
points = int(input("How many points are on your card? "))
if points < 100:
    bonus_rate = 1.1
    print("Your bonus is 10 %")

if points >= 100:
    bonus_rate = 1.15
    print("Your bonus is 15 %")

# a *= b is the same thing as a = a * b
points *= bonus_rate 
print("You now have", points, "points")

# Example 5
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")

if temp <= 20:
    print("I recommend a jumper as well")
    
if temp <= 10:
    print("Take a jacket with you")

if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")   

# Quadratic Equation of the form ax²+bx+c - Compute the 2 real roots
# x = (-b ± sqrt(b²-4ac))/(2a)
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(f"The roots are {r1} and {r2}")