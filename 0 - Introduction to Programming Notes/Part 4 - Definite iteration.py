# Definite iteration
# Indefinite Iteration - 'while' loop
my_list = [3, 2, 4, 5, 2]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# Definite Iteration - 'for' loop
my_list = [3, 2, 4, 5, 2]

for item in my_list:
    print(item)
    
# Sample structure of a for loop
# for <variable> in <collection>:
#    <block>

# Example 1
name = input("Please type in your name: ")

for character in name:
    print(character)
    
# The function range
# Example 1 - range function
for i in range(5):
    print(i) 

# Example 2 - range function 
for i in range(3, 7):
    print(i)

# Example 3 - range function
for i in range(1, 9, 2):
    print(i)
    
# Example 4 - range function
for i in range(6, 2, -1):
    print(i)

# From a range to a list
numbers = range(2, 7)
print(numbers) # outputs only the description of a range object

numbers = list(range(2, 7))
print(numbers) # 'list' function will convert a range into a list. The list will contain all the values that are in the range.

# Finding the best or the worst item in a list - Sample code structure
# best = initial_value # The initial value depends on the situation
# for item in my_list:
#     if item is better than best:
#         best = item
# We now have the best one figured out!


# Star-studded
string = input("Please type in a string: ")

for letter in string:
    print(letter)
    print("*")
    
# From negative to positive
number = int(input("Please type in a positive integer: "))
for i in range(-number, number + 1):
    if i == 0:
        continue
    print(i)

# From positive to negative - Appraoch 2
number = int(input("Please type in a positive integer: "))
 
for i in range(-number, number + 1):
    # Because in Python bool-type equals to
    # 0 and 1 (False and True), condition can also be written as follows
    # if i:
    if i != 0:
        print(i)
    
# List of stars
def list_of_stars(list: list):
    for i in list:
        print("*" * i)

list_of_stars([3, 7, 1, 1, 2])

# Anagrams - Approach 1
def anagrams(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

print(anagrams("tAMe", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False

# Anagrams - Approach 2
def anagrams(string1, string2):
    list1 = []
    list2 = []
    for i in string1.lower():
        list1.append(i)
    for i in string2.lower():
        list2.append(i)
    list1.sort()
    list2.sort()
    return list1 == list2

print(anagrams("tAmE", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tAmE", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False

# Anagram - Notes
string1 = "Abdullah"
list1 = []
for i in string1.lower():
    list1.append(i)
list1.sort()

string2 = "Halludba"
list2 = []
for i in string2.lower():
    list2.append(i)
list2.sort()

print(list1)
print(list2)

print(list1 == list2)

# Palindromes - Approach 1
def palindromes(string):
    item = ""
    for i in range(-1, -len(string)-1,-1):
        item += string[i]
    return string == item
        
while True:
    string = input("Please type in a palindrome: ")
    if palindromes(string.lower()) == True:
        print(f"{string} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
        
# ⭐ Palindromes = Approach 2
def palindromes(word: str):
    for i in range(len(word)//2): # code divides the string into half and assesses weather each character in each half is a match
        if word[i] != word[len(word)-i-1]:
            return False
    return True
 
while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(word, "is a palindrome!")
        break
    print("that wasn't a palindrome")
        
# Palindromes = Approach 2 explained
word = "neveroddoreven"
numbers = list(range(len(word)//2)) # -> range funtions runs half of the length of the string
print(numbers) 
word[2] # -> character returned from the string index must match the reverse index
word[len(word)-1-2] # -> character returned from the reverse string index must match the standard index
# if each character in the left-to-right half of the string matches matches the right-to-left half, the string is a palindrome
# e.g. string = "neveroddoreven" would be split as:
# left-to-right half: n-e-v-e-r-o-d-d 
# right-to-left half: o-d-d-o-r-e-v-e-n
# the last character of the right-to-left and first character of the left-to-right are compared until half of the word.

# The sum of positive numbers
def sum_of_positives(my_list: list) -> int:
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i
    return sum

numbers = [1, -2, 3, -4, 5]
number = sum_of_positives(numbers)
print(number)

# Even numbers
def even_numbers(my_list: list) -> list:
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

# The sum of lists
def list_sum(list1, list2):
    new_list = []
    for i in range(len(list1)):
        sum = list1[i] + list2[i]
        new_list.append(sum)
    return new_list

a = [1, 2, 3]
b = [7, 8, 9]
list_sum(a,b)

# The sum of lists - Notes
a = [1, 2, 3]
b = [7, 8, 9]
# summing a list with another list simply appends the second list to the end of the first list as such:
a + b # [1, 2, 3, 7, 8, 9]

a = [1, 2, 3]
b = [7, 8, 9]
new_list = []
for i in range(len(a)):
    sum = a[i] + b[i]
    new_list.append(sum)
print(new_list)

# The sum of lists - Approach 2
def list_sum(list1: list, list2: list):
    results = []
    for i in range(len(list1)):
        results.append(list1[i] + list2[i])
 
    return results
# Another solution would be use zip-function,
# which creates new list by combining items in two or more lists
# for item1, item2 in zip(list1, list2):
#   results.append(item1 + item2)

# The sum of lists - Approach 3
list1 = [1, 2, 3]
list2 = [7, 8, 9]
results = []
for item1, item2 in zip(list1, list2): # zip function combines two or more lists
    results.append(item1 + item2)
print(results)

zip(list1, list2) # returns a cryptic data type <zip at 0x1ce80013340>
type(zip(list1, list2)) # data type = zip
list(zip(list1, list2)) # outputs a tuple which is a combination of two or more lists: [(1, 7), (2, 8), (3, 9)]
# the for loop here takes the two items at each index within the zip and assigns it to two for loop variables.

# Distinct numbers - Approach 1
def distinct_numbers(my_list):
    new_list = []
    sorted_list = sorted(my_list)
    for i in range(len(sorted_list)):
        if sorted_list[i] in new_list: # Condition looks at the new_list to assess wether the current number exists within the list
            continue
        else:
            new_list.append(sorted_list[i])
    return new_list
    
my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]

# Distinct numbers - Approach 2
def distinct_numbers(my_list):
    new_list = []
    sorted_list = sorted(my_list)
    for i in range(len(sorted_list)):
        if sorted_list[i] in sorted_list[:i]: # Condition looks at the sorted list up until the current index to assess repetition
            continue
        else:
            new_list.append(sorted_list[i])
    return new_list
    
my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]

my_list = [3, 2, 2, 1, 3, 3, 1]
list(range(len(my_list)))

# Distinct numbers - Approach 3
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results: # rather than checking for existence with an "in" operator, "not in" operator checks for non-existence and returns true if the item does not exist in a list or a string.
            results.append(item)
 
    results.sort()
    return results

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]

# The length of the longest in the list
def length_of_longest(my_list: list):
    max_len = 0
    for i in my_list:
        if len(i) > max_len:
            max_len = len(i)
    return max_len

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)

# The shortest in the list
def shortest(my_list: list):
    word = my_list[0]
    for i in my_list:
        if len(i) < len(word):
            word = i
    return word

my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)

# The shortest in the list - Approach 2
def shortest(names: list):
    result = "" # creates an empty string helper variable
 
    for nimi in names:
        if result == "" or len(nimi) < len(result): # returns true when either the helper variable is empty OR if the length of the string in the list is less than the value stored inside the helper variable.
            result = nimi
 
    return result

# All the longest in the list - Approach 1
def all_the_longest(my_list: list):
    max_len = 0
    for i in my_list:
        if len(i) > max_len:
            max_len = len(i)
    result = []
    for i in my_list:
        if len(i) == max_len:
            result.append(i)
    return result

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result) # ['eleventh']

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']


# ⭐ All the longest in the list - Approach 2

# At its core, the defined function loops through all the items within the input list and compares the length of each string to the length of the first string in the result list. 
# If the string being assessed is larger, the result list is reset and contains only the new string. 
# Otherwise, if the string is the same length as the first/existing string in the list, the string is appended to result list. 
def all_the_longest(names: list):
    result = []
 
    for name in names:
        if result == [] or len(name) > len(result[0]): # returns true when either the helper variable is empty OR if the length of the first string in the list is less than the value stored inside the helper variable.
            result = [name] # if the above condition is true (i.e, if the list is empty or if the first content within the list is smaller than the value stored inside the helper variable), then the result list is reset with only the longest word placed in the list.
        elif len(name) == len(result[0]): # Returns true when the helper variable is the same length as the first string in the list.
            result.append(name) # if true, the result list is appended with an item of the equivalent length.
 
    return result

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result) # ['eleventh']

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']