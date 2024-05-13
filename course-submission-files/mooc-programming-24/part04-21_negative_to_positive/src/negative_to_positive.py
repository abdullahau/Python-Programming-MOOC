# Write your solution here
number = int(input("Please type in a positive integer: "))
for i in range(-number, number + 1):
    if i == 0:
        continue
    print(i)