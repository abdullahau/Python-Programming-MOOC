# Write your solution here

number = int(input("Please type in a number: "))
i = 1

while i <= number:
    z = 1
    while z <= number:
        print(f"{i} x {z} = {i * z}")
        z += 1
    i += 1