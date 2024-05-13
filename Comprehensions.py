# Basic List Comprehensions

# Standard
values = []
for x in range(10):
    values.append(x)

print(values)

# Using List Comprehensions
values = [x for x in range(10)]
print(values)


# Comprehension Condition

# Get all the even numbers from 0-50
evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)
print(evens)

# Using Comprehensions
evens = [number for number in range(50) if number % 2 == 0]
print(evens)

# Comprehension With Multiple Conditions

# Strings that start with "a" and end in "y"
options = ["any", "albany", "apple", "world", "hello", ""]
valid_string = []

for string in options:
    if len(string) <= 1:
        continue
    if string[0] != "a":
        continue
    if string[-1] != "y":
        continue
    
    valid_string.append(string)

print(valid_string)

# Using Comprehensions
options = ["any", "albany", "apple", "world", "hello", ""]

valid_string = [
    string 
    for string in options 
    if len(string) > 1 
    if string[0] == "a" 
    if string [-1] == "y"
    ]

print(valid_string)

# Multiple List Comprehension

# Flattening a Matrix (list of lists) (2D matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)

# Using Comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print(flattened)

# If/Else In A Comprehension

# Categorize numbers as even or odd
categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

print(categories)

# Using Comprehensions
categories = ["Even" if number % 2 == 0 else "Odd" for number in range(10)]
print(categories)

# Nested List Comprehension

# Bulding a 3D matrix
lst = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    lst.append(l1)

print(lst)

# Using Comprehensions
lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
print(lst)

# Transformation In Comprehension

# list comp with functions
def square(x):
    return x**2

squared_number = [square(x) for x in range(10)]
print(squared_number)

# Dictionary Comprehension

# Creating a dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]

my_dict = {k: v for k, v in pairs}
print(my_dict)

# Set Comprehension

# Removing duplicates from a list while applying a function
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_squared = {x**2 for x in nums} # Builds a 'set' data type. Sets contain only unique values, therefore, duplicates are ignored
print(unique_squared)

# Generator Comprehension

# Sum of Squares

sum_of_squares = sum(num**2 for num in range(1000000))
print(sum_of_squares)

# Range of 1,000,000 and its squares are not stored in memory
# Generator returns value when needed
# Only the previous cumulative sum is stored and with each sequential call from range is added tot he previous sum.

