# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

number = 0
count = 0
sums = 0
positives = 0
negatives = 0

while True:
    number = int(input("Number: "))
    
    if number != 0:
        count += 1
        sums += number
        if number > 0:
            positives += 1
        if number <0:
            negatives += 1
    else:
        break

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sums}")
print(f"The mean of the numbers is {sums/count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")
    