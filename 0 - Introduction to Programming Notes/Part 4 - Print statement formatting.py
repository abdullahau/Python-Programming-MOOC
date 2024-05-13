# Print statement formatting

# Method 1 - Using '+' to concatenate multiple strings segments
name = "Mark"
age = 37
print("Hi " + name + " your age is " + str(age) + " years" )
# Limitation: all segments must be a string

# Method 2 - Using ',' to concatenate multiple types as seperate arguments
name = "Mark"
age = 37
print("Hi", name, "your age is", age, "years" )

# Removing automatic/default whilespaces between the arguments
name = "Mark"
age = 37
print("Hi", name, "your age is", age, "years", sep="")

# sep="" is a keyword argument and is short for "seperator"

# Adding different seperations (sep=) between arguments
name = "Mark"
age = 37
print("Hi", name, "your age is", age, "years", sep="-")

# Adding newline character seperations between arguments
name = "Mark"
age = 37
print("Hi", name, "your age is", age, "years", sep="\n")

# Removing newline character from the end of the print command
print("Hi ", end="")
print("there!")

# f-string - concatenate multiple types
name = "Erkki"
age = 39
print(f"Hi {name} your age is {age} years")

# f-string - rounding floats
number = 1/3
print(f"The number is {number}")
print(f"The number is {number:.2f}")

# f-string - aligning and whitspaces
names =  [ "Steve", "Jean", "Katherine", "Paul" ]
for name in names:
  print(f"{name:15} centre {name:>15}")
  
# f-string - aligning and whitespaces - Advance

# F-strings differentiate between strings and numbers when it comes to justifying columns:
word = "python"
print(f"{word:10}continues")
print(f"{word:>10}continues")

# As you can see above, by default strings are justified to the left edge of the area specified for them. 
# The '>' symbol can be used to justify to the right edge.

# With number values the logic is reversed:
number = 42
print(f"{number:10}continues")
print(f"{number:<10}continues")

# With numbers the default behaviour is to justify to the right edge. 
# The symbol < can be used to justify to the left edge.

  
# f-string - assigning to variables and combining with other strings
name = "Larry"
age = 48
city = "Palo Alto"
greeting = f"Hi {name}, you are {age} years of age"
print(greeting + f", and you live in {city}")

# f-string is a sort of function, which creates a normal string based on the "arguments" within the curly brackets.

# Integers to strings
def formatted(my_list: list):
    new_list = []
    for i in my_list:
            new_list.append(f"{i:.2f}")
    return new_list

my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)