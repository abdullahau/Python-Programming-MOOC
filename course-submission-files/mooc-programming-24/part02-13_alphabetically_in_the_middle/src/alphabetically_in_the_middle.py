# Write your solution here

first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first > second:
    if first < third:
        print(f"The letter in the middle is {first}")
    elif second > third:
        print(f"The letter in the middle is {second}")
    else:
        print(f"The letter in the middle is {third}")
elif first < second:
    if first > third:
        print(f"The letter in the middle is {first}")
    elif second < third:
        print(f"The letter in the middle is {second}")
    else:
        print(f"The letter in the middle is {third}")
