# Developing a larger programming project

"""
Rule No. 1 in tackling any programming project is not trying to solve everything at once. 
The program should be built out of smaller sections, such as helper functions. 
You should verify the operation of each part before moving on to the next. 
If you try to handle too much at once, most likely only chaos ensues.

To do this you will need a way of testing your functions outside the main function. 
You can achieve this by defining a main function explicitly, and calling this function from outside any other function in the program. 
A single function call is then easy to comment out for testing. 
The first steps in building the following programming project could look like this:

```
def main():
    points = []
    # your program code goes here

main()
```

Now the helper functions can be tested without running the main function:

```
# helper function for determining the grade based on the amount of points
def grade(points):
    # more code

def main():
    all_points = []
    # your program code goes here

# comment out the main function
#main()

# test the helper function
student_points = 35
result = grade(student_points)
print(result)
```
"""

# Passing data from one function to another
"""
When a program contains multiple functions, the question arises: how do you pass data from one function to another?

The following example asks the user for some integer values. The program then prints out these values and performs an "analysis" on them. 
The program is divided into three separate functions:

```
def input_from_user(how_many: int):
    print(f"Please type in {how_many} numbers:")
    numbers = []

    for i in range(how_many):
        number = int(input(f"Number {i+1}: "))
        numbers.append(number)

    return numbers

def print_result(numbers: list):
    print("The numbers are: ")
    for number in numbers:
        print(number)

def analyze(numbers: list):
    mean = sum(numbers) / len(numbers)
    return f"There are altogether {len(numbers)} numbers, the mean is {mean}, the smallest is {min(numbers)} and the greatest is {max(numbers)}"

# the "main function" using these functions
inputs = input_from_user(5)
print_result(inputs)
analysis_result = analyze(inputs)
print(analysis_result)
```

When the program is executed, it could go like this:

```
Please type in 5 numbers:
Number 1: 10
Number 2: 34
Number 3: -32
Number 4: 99
Number 5: -53
The numbers are:
10
34
-32
99
-53
There are altogether 5 numbers, the mean is 11.6, the smallest is -53 and the greatest is 99
```

The idea here is that the main function "saves" all data processed by the program. In this case all that is needed is the input from the user in the variable inputs.

If the input is needed in a function, it is passed as an argument. This happens with the functions print_result and analyze. 
If the function produces data that is needed elsewhere in the program, the function returns it with the return command, and it is stored in a variable in the main function. 
This happens with the functions input_from_user and analyze.

You could use the global variable inputs from the main function directly in the helper functions. 
We have already covered why that is a bad idea, but here is another explanation. 
If functions are able to change a global variable, unexpected things may start happening in the program, especially when the number of functions grows large.

Passing data into and out of functions is best handled by arguments and return values.

You could also separate the implicit main function in the example above into its own function. 
Then the variable inputs would no longer be a global variable, but instead a local variable within the main function:

```
# your main function goes here
def main():
    inputs = input_from_user(5)
    print_result(inputs)
    analysis_result = analyze(inputs)

    print(analysis_result)

# run the main function
main()
```

"""