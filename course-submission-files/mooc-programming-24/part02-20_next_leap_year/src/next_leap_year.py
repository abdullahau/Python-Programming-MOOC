# Write your solution here

year = int(input("Year: "))
next = year + 1

while True:
    if next % 100 == 0:
        if next % 400 == 0:
            break
    elif next % 4 == 0:
        break

    next += 1

print(f"The next leap year after {year} is {next}")








