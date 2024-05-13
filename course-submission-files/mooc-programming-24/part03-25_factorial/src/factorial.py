# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    i = number
    z = 1
    while i >= 1:
        z *= i
        i -= 1
    print(f"The factorial of the number {number} is {z}")

print("Thanks and bye!")