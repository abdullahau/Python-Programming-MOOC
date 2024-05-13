# Accessing part of a list or a string using the [] syntax 
my_string = "exemplary"
print(my_string[3:7])

my_list = [3,4,2,4,6,1,2,4,2]
print(my_list[3:7])

# Using [] syntax to access a range of specified index items along with steps & directions
my_string = "exemplary"
print(my_string[0:7:2]) # starts at index 0 and ends at 7-1 with a step of 2
my_list = [1,2,3,4,5,6,7,8]
print(my_list[6:2:-1]) # starts at index 6 and ends at 2-1 in reverse steps of -1

# [] syntax to access enitre range of items starting from a specified index
my_string = "exemplary"
print(my_string[0:7:2]) # runs from the start to the 7-1th index with a step of 2
print(my_string[::2]) # runs from the start to the end index with a step of 2
my_list = [1,2,3,4,5,6,7,8]
print(my_list[:2:-1]) # runs from the very last index to the 2-1th index in reverse steps of -1
print(my_list[6::-1]) # runs from the 6th index to the first index in reverse steps of -1

# Reverse strings and lists with a simple [] syntax
my_string = "exemplary"
print(my_string[::-1])
my_list = [1,2,3,4,5,6,7,8]
print(my_list[::-1])

# Everything reversed
def everything_reversed(my_list: list):
    new_list = []
    for i in my_list:
        new_list.append(i[::-1]) # reversing the items within the list by looping through the list
    new_list = new_list[::-1] # reversing the list itself
    return new_list

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)

# String are immutable
my_string = "exemplary"
my_string[0] = "a" # outputs: 'str' object does not support item assignment

# Strings are immutale but references to strings are not.
my_string = "Hey"
my_string = my_string + "!"
my_string # Strings themselves are immutable, but the variables holding them are not. A string can be replaced by another string.

# Lists are mutable
my_list = [1,2,3]
my_list[0] = 10
my_list

# 'count' method - counts the number of times the specified item or substring occurs in the target
my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(my_string.count("ch"))

my_string = "aaaa"
print(my_string.count("aa")) # The method will not count overlapping occurrences.
# The method counts only two occurrences of the substring aa, even though there would actually be three if overlapping occurrences were allowed.

my_list = [1,2,3,1,4,5,1,6]
print(my_list.count(1))

# 'replace' method - creates a new string, where a specified substring is replaced with another string
my_string = "Hi there"
new_string = my_string.replace("Hi", "Hey")
print(new_string)

# The 'replace' method will replace all occurrences of the substring:
sentence = "sheila sells seashells on the seashore"
print(sentence.replace("she", "SHE"))
sentence # However, the method call will not change the original string itself and an unchanged string reference will return the original string.

# String are immutable and thus the replace method does not change the original string.
my_string = "Python is fun"

# Replaces the substring but doesn't store the result...
my_string.replace("Python", "Java")
print(my_string)

# However, new string can be assigned to the same variable:
my_string = "Python is fun"

# Replaces the substring and stores the result in the same variable
my_string = my_string.replace("Python", "Java")
print(my_string)

# Most common character - Approach 1
def most_common_character(my_string: str):
    count = 0
    for i in my_string:
        if my_string.count(i) > count:
            count = my_string.count(i)
            common_character = i
    return common_character

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))

# Most common character - Approach 2
def most_common_character(my_string: str):
    most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common): # if-condition assess whether the current character count in my_string exceeds the character count of the most common character placed inside most_common variable thus far
            most_common = character
 
    return most_common

# ⭐ ⭐ No vowels allowed - Approach 1 - vowels as string in list
def no_vowels(my_string: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        my_string = my_string.replace(i, "")
    return my_string


my_string = "this is an example"
print(no_vowels(my_string))

# No vowels allowed - Approach 1 - vowels as string
def no_vowels(my_string: str):
    vowels = "aeiou"
    for i in vowels:
        my_string = my_string.replace(i, "")
    return my_string


my_string = "this is an example"
print(no_vowels(my_string))

# No vowels allowed - Approach 2
def no_vowels(my_string: str):
    vowels = "aeiou"
    result = ""
 
    for letter in my_string:
        if letter not in vowels: # Main loop iterates through the entire my_string and assess whether the letter appears in the vowel string. If letter is found in the vowel string, the letter is not added to the result variable.
            result += letter
 
    return result

my_string = "this is an example"
print(no_vowels(my_string))

# No shouting allowed
def no_shouting(my_list: list[str]) -> list:
    result = []
    for i in my_list:
        if i.isupper() != True:
            result.append(i)           
    return result

my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)

# No shouting allowed - Approach 2
def no_shouting(my_list: list):
    without_upper = []
 
    for string in my_list:
        if not string.isupper(): # we can use "if not" condition to check whether the string is uppercase or not.
            without_upper.append(string)
 
    return without_upper

# Neighbours in a list - Approach 1
def longest_series_of_neighbours(my_list: list):
    counter = 0
    counter_max = 0
    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            counter += 1
        else:
            if counter_max < counter:
                counter_max = counter
            counter = 0
    return max(counter, counter_max) + 1
    
my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))

my_list = [1, 2, 5, 4, 3, 4]
print(longest_series_of_neighbours(my_list))

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0, 1, 2, 3]
print(longest_series_of_neighbours(my_list))

# ⭐ ⭐ Neightbours in a list - Approach 2
def longest_series_of_neighbours(my_list: list):
    longest = 1 # the lowest value of the longest neighbour sequence cannot be lower than 1
    result = 1 # given that the lowest value possible is 1 and the counter is always added up N times (N+1 = neighbour series length) which is 1 less than the neighbour series length, starting the counter with 1 helps. 
    for i in range(1, len(my_list)): # range is 1 less than the length of the original list to factor the reduced length of the increment list.
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))

my_list = [1, 2, 5, 4, 3, 4]
print(longest_series_of_neighbours(my_list))

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0, 1, 2, 3]
print(longest_series_of_neighbours(my_list))