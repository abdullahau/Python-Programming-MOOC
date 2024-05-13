from math import sqrt
# Write your solution here
while True:
    number = int(input("Please type in a number"))
    if number > 0:
        print(sqrt(number))
    elif number < 0:
        print("Invalid number")
    else:
        break
print("Exiting...")