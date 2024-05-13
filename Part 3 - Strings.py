# String operations

# Concatenate with '+'
begin = "ex"
end = "ample"
word = begin+end
print(word)

# Repeate with '*'
word = "banana"
print(word*3)

# Example - 1
string = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))

print(string * amount)

# Build a pyramid
n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

# ⭐ Build a pyramid - Approach 2
height = 5
i = 1
while i <= height:
    empty = height - i
    stars = 2 * i - 1
    print(" " * empty + "*" * stars)
    i += 1
    
# The print command within the loop prints a line, which begins with n spaces, followed by whatever is stored in the variable row. 
# Then two stars are added to the end of the variable row, and the value of the variable n is decreased by 1.

# Build a pyramid
n = 10 # number of layers in the pyramid
row = "Rehab"

while n > 0:
    print(" " * n * 6 + row)
    row += " Rehab Rehab"
    n -= 1

# Length of a string
# The function len returns the number of characters in a string, which is always an integer value.
# The length of a string includes all the characters in the string, including whitespace.

# Example 1
input_string = input("Please type in a string: ")
print(input_string)
print("-"*len(input_string))

# Example 2
string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string2) > len(string1):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")
    
# Index of a string
# As strings are essentially sequences of characters, any single character in a string can also be retrieved.
# The operator [] finds the character with the index specified within the brackets.

# The index refers to a position in the string, counting up from zero. 
# The first character in the string has index 0, the second character has index 1, and so forth.
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
# | E | x | a | m | p | l | e |

# Example 1
input_string = input("Please type in a string: ")
print(input_string[0])
print(input_string[1])
print(input_string[3])

# Since the first character in a string has the index 0, the last character has the index length - 1.

# Example 2 - Print out first and last character
input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[len(input_string) - 1])

# Implementation 2
input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[-1])

# Loop throughs string index
input_string = input("Please type in a string: ")
index = 0
while index < len(input_string):
    print(input_string[index])
    index += 1

# Negative index of a string
# A negative index counts backwards from the end of the string.
# You can also use negative indexing to access characters counting from the end of the string. 
# The last character in a string is at index -1, the second to last character is at index -2, and so forth. 
# You can think of input_string[-1] as shorthand for input_string[len(input_string) - 1].

# | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
# |  E |  x |  a |  m |  p |  l |  e |

input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[-1])

# Example - End to beginning - Approach 1
string = input("Pleae type in a string: ")
length = len(string) - 1

while length >= 0:
    print(string[length])
    length -= 1

# Example - End to beginning - Approach 2
input_string = input("Please type in a string: ")
index = -1
while index >= -len(input_string):
    print(input_string[index])
    index -= 1

# Second and second to last characters - Approach 1
string = input("Please type in a string: ")

second = string[1]
second_last = string[-2]

if second == second_last:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")
    
# Second and second to last characters - Approach 2
word = input("Please type in a string: ")
 
# Check also that the word is at least two characters long,
# so that the second and second to last characters exist
if len(word) > 1 and word[1] == word[-2]:
    print("The second and the second to last characters are " + word[1])
else:
    print("The second and the second to last characters are different")

# A line of hashes
width = int(input("Width: "))
print("#" * width)

# A rectangle of hashes
width = int(input("Width: "))
height = int(input("Height: "))
i = 0

while i < height:
    print("#"*width)
    i += 1

# Underlining - Approach 1
while True:
    string = input("Please type in a string: ")
    if len(string) > 0:
        print(string)
        print("-" * len(string))
    else:
        break

# Underlining - Approach 2
while True:
    string = input("Please type in a string: ")
    if string == "":
        break
    print(string)
    print(len(string) * "-")

# Right-Aligned
string = input("Please type in a string: ")
asterisk = 20 - len(string)
print("*" * asterisk + string)

# A framed word - Approach 1
word = input("Word: ")
lenght = len(word)

print("*" * 30)

begspace = int((30 - lenght)/2 - 1)
endspace = 30 - 2 - begspace - lenght

print("*" + " " * begspace + word + " " * endspace + "*")

print("*" * 30)

# A framed word - Approach 2
word = input("Word: ")
 
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
# If the word length is odd, one is added to the spaces at the end of the word
# to get all 30 characters filled
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)

# Substrings & Slices

# If you know the beginning and end indexes of the slice you wish to extract, you can do so with the notation [a:b]. 
# This means the slice begins at the index a and ends at the last character before index b - that is, including the first, but excluding the last. 
# [a : b] index selection >= a and selection < b
# Easily calculate the length of a slice with b-a

# Example 1
input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])

# Substring, Part 1
word = input("Please type in a string: ")
i = 1

while i <= len(word):
    print(word[:i])
    i += 1

# Substring, Part 2 - Backwards
word = input("Please type in a string: ")
i = len(word) - 1

while i >= 0:
    print(word[i:])
    i -= 1

# Searching for substrings
# The 'in' operator can tell us if a string contains a particular substring. 
# The Boolean expression 'a in b' is true, if 'b' contains the substring 'a'.

# Example 1
input_string = "test"

print("t" in input_string)
print("x" in input_string)
print("es" in input_string)
print("ets" in input_string)

# Example 2
input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    if substring in input_string:
        print("Found it")
    else:
        print("Not found")
        break

# Does it contain vowels - Approach 1
string = input("Please type in a string: ")

if "a" in string:
    print("a found")
else:
    print("a not found")

if "e" in string:
    print("e found")
else:
    print("e not found")

if "o" in string:
    print("o found")
else:
    print("o not found")


# ⭐ ⭐ Does it contain vowels - Approach 2
string = input("Please type in a string: ")
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1

# Index of substrings
# The operator 'in' returns a Boolean value, so it will only tell us if a substring exists in a string, but it will not be useful in finding out where exactly it is. 
# Python string method 'find' can be used to find the substring within a string. 
# It takes the substring searched for as an argument, and returns either the first index where it is found, or -1 if the substring is not found within the string.

# 'in' is an operator while 'find' is a method call.
# Method call for 'find' can be applied as such:
# my_string.find("xem")
# my_string -> the string within which we are looking
# .find() -> method call
# "xem" -> the substring we are looking for

# Example 1
input_string = "test"

print(input_string.find("t"))
print(input_string.find("x"))
print(input_string.find("es"))
print(input_string.find("ets"))

# Example 2
input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    index = input_string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    else:
        print("Not found")
        break

# Find the first substring - Approach 1
word = input("Please type in a word: ")
letter = input("Please type in a character: ")

i = word.find(letter)

if i >= 0 and i+3 <= len(word):
    print(word[i:i+3])

# Find the first substring - Approach 2
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = word.find(character)
if index!=-1 and len(word)>=index+3:
    print(word[index:index+3])
    
# Find all the substrings - Approach 1
word = input("Please type in a word: ")
letter = input("Please type in a character: ")

length = len(word)
i = word.find(letter)

while i != -1 and i <= length - 3:
    print(word[i : i +3])
    word = word[i + 1 :]
    i = word.find(letter)
    length = len(word)

# Find all the substrings - Approach 2
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1

# The second occurrence of substring - Approach 1
string = input("Please type in a string: ")
sub = input("Please type in a substring: ")

i = string.find(sub)

if i != -1:
    string = string[i + len(sub) : ]
    z = string.find(sub)
    if z != -1:
        i += len(sub)
        print(f"The second occurrence of the substring is at index {i + z}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")
    
# ⭐ The second occurrence of substring - Approach 2
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
 
index1 = string.find(substring)
index2 = -1
if index1 != -1:
    string = string[index1+len(substring):]
    index2 = string.find(substring)
 
if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".")