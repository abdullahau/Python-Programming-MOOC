# More Python features

# Single line conditionals

# The following two statements produce the exact same results:
if x%2 == 0:
    print("even")
else:
    print("odd")

# Ternary operator
print("even" if x%2 == 0 else "odd")

# In the latter example we have a conditional expression on a single line: 'a if [condition] else b'. 
# The value of this expression evaluates to 'a' if the condition is true, and 'b' if it is false. 
# This structure is sometimes referred to as a ternary operator.

# Conditional expressions can be very useful when you need to assign something conditionally. 
# For example, if you had the variables 'x' and 'y', and you wanted to either increment or set 
# the value of 'y' depending on the parity of 'x', you could write it in a normal 'if else' statement, like so:
if x%2 == 0:
    y += 1
else:
    y = 0
    
# The same could be achieved with a nifty one-liner:
y = y + 1 if x%2 == 0 else 0

# An "empty" block

# You are not allowed to have an empty block in a Python program. 
# If you need to have a block of code which does nothing, for example when testing some other functionality, the 'pass' command will let you do this.
def testing():
    pass

# Loops with 'else' blocks
# In Python, loops can have 'else' blocks, too. 
# This section of code is executed if the loop finishes normally. 

# For example, in the following example we are looking through a list of numbers. 
# If there is an even number on the list, the program prints out a message and the loop is broken. 
# If there are no even numbers, the loop finishes normally, but a different message is then printed out.

my_list = [3,5,2,8,1]
for x in my_list:
    if x%2 == 0:
        print("found an even number", x)
        break
else:
    print("there were no even numbers")
    
# A more traditional way to achieve this would be to use a helper variable to remember whether the desired item was found:
my_list = [3,5,2,8,1]
found = False
for x in my_list:
    if x%2 == 0:
        print("found an even number", x)
        found = True
        break
if not found:
    print("there were no even numbers")
    
# Using a 'for else' statement saves us the trouble of writing a separate variable.

# Default parameter value
# A Python function can have a default parameter value. 
# It is used whenever no argument is passed to the function. See the following example:
def say_hello(name="Emily"):
    print("Hi there,", name)

say_hello()
say_hello("Eric")
say_hello("Matthew")
say_hello("")

# NB: an empty string is still a string, so the default parameter is not used if an empty string is passed to the function.

# A variable number of parameters

# You can also define a function with a variable number of parameters, by adding a star before the parameter name. 
# All the remaining arguments passed to the function are contained in a tuple, and can be accessed through the named parameter.

# The following function counts the number and sum of its arguments:
def testing(*my_args):
    print("You passed", len(my_args), "arguments")
    print("The sum of the arguments is", sum(my_args))
    print(type(my_args))

testing(1, 2, 3, 4, 5)

# Your own programming language - Review

# In this exercise you will write your own programming language executor. 

# The programs will consist of rows, and each row will be in one of the following formats:
    # 'PRINT [value]': prints the value
    # 'MOV [variable] [value]': assigns the value to the variable
    # "ADD [variable] [value]": adds the value to the variable
    # 'SUB [variable] [value]': subtracts the value from the variable
    # 'MUL [variable] [value]': multiplies the variable by the value
    # '[location]:': names a line of code, so it can be jumped to from elsewhere
    # "JUMP [location]": jumps to the location specified
    # 'IF [condition] JUMP [location]': if the condition is true, jump to the location specified
    # 'END': finish execution
    
# The program is executed line by line from the first line onwards. 
# The execution ends when the executor comes across the command `END`, or when there are no more lines to execute.

# Each program has 26 pre-defined variables, named `A` to `Z`. Each variable has the value 0 when the program begins. 
# The notation `[variable]` refers to one of these 26 variables.

# All the values processed by the program are integer numbers. The notation `[value]` refers either to a value stored in a variable, or an integer number typed in directly.

# The notation `[location]` refers to any name of a location which consists of lowercase letters `a` to `z` and/or numbers `0` to `9`. Two different locations may not have the same name.

# The notation `[condition]` refers to any expression in the format `[value] [comparison] [value]`, where `[comparison]` is one of the following operators: `==`, `!=`, `<`, `<=`, `>` and `>=`.

# Please write a function named `run(program)`, which takes a list containing the program commands as its argument. 
# Each item on the list is a line of code in the program. The function should return a new list, which contains the results of the `PRINT` commands executed during the program's run.

# You may assume the function will only be given programs which are entirely in the correct format. 
# You do not have to implement any input validation or error handling.

from string import ascii_uppercase
import operator

variables = {}
for i in ascii_uppercase:
    variables[i] = 0
    
print(variables)

variables = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

ops = {"ADD": operator.add, "SUB": operator.sub, "MUL": operator.mul}

ifs = {"==": operator.eq, "!=": operator.ne, "<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge}

program = ["MOV A 1", 
           "MOV B 2",
           "PRINT A",
           "PRINT B",
           "ADD A B",
           "PRINT A",
           "END"]


program = ["MOV A 1",
            "MOV B 10",
            "begin:",
            "IF A >= B JUMP quit",
            "PRINT A",
            "PRINT B",
            "ADD A 1",
            "SUB B 1",
            "JUMP begin",
            "quit:",
            "END"]


program = ["MOV A 1",
            "MOV B 1",
            "begin:",
            "PRINT A",
            "ADD B 1",
            "MUL A B",
            "IF B <= 10 JUMP begin",
            "END"]


program = ["MOV A 2", 
           "MOV B 7",
           "PRINT A",
           "PRINT B",
           "MUL B 5",
           "PRINT A",
           "PRINT B",
           "END"]

program = ["MOV A 3", "PRINT A"]

program = ["MOV N 50",
            "PRINT 2",
            "MOV A 3",
            "begin:",
            "MOV B 2",
            "MOV Z 0",
            "test:",
            "MOV C B",
            "new:",
            "IF C == A JUMP error",
            "IF C > A JUMP over",
            "ADD C B",
            "JUMP new",
            "error:",
            "MOV Z 1",
            "JUMP over2",
            "over:",
            "ADD B 1",
            "IF B < A JUMP test",
            "over2:",
            "IF Z == 1 JUMP over3",
            "PRINT A",
            "over3:",
            "ADD A 1",
            "IF A <= N JUMP begin"]

output = []
k = 0
whileloop = True
while True:
    for i in program[k:]:
        whileloop = False
        part = i.split(" ")
        
        if part[0] == "MOV":
            variables[part[1]] = int(part[2]) if part[2] not in variables else variables[part[2]]
            
        elif part[0] in ops:
            if part[2] not in variables:
                variables[part[1]] = ops[part[0]](variables[part[1]], int(part[2]))
            else:
                variables[part[1]] = ops[part[0]](variables[part[1]], variables[part[2]])
        
        elif part[0] == "IF":
            if part[3] not in variables:
                condition = ifs[part[2]](variables[part[1]],int(part[3]))
            else:
                condition = ifs[part[2]](variables[part[1]],variables[part[3]])

            if condition:
                k = program.index(part[5]+":")
                break
            elif i == program[-1]: 
                whileloop = True
                break
            else:
                continue       
        
        elif part[0] == "PRINT":
            output.append(int(part[1])) if part[1] not in variables else output.append(variables[part[1]])
                
        elif part[0] == "JUMP":
            k = program.index(part[1]+":")
            break
        
        if part[0] == "END" or i == program[-1]:
            whileloop = True
            break
    
    if whileloop:
        break
                
print(output)

# Your own programming language - Approach 1

import operator

def run(program: list) -> list:
    variables = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    ops = {"ADD": operator.add, "SUB": operator.sub, "MUL": operator.mul}

    ifs = {"==": operator.eq, "!=": operator.ne, "<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge}

    output = []
    k = 0
    whileloop = True
    while True:
        for i in program[k:]:
            k += 1
            whileloop = False
            part = i.split(" ")
            
            if part[0] == "MOV":
                variables[part[1]] = int(part[2]) if part[2] not in variables else variables[part[2]]
                
            elif part[0] in ops:
                if part[2] not in variables:
                    variables[part[1]] = ops[part[0]](variables[part[1]], int(part[2]))
                else:
                    variables[part[1]] = ops[part[0]](variables[part[1]], variables[part[2]])
            
            elif part[0] == "IF":
                if part[3] not in variables:
                    condition = ifs[part[2]](variables[part[1]],int(part[3]))
                else:
                    condition = ifs[part[2]](variables[part[1]],variables[part[3]])

                if condition:
                    k = program.index(part[5]+":")
                    break
                elif k == len(program): 
                    whileloop = True
                    break
                else:
                    continue       
            
            elif part[0] == "PRINT":
                output.append(int(part[1])) if part[1] not in variables else output.append(variables[part[1]])
                    
            elif part[0] == "JUMP":
                k = program.index(part[1]+":")
                break
            
            if part[0] == "END" or k == len(program):
                whileloop = True
                break
        
        if whileloop:
            break
    
    return output

program = ['MOV A 10', 'PRINT A', 'MOV B A', 'SUB B 8', 'PRINT B', 'SUB A B', 'PRINT A']
result = run(program)
print(result)
            
program1 = []
program1.append("MOV A 1")
program1.append("MOV B 2")
program1.append("PRINT A")
program1.append("PRINT B")
program1.append("ADD A B")
program1.append("PRINT A")
program1.append("END")
result = run(program1)
print(result)

program2 = []
program2.append("MOV A 1")
program2.append("MOV B 10")
program2.append("begin:")
program2.append("IF A >= B JUMP quit")
program2.append("PRINT A")
program2.append("PRINT B")
program2.append("ADD A 1")
program2.append("SUB B 1")
program2.append("JUMP begin")
program2.append("quit:")
program2.append("END")
result = run(program2)
print(result)

program3 = []
program3.append("MOV A 1")
program3.append("MOV B 1")
program3.append("begin:")
program3.append("PRINT A")
program3.append("ADD B 1")
program3.append("MUL A B")
program3.append("IF B <= 10 JUMP begin")
program3.append("END")
result = run(program3)
print(result)

program4 = []
program4.append("MOV N 50")
program4.append("PRINT 2")
program4.append("MOV A 3")
program4.append("begin:")
program4.append("MOV B 2")
program4.append("MOV Z 0")
program4.append("test:")
program4.append("MOV C B")
program4.append("new:")
program4.append("IF C == A JUMP error")
program4.append("IF C > A JUMP over")
program4.append("ADD C B")
program4.append("JUMP new")
program4.append("error:")
program4.append("MOV Z 1")
program4.append("JUMP over2")
program4.append("over:")
program4.append("ADD B 1")
program4.append("IF B < A JUMP test")
program4.append("over2:")
program4.append("IF Z == 1 JUMP over3")
program4.append("PRINT A")
program4.append("over3:")
program4.append("ADD A 1")
program4.append("IF A <= N JUMP begin")
result = run(program4)
print(result)

# # Your own programming language - Approach 2

def value(x, data):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return data[characters.index(x)]
    else:
        return int(x)
 
def condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<":
        return a < b
    if condition == "<=":
        return a <= b
    if condition == ">":
        return a > b
    if condition == ">=":
        return a >= b
 
def run(program):
    length = len(program)
    row = 0
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    result = []
    while True:
        if row == length:
            break
        parts = program[row].split(" ")
        if parts[0] == "PRINT":
            result.append(value(parts[1], data))
        if parts[0] == "MOV":
            data[characters.index(parts[1])] = value(parts[2], data)
        if parts[0] == "ADD":
            data[characters.index(parts[1])] += value(parts[2], data)
        if parts[0] == "SUB":
            data[characters.index(parts[1])] -= value(parts[2], data)
        if parts[0] == "MUL":
            data[characters.index(parts[1])] *= value(parts[2], data)
        if parts[0] == "JUMP":
            row = program.index(parts[1]+":")
            continue
        if parts[0] == "IF":
            if condition(value(parts[1], data), parts[2], value(parts[3], data)):
                row = program.index(parts[5]+":")
                continue
        if parts[0] == "END":
            break
        row += 1
    return result