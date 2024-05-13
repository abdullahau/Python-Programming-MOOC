# Objects and methods

# if we are trying to store information about a book, it might make sense to use a tuple or a dictionary to organize the data into a single data structure.
# The solution could look like this when using a tuple:

name = "In Search of Lost Typing"
author = "Marcel Pythons"
year = 1992

# Combine these in a tuple
book = (name, author, year)

# Print the name of the book
print(book[0])


# In a case like this, the advantage of using a dictionary is that we can use strings instead of indexes as the keys. 
# That is, we can give descriptive names to the items stored in the data structure:

name = "In Search of Lost Typing"
author = "Marcel Pythons"
year = 1992

# Combine these in a dictionary
book = {"name": name, "author": author, "year": year}

# Print the name of the book
print(book["name"])

# In both cases we are creating a new _object_. 
# In programming, the term has the specific meaning of an independent whole, in this case containing some bits of data which are somehow related. 
# Being independent means that any changes made to one object will not affect other objects.

# If we were to create two structurally identical representations of books, using dictionaries with identical keys, any changes made to one of them would not have any effect on the other:
book1 = {"name": "The Old Man and the Pythons", "author": "Ernest Pythons", "year": 1952}
book2 = {"name": "Seven Pythons", "author": "Aleksis Python", "year": 1894}

print(book1["name"])
print(book2["name"])

book1["name"] = "A Farewell to ARM Processors"

print(book1["name"])
print(book2["name"])

# Objects and methods
# The data stored in an object can be accessed through _methods_. 
# A method is a function which operates on the specific object it is attached to. 
# The way to distinguish methods from other functions is the way in which they are called: first you write the name of the object targeted, followed by a dot, and then the name of the method, with arguments if any.

# For example, the method `values` returns all the values stored in an object of type dictionary, or `dict`:
# this creates an object of type dictionary with the name book
book = {"name": "The Old Man and the Pythons", "author": "Ernest Pythons", "year": 1952}

# Print out all the values
# The method call values() is written after the name of the variable
# Remember the dot notation!
for value in book.values():
    print(value)
    
# Similarly, string methods target the string object which they are called on. 
# Some examples of string methods include `count` and `find`:
name = "Imaginary Irene"

# Print out the number of times the letter I is found
print(name.count("I"))

# The number of letters I found in another string
print("Irreverent Irises in Islington".count("I"))

# The index of the substring Irene
print(name.find("Irene"))

# This string has no such substring
print("A completely different string".find("Irene"))

# String methods return values, but they will not change the contents of a string. 
# As stated above, strings in Python are immutable. 
# This does not apply to all methods, however. 
# Python lists are mutable, so Python list methods may change the contents of the list they are called on:
my_list = [1,2,3]

# Add a couple of items
my_list.append(5)
my_list.append(1)

print(my_list)

# Remove the first item
my_list.pop(0)

print(my_list)

# In Python, every value stored in a variable is a reference to an object, so any value stored in a list is also a reference to an object. 
# This is also true when modelling a matrix data structure: each value in the top level list is a reference to another list, which in turn contains references to the objects representing the elements of the matrix.

# The smallest average result - Approach 1

# Please write a function named `smallest_average(person1: dict, person2: dict, person3: dict)`, which takes three dictionary objects as its arguments.

# Each dictionary object contains values mapped to the following keys:
    # `"name"`: The name of the contestant
    # `"result1"`: the first result of the contestant (an integer between 1 and 10)
    # `"result2"`: the second result of the contestant (as above)
    # `"result3"`: the third result of the contestant (as above)

# The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. 
# The return value should be the entire dictionary object containing the contestant's information.
# You may assume there will be no ties, i.e. a single contestant will have the smallest average result.

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

def smallest_average(person1: dict, person2: dict, person3: dict):
    collection = (person1, person2, person3)
    
    avg_list = []
    for person in collection:
        total = 0
        for i in range(3):
            total += person["result"+str(i+1)]
        avg_list.append(total/3)

    return collection[avg_list.index(min(avg_list))]

# The smallest average result - Approach 2

# Helper function for one average
def average(person: dict):
    ex_sum = person["result1"]+person["result2"]+person["result3"]
    return ex_sum/3
 
def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest = person1
 
    if average(person2) < average(smallest):
        smallest = person2
 
    if average(person3) < average(smallest):
        smallest = person3
 
    return smallest

# Row sums - Approach 1
# Please write a function named row_sums(my_matrix: list), which takes an integer matrix as its argument.
# The function should add a new element on each row in the matrix. 
# This element contains the sum of the other elements on that row. 
# The function does not have a return value. It should modify the parameter matrix in place.


my_matrix = [[1, 2], [3, 4], [4, 5, 6], [7, 8, 9, 10]]

def row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        total = 0
        for num in my_matrix[i]:
            total += num
        my_matrix[i].append(total)
        
row_sums(my_matrix)
print(my_matrix)

# Row sums - Approach 2
def row_sums(matrix: list):
    for row in matrix:
        row.append(sum(row))