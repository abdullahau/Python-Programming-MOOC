# Simple dictionary from Finnish to English
my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])

# After defining the dictionary we could also use it with user input:
word = input("Please type in a word: ")
if word in my_dictionary:
    print("Translation: ", my_dictionary[word])
else:
    print("Word not found")
    
# String keys and integer values
results = {}
results["Mary"] = 4
results["Alice"] = 5
results["Larry"] = 2

# Integer keys and list values
lists = {}
lists[5] = [1, 2, 3]
lists[42] = [5, 4, 5, 4, 5]
lists[100] = [5, 2, 3]

# If you add an entry using a key that already exists in the dictionary, the original value mapped to that key is replaced with the new value:
my_dictionary["suuri"] = "big"
my_dictionary["suuri"] = "large"
print(my_dictionary["suuri"])

# All keys in a dictionary must be immutable. So, a list cannot be used as a key, because it can be changed.

# Unlike keys, the values stored in a dictionary can change, so any type of data is acceptable as a value. A value can also be mapped to more than one key in the same dictionary.

# Traversing a dictionary

# The familiar 'for item in collection' loop can be used to traverse a dictionary
# When used on the dictionary directly, the loop goes through the keys stored in the dictionary, one by one. 

# In the following example, all keys and values stored in the dictionary are printed out:
my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key in my_dictionary:
    print("key:", key)
    print("value:", my_dictionary[key])
    
# Sometimes you need to traverse the entire contents of a dictionary. 
# The method 'items' returns all the keys and values stored in the dictionary, one pair at a time:
for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)

# The keys are processed in the same order as they were added to the dictionary. 
# As the keys are processed based on a hash value, the order should not usually matter in applications. 

# Advanced ways to use dictionaries

word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

# We would like to analyze this list of words in different ways. 
# For instance, we would like to know how many times each word appears in the list.

# A dictionary can be a useful tool in managing this kind of information. 
# In the example below, we go through the items in the list one by one. 
# Using the words in the list as keys in a new dictionary, the value mapped to each key is the number of times the word has appeared:
def counts(my_list):
    words = {}
    for word in my_list:
        # if the word is not yet in the dictionary, initialize the value to zero
        if word not in words:
            words[word] = 0
        # increment the value
        words[word] += 1
    return words

# call the function
print(counts(word_list))

# What if we wanted to categorize the words based on the initial letter in each word? One way to accomplish this would be to use dictionaries:
def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            groups[initial] = []
        # add the word to the appropriate list
        groups[initial].append(word)
    return groups

groups = categorize_by_initial(word_list)

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)

# Removing keys and values from a dictionary

# There are two ways to accomplish this. 

# The first is the command 'del':
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
del staff["David"]
print(staff)

# If you try to use the del command to delete a key which doesn't exist in the dictionary, there will be an error:
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
del staff["Paul"]

# before deleting a key you should check if it is present in the dictionary:
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
if "Paul" in staff:
  del staff["Paul"]
  print("Deleted")
else:
  print("This person is not a staff member")

# The other way to delete entries in a dictionary is the method 'pop':
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("David")
print(staff)
print(deleted, "deleted")

# 'pop' also returns the value from the deleted entry.

# By default, 'pop' will also cause an error if you try to delete a key which is not present in the dictionary. 
# It is possible to avoid this by giving the method a second argument, which contains a default return value. 
# This value is returned in case the key is not found in the dictionary. 
# The special Python value 'None' will work here:
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("Paul", None)
if deleted == None:
  print("This person is not a staff member")
else:
  print(deleted, "deleted")

# When traversing a collection with a 'for' loop, the contents may not change while the loop is in progress.
# Thus, you cannot delete the contents of the entire dictionary using a loop like so:
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
for key in staff:
  del staff[key]
  
# Luckily, there is a dictionary method for just this purpose:
staff.clear()

# Using dictionaries for structured data

# Dictionaries are very useful for structuring data. The following code will create a dictionary which contains some personal data:
person = {"name": "Pippa Python", "height": 154, "weight": 61, "age:" 44}

# The same information could just as well be stored in variables:
name = "Pippa Python"
height = 154
weight = 61
age = 44

# The advantage of a dictionary is that it is a collection. 
# It collects related data under one variable, so it is easy to access the different components. 
# This same advantage is offered by a list:
person = ["Pippa Python", 153, 61, 44]

# With lists, the programmer will have to remember what is stored at each index in the list. 
# There is nothing to indicate that 'person[2]' contains the weight and 'person[3]' the age of the person. 
# When using a dictionary this problem is avoided, as each bit of data is accessed through a named key.

# Assuming we have defined multiple people using the same format, we can access their data in the following manner:
person1 = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
person2 = {"name": "Peter Pythons", "height": 174, "weight": 103, "age": 31}
person3 = {"name": "Pedro Python", "height": 191, "weight": 71, "age": 14}

people = [person1, person2, person3]

for person in people:
    print(person["name"])

combined_height = 0
for person in people:
    combined_height += person["height"]

print("The average height is", combined_height / len(people))

# Word Count in a List
def counts(my_list):
    words = {}
    for word in my_list:
        # if the word is not yet in the dictionary, initialize the value to zero
        if word not in words:
            words[word] = 0
        # increment the value
        words[word] += 1
    return words

word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

# call the function
print(counts(word_list))

# Word Categorized by Initial Letter and Placed in Lists within a Dictionary
def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            groups[initial] = []
        # add the word to the appropriate list
        groups[initial].append(word)
    return groups

word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

groups = categorize_by_initial(word_list)

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)
    
# Step 1: The categorize_by_initial function takes a list of string as argument. 
# Step 2: Initializes a "groups" dictionary
# Step 3: Loops through the word list provided in the argument of the function and stores every item in the variable "word" for every iteration
# Step 4: Create a variable to reference the first index (or the first letter) in the "word" variable from the list. 
# Step 4: Initializes a new list and adds it to the dictionary "group" when the first letter is encountered in the word list by running an if-statement that checks if the first letter of the word (the "key") is already in the dictionary.
# Step 4a: Creates a new key in the dictionary "groups" with the first letter of the word as the key (only if the key is encountered for the first time - or if that key is not found in the "groups" dictionary)
# Step 5: For every word in the word list, the function then appends the word itself to its respective list created for each inital letter.

# Printing 1: The for loop unpacks and creates two variables (key and value) out of the newly generated dictionary "groups".
# Printing 2: The for loop iterates through the dictionary "groups" and prints the keys in the statement "words beginning with {key}"
# Printing 3: The nested for loop interates through the list within the dictionary key and prints each item in the list.


# Times ten
def times_ten(start_index: int, end_index: int):
    new_dictionary = {}
    for i in range(start_index, end_index + 1):
        new_dictionary[i] = i * 10
    return new_dictionary
        
d = times_ten(3, 6)
print(d)

# Factorials
def factorials(n: int):
    fact_dictionary = {}
    fact_dictionary[1] = 1
    for i in range(2, n + 1):
        fact_dictionary[i] = i * fact_dictionary[i-1]
    return fact_dictionary


k = factorials(5)
print(k[1])
print(k[3])
print(k[5])

# Histogram - Approach 1
def histogram(my_string: str):
    my_dictionary = {}
    for letter in my_string:
        if letter not in my_dictionary:
            my_dictionary[letter] = 0
        my_dictionary[letter] += 1
    for key, value in my_dictionary.items():
        print(f"{key}: {'*' * value}")
        
histogram("statistically")

# Histogram - Approach 2
def histogram(my_str: str):
    characters = {}
    for character in my_str:
        if character not in characters:
            characters[character] = 0
        characters[character] += 1
 
    for character, lkm in characters.items():
        stars = "*"*lkm
        print(f"{character} {stars}")

histogram("statistically")

# Phone book, version 1 - Approach 1
contact = {}

while True:
    user_input = int(input("command (1 search, 2 add, 3 quit): "))
    if user_input == 1:
        name = input("name: ")
        if name in contact:
            print(contact[name])
            continue
        else:
            print("no number")
            continue
    if user_input == 2:
        name = input("name: ")
        number = input("number: ")
        contact[name] = number
        print("ok!") 
        continue
    else:
        print("quitting...")
        break

# Phone book, version 1 - Approach 2
def search(persons):
    name = input("name: ")
    if name in persons:
        print(persons[name])
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()



# Phone book, version 2 - Approach 1
contact = {}

while True:
    user_input = int(input("command (1 search, 2 add, 3 quit): "))
    if user_input == 1:
        name = input("name: ")
        if name in contact:
            for num in contact[name]:
                print(num)
            continue
        else:
            print("no number")
            continue
    if user_input == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in contact:
            contact[name] = []
        contact[name].append(number)
        print("ok!") 
        continue
    else:
        print("quitting...")
        break

# Phone book, version 2 - Approach 2
def search(persons):
    name = input("name: ")
    if name in persons:
        for number in persons[name]:
            print(number)
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = []
    persons[name].append(number)
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()

# Invert a dictionary - Approach 1
def invert(my_dict: dict):
    inverted_dict = {}
    for key, value in my_dict.items():
        inverted_dict[value] = key
    my_dict.clear()
    for key, value in inverted_dict.items():
        my_dict[key] = value

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)

for key in s:
    print(s[key])

# Invert a dictionary - Approach 2
def invert(dictionary: dict):
	copy = {}
	for key in dictionary:
		copy[key] = dictionary[key]
	for key in copy:
		del dictionary[key]
	for key in copy:
		dictionary[copy[key]] = key
  

# Numbers spelled out - Approach 1
d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
        19 : 'nineteen', 20 : 'twenty',
        30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
        70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

def dict_of_numbers():
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            30, 40, 50, 60, 70, 80, 90]

    num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 
                'seventy', 'eighty', 'ninety']

    number_dict = {}

    for i in range(0, 100):
        if i not in num:
            number_dict[i] = f"{num_words[num.index(i // 10 * 10)]}-{num_words[num.index(i - (i // 10 * 10))]}"
        else:
            number_dict[i] = num_words[num.index(i)]
    
    return number_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])

# Numbers spelled out - Approach 2
def dict_of_numbers():
    # Helper dictionaries
    singles = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    whole_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
 
    numbers = {}
 
    # 0 - 9
    for i in range(10):
        numbers[i] = singles[i]
 
    # 10 - 19 are special cases
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"
 
    # 20 - 99
    for i in range(2, 10):
        numbers[i * 10] = whole_tens[i]
        for j in range(1, 10):
            numbers[i * 10 + j] = whole_tens[i] + "-" + singles[j]
 
    return numbers
 
if __name__ == "__main__":
    print(dict_of_numbers())

# Movie database - Approach 1
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {}
    movie["name"] = name
    movie["director"] = director
    movie["year"] = year
    movie["runtime"] = runtime
    database.append(movie)
    
database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)

# Movie database - Approach 2
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # Python accepts splitting rows from punctuation
    # The addition becomes more readable when parts are divided into separate rows
    movie = {"name": name,
               "director": director,
               "year": year,
               "runtime": runtime}
 
    database.append(movie)

# Find movies - Approach 1
def find_movies(database: list, search_term: str):
    filtered_database = []
    for i in range(len(database)):
        find_index = database[i]["name"].lower().find(search_term)
        if find_index != -1:
            filtered_database.append(database[i])
    return filtered_database


database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

my_movies = find_movies(database, "python")
print(my_movies)

# Find movies - Approach 2
def find_movies(database: list, search_term: str):
    found_ones = []
    for movie in database:
        # The function lower() converts a string to lowercase
        # when this is done for both strings search is case insensitive
        if search_term.lower() in movie["name"].lower():
            found_ones.append(movie)
 
    return found_ones
database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

my_movies = find_movies(database, "python")
print(my_movies)
        