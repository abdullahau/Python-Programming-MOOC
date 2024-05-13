# Create a new, empty List
my_list = []

# List with itme assigned to a variable
my_list = [7, 2, 2, 5, 2]

# Accessing item in a list
my_list = [7, 2, 2, 5, 2]

print(my_list[0])
print(my_list[1])
print(my_list[3])

print("The sum of the first two items:", my_list[0] + my_list[1])

# Printing out a list
my_list = [7, 2, 2, 5, 2]
print(my_list)

# Mutable - Changing the content of the list
my_list = [7, 2, 2, 5, 2]
print(my_list)
my_list[1] = 3
print(my_list)

# Length of a list
my_list = [7, 2, 2, 5, 2]
print(len(my_list))

# Change the value of an item
my_list = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i == -1:
        break
    if i < 0 or i >= len(my_list):
        print("Index is outside of the range of the list")
        continue
    value = int(input("New Value: "))
    my_list[i] = value
    print(my_list)
    
# Adding items to a list
numbers = []
shoe_sizes = []

numbers.append(5)
numbers.append(10)
numbers.append(3)

shoe_sizes.append(37)
shoe_sizes.append(44)
shoe_sizes.append(40)
shoe_sizes.append(28)

print("Numbers:")
print(numbers)

print("Shoe sizes:")
print(shoe_sizes)

# Add items to a list - Approach 1
items = int(input("How many items: "))
my_list = []
i = 0
while i < items:
    item = int(input(f"Item {i+1}: "))
    my_list.append(item)
    i += 1
print(my_list)

# Add items to a list - Approach 2
numbers = int(input("How many items: "))
list = []
 
while len(list) < numbers:
    number = int(input(f"Item {len(list) + 1}: "))
    list.append(number)
 
print(list)

# Adding to a specific location - 'inset' method
# 'inset' method - specify a location in the list where an item should be added
# Method adds an item at the specified index. 
# `inset` method takes two arguments (respectively): index and item. Index is where the item should appear in the updated list, and item is the item that should be placed in the specified index.
# All the items already in the list with an index equal to or higher than the specified index are moved one index further, "to the right"

numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(0, 10)
print(numbers)
numbers.insert(2, 20)
print(numbers)

# Removing items from a list - 'pop' method
# If the index of the item is known, you can use the method 'pop'.
# Method 'pop' takes the index of the item you want to remove as its argument.
# The indexes of the remaining items change when one is removed.
# method 'pop' also returns the removed item.

my_list = [1, 2, 3, 4, 5, 6]

my_list.pop(2)
print(my_list)
my_list.pop(3)
print(my_list)

# 'pop' method return
my_list = [4, 2, 7, 2, 5]

number = my_list.pop(2)
print(number)
print(my_list)

# Removing items from a list - 'remove' method
# If the contents of the item are known, you can use the method remove.
# method 'remove' takes the value of the item to be removed as its argument.
# The method removes the first occurrence of the value in the list, much like the string function 'find' returns the first occurrence of a substring.

my_list = [1, 2, 1, 2]

my_list.remove(1)
print(my_list)
my_list.remove(1)
print(my_list)

# 'remove' method causes an error if the specified item is not in the list
# Just like with strings, we can check for the presence of an item with the 'in' operator
my_list = [1, 3, 4]

if 1 in my_list:
    print("The list contains item 1")

if 2 in my_list:
    print("The list contains item 2")


# Addition and removal - Approach 1
list = []
print(f"The list is now {list}")
i = 0
while True:
    instruction = input("a(d)d, (r)emove or e(x)it: ")
    if instruction == "x":
        print("Bye!")
        break
    elif instruction == "r":
        list.pop(i-1)
        i -= 1
    else:
        list.insert(i, i + 1)
        i += 1
    print(f"The list is now {list}")
    
# Addition and removal - Approach 2
list = []
while True:
    print(f"The list is now {list}")
    selection = input("a(d)d, (r)emove or e(x)it:")
    if selection == "d":
        # Value of item is length of the list + 1
        item = len(list) + 1
        list.append(item)
    elif selection == "r":
        list.pop(len(list) - 1)
    elif selection == "x":
        break
 
print("Bye!")

# Same word twice
list =[]
while True:
    word = input("Word: ")
    if word in list:
        break
    list.append(word)

print(f"You typed in {len(list)} different words")

# Sorting list
# The 'sort' method orders the original list in place in an ascending order
# The 'sorted' function returns an ordered list placed in its arguments but does not alter the original list itself
# The 'sorted' function creates a new, ordered copy of the list

# 'sort' method -> Method alters the original list in place
my_list = [2,5,1,2,4]
my_list.sort()
print(my_list)

# 'sorted' function -> returns a new ordered list
my_list = [2,5,1,2,4]
print(sorted(my_list))

original = [2, 5, 1, 2, 4]
in_order = sorted(original)
print(original)
print(in_order)

# List twice
list = []
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    list.append(item)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")

# List maximum, minimum and sum
# The functions max and min, short for maximum and minimum, return the greatest and smallest item in a list.
# The function sum returns the sum of all items in a list.

my_list = [5, 2, 3, 1, 4]

greatest = max(my_list)
smallest = min(my_list)
list_sum = sum(my_list)

print("Smallest:", smallest)
print("Greatest:", greatest)
print("Sum:", list_sum)

# Method Vs Functions

# Methods are used with a dot '.' operator on the list variable
# Examples of list method
my_list = []

# method calls
my_list.append(3)
my_list.append(1)
my_list.append(7)
my_list.append(2)

# another method call
my_list.sort()

# List functions take in the list as an agrument
# Examples of functions
my_list = [3, 2, 7, 1]

# function calls take the list as an argument
greatest = max(my_list)
smallest = min(my_list)
length = len(my_list)

print("Smallest:", smallest)
print("Greatest:", greatest)
print("Length of the list:", length)

# another function call 
# the list itself is an argument, the function returns a sorted copy
in_order = sorted(my_list)
print(in_order)

# A list as an argument or a return value in a user defined function
# Median value from a list input
def median(my_list: list) -> int: # "my_list: list" indicates that the input should be a list and "-> int" indicates that function will return an intiger or float based on the items within the list 
    ordered = sorted(my_list)
    list_centre = len(ordered) // 2
    return ordered[list_centre]

shoe_sizes = [45, 44, 36, 39, 40]
print("The median of the shoe sizes is", median(shoe_sizes))

ages = [1, 56, 34, 22, 5, 77, 5]
print("The median of the ages is", median(ages))

# Input integers from user and returns a list
def input_numbers():
    numbers = []
    while True:
        user_input = input("Please type in an integer, leave empty to exit: ")
        if len(user_input) == 0:
            break
        numbers.append(int(user_input))
    return numbers

numbers = input_numbers()

print("The greatest number is", max(numbers))
print("The median of the numbers is", median(numbers))

print("Shoe sizes:")
shoe_sizes = input_numbers()

print("Weights:")
weights = input_numbers()

print("Heights:")
heights = input_numbers()

# Implementing above without a user defined function
numbers = []
while True:
    user_input = input("Please type in an integer, leave empty to exit: ")
    if len(user_input) == 0:
        break
    numbers.append(int(user_input))

ordered = sorted(numbers)
list_centre = len(ordered) // 2
median = ordered[list_centre]

print("The greatest number is", max(numbers))
print("The median of the numbers is", median)

# The length of a list
def length(my_list: list) -> int:
    return len(my_list)

my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

result = length([1, 1, 1, 1])
print("The length is", result)

# Arithmetic mean
def mean(my_list: list) -> float:
    return sum(my_list) / len(my_list)

my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print("mean value is", result)

# The range of a list
def range_of_list(my_list: list) -> int:
    return max(my_list) - min(my_list)

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)