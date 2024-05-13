# Write your solution here
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{n1} + {n2} = {n1 + n2}")
if operation == "multiply":
    print(f"{n1} * {n2} = {n1 * n2}")
if operation == "subtract":
    print(f"{n1} - {n2} = {n1 - n2}")