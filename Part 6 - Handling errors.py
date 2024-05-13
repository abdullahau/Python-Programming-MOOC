# Handling errors

# Two basic categories of errors
# 1) Syntax errors, which prevent the execution of the program
# 2) Runtime errors, which halt the execution

# Input Validation
# missing or empty input values in mandatory fields, such as empty strings when the length of the string is critical
# negative values where only positive values are accepted, such as -15 as the amount of an ingredient in a recipe
# missing files or typos in filenames
# values that are too small or too large, for example when working with dates and times
# invalid indexes, such as trying to access index 3 in the string "hey"
# values of a wrong type, such as strings when integers are expected 

age = int(input("Please type in your age: "))
if age >= 0 and age <= 150:
    print("That is a fine age")
else:
    print("This is not a valid age")
    
# As long as the user types in an integer value, our input validation seems to work fine. But what if they type in a string?
'''
Please type in your age: twenty-three
ValueError: invalid literal for int() with base 10: 'twenty-three'
'''

# Exceptions
# Errors that occur while the program is already running are called exceptions.
# Exception handling in Python is accomplished with 'try' and 'except' statements. 
# The idea is that if something within a 'try' block causes an exception, Python checks if there is a corresponding 'except' block. 
# If such a block exists, it is executed and the program then continues as if nothing happened.

# Example of 'ValueError'
try:
    age = int(input("Please type in your age: "))
except ValueError:
    age = -1

if age >= 0 and age <= 150:
    print("That is a fine age")
else:
    print("This is not a valid age")

'''
Please type in your age: twenty-three
This is not a valid age
'''

# In the above example we covered only a 'ValueError' exception. 
# If the exception had some other cause, the execution would still have halted, despite the 'try' and 'except' blocks.

# In the following example we have a function 'read_integer', which asks the user to type in an integer value, but the function is also prepared for invalid input. 
# The function keeps asking for integers until the user types in a valid input value.

def read_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            return int(input_str)
        except ValueError:
            print("This input is invalid")

number = read_integer()
print("Thank you!")
print(number, "to the power of three is", number**3)

'''
Please type in an integer: three
This input is invalid
Please type in an integer: aybabtu
This input is invalid
Please type in an integer: 5
Thank you!
5 to the power of three is 125
'''

# Sometimes it is enough to catch exceptions with a 'try-except' structure, without doing anything about them. 
# That is, we can just ignore the situation in the 'except' block.

def read_small_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            number = int(input_str)
            if number < 100:
                return number
        except ValueError:
            pass # this command doesn't actually do anything

        print("This input is invalid")

number = read_small_integer()
print(number, "to the power of three is", number**3)

'''
Please type in an integer: three
This input is invalid
Please type in an integer: 1000
This input is invalid
Please type in an integer: 5
Thank you!
5 to the power of three is 125
'''

# Now the 'except' block only contains the command 'pass', which doesn't do anything. 
# Python does not allow empty blocks, so the command is necessary.

# Reading input - Approach 1
def read_input(input_string: str, lower_bound: int, upper_bound: int):
    while True:
        try:
            number = int(input(input_string))
            if number > lower_bound and number < upper_bound:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_bound} and {upper_bound}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print(f"You typed in: {number}")

# Reading input - Approach 2
def read_input(prompt: str, lower_limit: int, upper_limit: int):
    while True:
        error = False
        try:
            number = int(input(prompt))
            if number < lower_limit or number > upper_limit:
                error = True
        except:
            error = True
        if error:
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")
        else:
            return number

# Typical Errors
# NameError
# This error is raised when the program attempts to access or use a variable that has not been defined or assigned a value. 
# This can happen if the variable is spelled incorrectly, or if it is accessed before it has been defined.

# ValueError
# This error is often thrown when the argument passed to a function is somehow invalid. 
# For example, the function call float("1,23")causes an error, because decimals are always separated by a point in Python, and here we have a comma.

# TypeError
# This error occurs when a value is of the wrong type. 
# For example, the function call len(10) causes a TypeError, because the function len requires a value whose length can be calculated, such as a string or a list.

# IndexError
# This common error occurs when trying to refer to an index which doesn't exist. 
# For example, the expression "abc"[5] causes an IndexError, because the string in question has no index 5.

# ZeroDivisionError
# As the name implies, this error is thrown when trying to divide by zero, which we know from mathematics to always be a bad idea. 
# For example, if we try to determine the arithmetic mean of values in a list with the formula sum(my_list) / len(my_list), but our list has length zero, this error will occur.

# Exceptions in file handling
# Some common errors when working with files are 'FileNotFoundError' (when trying to access a file which doesn't exist), 
# 'io.UnsupportedOperation' (when trying to perform an operation on a file which is not supported by the mode in which the file is opened) or 
# 'PermissionError' (the program lacks necessary permissions to access the file).

# Handling multiple exceptions at once
# There may be more than one 'except' block attached to each 'try' block. 
# For example, the following program can handle both a 'FileNotFoundException' and a 'PermissionError':
try:
    with open("example.txt") as my_file:
        for line in my_file:
            print(line)
except FileNotFoundError:
    print("The file example.txt was not found")
except PermissionError:
    print("No permission to access the file example.txt")

# Sometimes it is not necessary to specify the error the program prepares for. 
# Especially when dealing with files, it is often enough to know that an error has occurred, and safely exit the program. 
# It is not always necessary to know why the error occurred. If we need to cover for all possible exceptions, we can use the except block without specifying the error:

try:
    with open("example.txt") as my_file:
        for line in my_file:
            print(line)
except:
    print("There was an error when reading the file.")

# NB: the except statement here covers all possible errors, even those caused by the programming mistakes. 
# Only syntax errors will not be caught by this, as they prevent the code from being executed in the first place.

# For example, the following program will always throw an error (NameError), because the variable name 'my_file' is written as 'myfile' on the third line.
try:
    with open("example.txt") as my_file:
        for line in myfile:
            print(line)
except:
    print("There was an error when reading the file.")

# An except block can hide the actual error: the problem here was not caused by file handling as such, but by the variable name which was misspelled. 
# Without the except block the error thrown would be shown, and the cause could be found more easily. 
# Therefore it is usually a good idea to use only except blocks specifically declared for certain error types.

# Passing exceptions
# If executing a function causes an exception, and this exception is not handled, it is passed on to the section of code which called the function, and so forth up the call chain, until it reaches the main function level. 
# If it is not handled there, either, the execution of the program halts, and the exception is usually printed out for the user to see.

# In the following example we have the function testing. If it causes an exception, this is not handled within the function itself, but in the main function:
def testing(x):
    print(int(x) + 1)

try:
    number = input("Please type in a number: ")
    testing(number)
except:
    print("Something went wrong")

'''
Please type in a number: three
Something went wrong
'''

# Raising Exceptions
# We can purposefully raise exceptions and cause errors, with the command 'raise'.

# It can sometimes be a good idea to raise an error when detecting invalid parameters. 
# Especially if we are writing a function which is executed from elsewhere, just printing something out can go unnoticed when the function is called. 
# Raising an error can make debugging easier.

# In the following example we have a function which calculates factorials (for example, the factorial of the number 5 is 1 * 2 * 3 * 4 * 5). 
# If the argument passed to the function is negative, the function raises an error:
def factorial(n):
    if n < 0:
        raise ValueError("The input was negative: " + str(n))
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k

print(factorial(3))
print(factorial(6))
print(factorial(-1))

# If invalid parameters were not detected and the subsequent ValueError was not raised, the function would incorrectly return "1". 
def factorial(n):
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k

print(factorial(3))
print(factorial(6))
print(factorial(-5))

# Parameter validation
def new_person(name: str, age: int):
    if name == "" or len(name) > 40 or name.find(" ") == -1 or age < 0 or age > 150:
        return error_function(name, age)
    return (name, age)


def error_function(name: str, age: int):
    if name == "":
        raise ValueError("name is an empty string")
    if len(name) > 40:
        raise ValueError("name is longer than 40 characters")
    if name.find(" ") == -1:
        raise ValueError("name contains less than two words")
    if age < 0:
        raise ValueError("age is a negative number")
    if age > 150:
        raise ValueError("age is greater than 150")

new_person("Abdullah Mahmood", 29)

# Parameter validation - Approach 2
def new_person(name: str, age: int):
    # Validate name
    if name == "" or (" " not in name) or len(name) > 40:
        raise ValueError("Invalid argument value for name: " + name)
 
    # Validate age
    if age < 0 or age > 150:
        raise ValueError("Invalid argument value for age:" + str(age))
 
    # Both ok
    return (name, age)

# Incorrect lottery numbers - Approach 1
def week_error(week_lable):
    try:
        if week_lable[0:5] == "week " and int(week_lable[5:]) > 0:
            return True
    except ValueError:
        return False

def number_error(lottery_numbers):
    lottery_numbers = lottery_numbers.split(",")
    if len(lottery_numbers) == 7:
        number_list = []
        for number in lottery_numbers:
                try:
                    if int(number) >= 1 and int(number) <= 39 and number not in number_list:
                        number_list.append(number)
                    else:
                        return False
                except ValueError:
                    return False
        if len(number_list) == 7:
            return True
    else:
        return False

def filter_incorrect():
    with open("Exercise Files\lottery_numbers.csv") as main, open("Exercise Files\correct_numbers.csv", "w") as correct:
        for line in main:
            line = line.strip()
            parts = line.split(";")
            if week_error(parts[0]) and number_error(parts[1]):
                correct.write(line + "\n")
        
filter_incorrect()

# Incorrect lottery numbers - Approach 2
def filter_incorrect():
    with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
        for row in input_file:
            parts = row.strip().split(";")
            if len(parts) != 2:
                continue
            week = parts[0].split(" ")
            error = False
            if len(week) != 2 or week[0] != "week":
                error = True
            try:
                mika = int(week[1])
            except:
                error = True
            number_list = parts[1].split(",")
            if len(number_list) != 7:
                error = True
 
            # numbers already listed --> to find out duplicates
            listed = []
            for item in number_list:
                try:
                    number = int(item)
                    if number < 1 or number > 39 or number in listed:
                        error = True
                    listed.append(number)
                except:
                    error = True
            if not error:
                result_file.write(row)