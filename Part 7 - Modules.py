# Modules

# Debuggin Revisited
# Using the breakpoint() command
# When the program is run, the execution halts at the point where you inserted the breakpoint command.

# When the execution halts at the 'breakpoint' command, an interactive console window is opened. 
# Here you can write any code just as you would in a normal Python console, and see how the code works at exactly that point in the program.

# The 'breakpoint' command is especially useful when you know that some line of code causes an error, but you are not quite sure why that is. 
# Add a breakpoint just before the problematic line of code and run your program. 
# Now you can try out different options in the interactive console window, and figure out the correct commands to include in your program.

# It is also possible to continue execution from where it halted. 
# The command 'continue', or the shorthand 'c', typed into the debugging console will resume execution until the next breakpoint is reached. 
# There are also some other commands available in the debugging console. You may find them by typing in 'help' in the debugging console.

# Using Modules

# The Python standard library is a collection of standardised functions and objects, which can be used to expand the expressive power of Python in many ways.
# The standard library is comprised of modules, which contain functions and classes grouped around different themes and functionalities.
# https://docs.python.org/3/library/

# The command 'import' makes the contents of the given module accessible in the current program.

# Let's have a closer look at working with the 'math' module. It contains the definitions of some mathematical functions, such as 'sqrt' for square root and 'log' for logarithm.
import math

# The square root of the number 5
print(math.sqrt(5))
# the base 2 logarithm of the number 8
print(math.log(8, 2))

# The functions are defined in the 'math' module, so they must be referred to as 'math.sqrt' and 'math.log' in the program code.

# Selecting distinct sections from a module
# Another way to use modules is to select a distinct entity from the module with the 'from' command.

# In case we want to use just the functions 'sqrt' and 'log' from the module 'math', we can do the following:
from math import sqrt, log

print(sqrt(5))
print(log(5,2))

# As you can see above, we do not need the 'math' prefix when using the functions imported in this manner.

# Sometimes a handy shortcut is to import all the contents of a module with the star notation:
from math import *

print(sqrt(5))
print(log(5,2))

# Importing modules with the star notation can be useful when testing and in some smaller projects, but it can pose some new problems, too. 

# Hypotenuse - Approach 1
from math import sqrt

def hypotenuse(leg1: float, leg2: float) -> float:
    return sqrt(leg1**2 + leg2**2)

print(hypotenuse(3,4)) # 5.0
print(hypotenuse(5,12)) # 13.0
print(hypotenuse(1,1)) # 1.4142135623730951

# The contents of a module

# Inspecting the contents of a module using the 'dir' function:
import math

print(dir(math))

# The function returns a list of names defined by the module. 
# These may be, for example, names of classes, constant values or functions:

'''
Output:
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 
'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 
'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 
'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 
'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 
'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''

# https://docs.python.org/3/library/math.html

# Special characters - Review
import string

print(dir(string))

'''
Output:
['Formatter', 'Template', '_ChainMap', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', '_re', '_sentinel_dict', '_string', 'ascii_letters', 'ascii_lowercase', 
'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
'''
# https://docs.python.org/3/library/string.html

'''
String Constants:
string.ascii_letters - 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.punctuation - !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
string.whitespace - characters space, tab, linefeed, return, formfeed, and vertical tab
'''

# write a function named 'separate_characters(my_string: str)'. 
# The function takes a string as its argument, and it should separate the characters in the string into three other strings, and return these in a 'tuple':
    # The first string should contain the lowercase and uppercase ASCII letters (string constant ascii_letters)
    # The second string should contain all punctuation characters defined by the string constant punctuation
    # The third string should contain all the other characters (including whitespace)
# The characters should appear in the three strings in the same order as they appeared in the original string.

# lowercase and uppercase ASCII letters (string constant ascii_letters)
import string

text = "Olé!!! Hey, are ümläüts wörking?"
for letter in text:
    if letter in string.ascii_letters:
        print(letter)

'''
Letters in ASCII constant:
O
l
H
e
y
a
r
e
m
l
t
s
w
r
k
i
n
g
'''

# all punctuation characters defined by the string constant punctuation

import string

text = "Olé!!! Hey, are ümläüts wörking?"
for character in text:
    if character in string.punctuation:
        print(character)

'''
Characters in punctuation constant:
!
!
!
,
?
'''

# all the other characters (including whitespace)

import string

text = "Olé!!! Hey, are ümläüts wörking?"
for character in text:
    if character not in string.punctuation or character not in string.ascii_letters:
        print(character)

'''
Characters not in ASCII or punctionation constant:
é
 
 
 
ü
ä
ü
 
ö
'''

# Special characters - Approach 1
import string

def separate_characters(my_string: str):
    letters = ""
    punctuations = ""
    specials = ""
    for character in my_string:
        if character in string.ascii_letters:
            letters += character
        elif character in string.punctuation:
            punctuations += character
        else:
            specials += character
    return letters, punctuations, specials

parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])

# Special characters - Approach 2
from string import ascii_letters, punctuation
 
def separate_characters(my_string: str):
    letters = ""
    special_characters = ""
    other_characters = ""
 
    for character in my_string:
        if character in ascii_letters:
            letters += character
        elif character in punctuation:
            special_characters += character
        else:
            other_characters += character
 
    return (letters, special_characters, other_characters)

# Fractions - review
import fractions

print(dir(fractions))

'''
['Decimal', 'Fraction', '_FLOAT_FORMAT_SPECIFICATION_MATCHER', '_PyHASH_INF', '_PyHASH_MODULUS', '_RATIONAL_FORMAT', 
'__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'_hash_algorithm', '_round_to_exponent', '_round_to_figures', 'functools', 'math', 'numbers', 'operator', 're', 'sys']
'''

# write a function named fractionate(amount: int), which takes the number of parts as its argument. 
# The function should divide the number 1 into as many equal sized fractions as is specified by the argument, and return these in a list.

from fractions import Fraction

number = 5
result = Fraction(1,5)
print(result)
print(type(result))

# Output is of a class called fractions.Fraction


# Fractions - Approach 1
from fractions import Fraction

def fractionate(amount: int) -> list:
    frac_list = []
    for i in range(amount):
        frac_list.append(Fraction(1, amount))
    return frac_list

for p in fractionate(3):
    print(p)

print()

print(fractionate(5))

# Fractions - Approach 2
from fractions import Fraction
 
def fractionate(amount: int):
    # numerator, denominator
    fraction = Fraction(1, amount)
    
    # [] creates a list and the amount variable is used to multiply the result element within the list 
    return [fraction] * amount

for p in fractionate(3):
    print(p)

print()

print(fractionate(5))

# Multipying a list duplicates the occurrance of the elements within the list 
# l = [5,6] 
# r = l * 5
# print(r)
# >>> [5, 6, 5, 6, 5, 6, 5, 6, 5, 6]