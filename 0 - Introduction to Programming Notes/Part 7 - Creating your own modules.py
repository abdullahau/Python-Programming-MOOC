# Creating your own modules

# Any file containing valid Python code can be imported as a module.
# The functions defined in the file can be accessed by importing the file with the import statement and the file's name.
# The file containing the Python module must be located either in the same directory with the program importing it, or in one of the default Python directories, or else the Python interpreter will not find it when the import statement is executed.

# import <custom_module_name>
# from <custom_module_name> import <def functions>

# File name words.py
def first_word(my_string: str):
    parts = my_string.split(" ")
    return parts[0]

def last_word(my_string: str):
    parts = my_string.split(" ")
    return parts[-1]

def number_of_words(my_string: str):
    parts = my_string.split(" ")
    return len(parts)

# Importing the file
import words

my_string = "Sheila sells seashells by the seashore"

print(words.first_word(my_string))
print(words.last_word(my_string))
print(words.number_of_words(my_string))

# Importing modules
from words import first_word, last_word

sentence = input("Please type in a sentence: ")

print("The first word was: " + first_word(sentence))
print("The last word was: " + last_word(sentence))

# String helper - Approach 1
# Please write a module named string_helper, which contains the following functions:
# file: string_helper.py

# The function 'change_case(orig_string: str)' creates and returns a new version of the parameter string. 
# The lowercase letters in the original should be uppercase, and uppercase letters should be lowercase.

# The function 'split_in_half(orig_string: str)' splits the parameter string in half, and returns the results in a tuple. 
# If the original has an odd number of characters, the first half should be shorter.

# The function 'remove_special_characters(orig_string: str)' returns a new version of the parameter string, with all special characters removed. 
# Only lowercase and uppercase letters, numbers and spaces are allowed in the returned string.

from string_helper import change_case, split_in_half, remove_special_characters

my_string = "Well hello there!"

print(change_case(my_string))

p1, p2 = split_in_half(my_string)

print(p1)
print(p2)

m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
print(m2)


# String helper - Approach 2
from string import ascii_letters, digits
 
def change_case(orig_string: str):
    new_string = ""
    for character in orig_string:
        if character.isupper():
            new_string += character.lower()
        elif character.islower():
            new_string += character.upper()
        else:
            new_string += character
 
    return new_string
 
def split_in_half(orig_string: str):
    return orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:]
 
def remove_special_characters(orig_string: str):
    allowed = ascii_letters + digits + ' '
    new_string = ""
    for character in orig_string:
        if character in allowed:
            new_string += character
 
    return new_string
