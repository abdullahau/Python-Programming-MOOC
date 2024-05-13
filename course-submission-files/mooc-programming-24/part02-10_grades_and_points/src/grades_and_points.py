# Write your solution here

point = int(input("How many points [0-100]: "))

if point > 100 or point < 0:
    grade = "impossible!"
elif point <= 49:
    grade = "fail"
elif point <= 59:
    grade = 1
elif point <= 69:
    grade = 2
elif point <= 79:
    grade = 3
elif point <= 89:
    grade = 4
elif point <= 109:
    grade = 5

print(f"Grade: {grade}")