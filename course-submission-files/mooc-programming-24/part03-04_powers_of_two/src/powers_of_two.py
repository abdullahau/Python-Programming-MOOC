# Write your solution here

limit = int(input("Upper limit: "))
power = 0
test = 0

while test <= limit:
    result = 2 ** power
    print(result)
    power += 1
    test = 2 ** (power)