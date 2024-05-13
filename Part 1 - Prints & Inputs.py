result = 10 * 25
print("The result is", result)

result = 10 * 25
print(f"The result is {result}")

name = "Mark"
age = 37
city = "Palo Alto"
print(f"Hi {name}, you are {age} years old. You live in {city}.")

# Using f-strings
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print()
print("my skills are")
print(f"    - {skill1} ({level1})")
print(f"    - {skill2} ({level2})")
print(f"    - {skill3} ({level3})")
print()
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")


# Using \n to add newline to the string
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f"    - {skill1} ({level1})")
print(f"    - {skill2} ({level2})")
print(f"    - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# Operations inside f-strings
x = 27
y = 15

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")
# Printing can also be made as follows:
print(x, "/", y, "=", (x / y))

# Skipping a line change with 'end=""' argument in the print command
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)