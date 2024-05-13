# Write your solution here
limit = int(input("Upper limit: "))
base = int(input("Base: "))
power = 0
test = 0

while test <= limit:
    result = base ** power
    print(result)
    power += 1
    test = base ** (power)