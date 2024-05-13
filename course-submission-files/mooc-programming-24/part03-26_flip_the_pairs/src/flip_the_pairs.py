number = int(input("Please type in a number: "))
i = 0
z = 2

while i <= number:
    i += 1
    if z * i >= number:
        break
    print(z * i)
    print(z * i - 1)

print(number)
if number % 2 == 0:
    print(number - 1)