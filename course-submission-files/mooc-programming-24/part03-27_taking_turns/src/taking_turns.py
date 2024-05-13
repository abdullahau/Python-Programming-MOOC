# Write your solution here
number = int(input("Please type in a number: "))

i = 0
z = number - 1


while z >= number/2:
    print(number - z)
    print(number - i)
    z -= 1
    i += 1

if number % 2 !=0:
    print(number - z)