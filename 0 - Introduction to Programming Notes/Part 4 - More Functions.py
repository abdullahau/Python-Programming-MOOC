# Line
def line(number, string):
    if string == "":
        string = "*"
    print(string[0] * number)

line(7, "%")
line(10, "LOL")
line(3, "")

# A box of hashes
def box_of_hashes(height):
    i = 0
    while i < height:
        line(10, "#")
        i += 1

box_of_hashes(5) 

# A square of hashes
def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1

square_of_hashes(5)

# A square
def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1

square(5, "*")
print()
square(3, "o")

# A triangle - Approach 1
def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

triangle(6)
print()
triangle(3)

# A triangle - Approach 2
def triangle(size):
    i = 0
    while i < size:
        i += 1
        line(i, '#')

# A shape - Approach 1
def shape(width, triangle, height, rectangle):
    i = 0
    while i < width:
        i += 1
        line(i, triangle)
    i = 0
    while i < height:
        line(width, rectangle)
        i += 1

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")

# A shape - Approach 2
def shape(y_height, y_character, a_height, a_character):
    i = 1
    while i <= y_height:
        line(i, y_character)
        i += 1
    i = a_height
    while i > 0:
        line(y_height, a_character)
        i -= 1

# A spruce (reference: Part 3 - Strings - Build a pyramid)
def spruce(size):
    i = size - 1
    row = "*"
    print("a spruce!")
    while i >= 0:
        print(" " * i + row)
        row += "**"
        i -= 1  
    print(" " * (size - 1) + "*")

spruce(5)

# A spruce - Approach 2
def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")
    
def max1(a, b):
    if a > b:
        return a
    else:
        return b

def max2(a, b):
    if a > b:
        print(a)
    else:
        print(b)

result = max1(3, 5)
print(result)

max2(7, 2)

result2 = max2(7, 2) # note that max2 uses print function to diretly output the maximum value to console. Thus, storing the function call result in a variable and printing the variable returns "None".
print(result2)

# The greatest number - Approach 1
def greatest_number(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    else:
        return number3

print(greatest_number(99, -4, 7))

# The greatest number - Approach 2
def greatest_number(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number3:
        return number2
    else:
        return number3
    
# The greatest number - Approach 3
def greatest_number(number1, number2, number3):
    return max(number1, number2, number3)

print(greatest_number(99, -4, 7))

# Same characters - Approach 1
def same_chars(string, index, index2):
    if index > len(string) - 1 or index2 > len(string) - 1:
        return False
    elif string[index] == string[index2]:
        return True
    else:
        return False
    
# Same characters - Approach 2
def same_chars(str, a, b):
    if a >= len(str) or b >= len(str):
        return False
    return str[a] == str[b] # running a comparison like this directly returns either True or False. No if statements and/or seperate returns are needed.

print(same_chars("programmer", 6, 7))
print(same_chars("programmer", 0, 4))
print(same_chars("programmer", 0, 12))

# First, second and last words - Approach 1
def first_word(sentence):
    index = sentence.find(" ")
    return sentence[0:index]

def second_word(sentence):
    index = sentence.find(" ")
    sentence = sentence[index + 1: len(sentence)]
    if sentence.find(" ") < 0:
        return sentence
    else:
        return sentence[0:sentence.find(" ")]

def last_word(sentence):
    i = - 1
    reverse = ""
    while i >= -len(sentence):
        reverse += sentence[i]
        i -= 1
    invert_index = - reverse.find(" ")
    return sentence[invert_index:]
    
sentence = "it was a dark and stormy python"
print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))

# First, second and last words - Approach 2
def find_word(str, whatth):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
    	if str[index] == " ":
    	    counter += 1
    	    if counter == whatth:
    	        break
    	    word = ""
    	else:
    	    word += str[index]
    	index += 1
    return word
 
def first_word(mjono):
    return find_word(mjono, 1)
 
def second_word(mjono):
    return find_word(mjono, 2)
 
def last_word(mjono):
    return find_word(mjono, 0)

sentence = "it was a programming langauge"
print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))

# First, second and last words - Approach 3
def first_second(sentence, word):
    index = sentence.find(" ")
    if word == 1:
        return sentence[0:index]
    else:
        sentence = sentence[index + 1: len(sentence)]
        if sentence.find(" ") < 0:
            return sentence
        else:
            return sentence[0:sentence.find(" ")]

def first_word(sentence):
    return first_second(sentence, 1)

def second_word(sentence):
    return first_second(sentence, 2)

def last_word(sentence):
    i = - 1
    reverse = ""
    while i >= -len(sentence):
        reverse += sentence[i]
        if sentence[i] == " ":
            break        
        i -= 1
    invert_index = - reverse.find(" ")
    return sentence[invert_index:]
    
sentence = "it was python"
print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))