# Randomness
# https://docs.python.org/3/library/random.html?highlight=random#module-random
# https://docs.python.org/3/library/

# Generating a random number
# The function 'randint(a, b)' returns a random integer value between 'a' and 'b', inclusive. 
# For example, the following program works like a generic die:
from random import randint

print("The result of the throw:", randint(1, 6))

# The following program throws the die ten times:
from random import randint

for i in range(10):
    print("The result of the throw:", randint(1, 6))

# NB: it is worth remembering that the function randint works a bit differently when compared to, for example, slices, or the function range, which we've come across previously. 
# The function call randint(1, 6) results in a number between 1 and 6 inclusive, but the function call range(1, 6) results in a range of numbers from 1 to 5.

# More randomizing functions

# 'shuffle' function
# https://docs.python.org/3/library/random.html?highlight=random#random.shuffle

# The function 'shuffle' will shuffle any data structure passed as an argument, in place. 
# For example, the following program shuffles a list of words:
from random import shuffle

words = ["atlas", "banana", "carrot"]
shuffle(words)
print(words)

# 'choice' function
# The function choice returns a randomly picked item from a data structure:
from random import choice

words = ["atlas", "banana", "carrot"]
print(choice(words))

# Lottery numbers
# A common example for studying randomness is the case of lottery numbers. Let's try and draw some lottery numbers. 
# In Finland the national lottery consists of a pool of 40 numbers, 7 of which are chosen for each week's draw.

# A first attempt at drawing a set of numbers could look like this:
from random import randint

for i in range(7):
    print(randint(1, 40))
    
# This would not work in the long run, however, as the same number may appear twice in a single weekly draw of seven numbers. 
# We need a way to make sure the numbers drawn are all unique.
# One possibility is to store the drawn numbers in a list, and only add a number if it is not already on the list. 
# This can be repeated until the length of the list is seven:

from random import randint

weekly_draw = []
while len(weekly_draw) < 7:
    new_rnd = randint(1, 40)
    if new_rnd not in weekly_draw:
        weekly_draw.append(new_rnd)

print(weekly_draw)

# A more compact approach would be to use the shuffle function:
from random import shuffle

number_pool = list(range(1, 41))
shuffle(number_pool)
weekly_draw = number_pool[0:7]
print(weekly_draw)

# Here the idea is that we first create a list containing the available numbers 1 to 40, rather like the balls in a lottery machine. 
# The pool of numbers is then shuffled, and the first seven numbers chosen for the weekly draw. 
# This saves us the trouble of writing a loop.

# In fact, the 'random' module contains an even easier way to select lottery numbers: the 'sample' function. 
# It returns a random selection of a specified size from a given data structure:
from random import sample

number_pool = list(range(1, 41))
weekly_draw = sample(number_pool, 7)
print(weekly_draw)

# Lottery Numbers - Approach 1
# Please write a function named 'lottery_numbers(amount: int, lower: int, upper: int)', which generates as many random numbers as specified by the first argument. 
# All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. The numbers should be in ascending order in the returned list.
# As these are lottery numbers, no number should appear twice in the list.
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    number_pool = list(range(lower, upper+1))
    lottery_list = sample(number_pool, amount)
    lottery_list.sort()
    return lottery_list

print(lottery_numbers(7, 1, 40))

print()

for number in lottery_numbers(7, 1, 40):
    print(number)
    
# Lottery Numbers - Approach 2
from random import randint
 
def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        number = randint(lower, upper)
        if number not in numbers:
            numbers.append(number)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    return sorted(numbers)

# The features of the module random are based on an algorithm which produces random numbers based on a specific initialization value and some arithmetic operations.
# The initialization value is often called a seed value.

# The seed value can be supplied by the user with the "seed" function:
from random import randint, seed

seed(1337)
# this will always produce the same "random" number
print(randint(1, 100))

# If we have functions which rely on randomization, and we set seed value, the function will produce the same result each time it is executed. 
# The result may be different with different Python versions, but in essence randomness is lost by setting a seed value. 
# This can be a useful feature when testing a program, for example.

# Password generator, part 1 - Approach 1
from string import ascii_lowercase
from random import choices

def generate_password(len: int) -> str:
    password = choices(ascii_lowercase, k=len)
    return "".join(password)

for i in range(10):
    print(generate_password(8))
    
# Password generator, part 1 - Approach 2
from random import choice
from string import ascii_lowercase
 
def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
 
    return passwd

# Password generator, part 2 - Practice
from string import ascii_lowercase, digits
from random import choices

def generate_strong_password(length: int, nums: bool, special: bool) -> str:
    if nums and special:
        return nums_special_password(length)
    elif nums and not special:
        return nums_password(length)
    elif not nums and special:
        return special_password(length)
    elif not nums and not special:
        return string_password(length)


def nums_special_password(length):
    special = "!?=+-()#"
    characters = ascii_lowercase + digits + special
    weight = [1 + 1/len(characters)] * len(ascii_lowercase) + [1] * (len(digits) + len(special))
    password = choices(characters,  weights = weight, k=length)
    return "".join(password)    

def nums_password(length):
    characters = ascii_lowercase + digits
    weight = [1 + 1/len(characters)] * len(ascii_lowercase) + [1] * (len(digits))
    password = choices(characters,  weights = weight, k=length)
    return "".join(password) 

def special_password(length):
    special = "!?=+-()#"
    characters = ascii_lowercase + special
    weight = [1 + 1/len(characters)] * len(ascii_lowercase) + [1] * (len(special))
    password = choices(characters,  weights = weight, k=length)
    return "".join(password) 

def string_password(length):
    password = choices(ascii_lowercase, k=length)
    return "".join(password)    

for i in range(10):
    print(generate_strong_password(8, False, False))

# A higher ascii_lowercase weight relative to other characters does not guarantee at least 1 ascii_lowercase in the password.


# Using recursion to call the same function within the function until lowercase alphabet condition is met 

def test():
    password = choices("1234567890!@#$%^&*()a", k=3)
    counter = 0
    for i in ascii_lowercase:
        if i in password:
            counter += 1
    
    if counter == 0:
        return test()
    else: 
        return password
    
for i in range(10):
    print(test())
    
'''
Output:
['a', '#', '!']
['a', '1', ')']
['%', '3', 'a']
['^', 'a', '9']
['a', '%', '*']
['^', 'a', '#']
['&', '(', 'a']
['a', '(', '(']
['@', 'a', 'a']
['*', 'a', '#']
'''

# Password generator, part 2 - Approach 1
# Password generator functions below check whether any of the characters within the randomly generated password contains an ascii_lowercase, special characters, or digits.
# If lowercase alphabet does not exist or any of the characters required as minimum, the function calls itself again. The process is repeated until a password is generated with an appropriate minumum.
from string import ascii_lowercase, digits

from random import choices

def generate_strong_password(length: str, nums: bool, specials: bool):
    if nums and specials:
        return nums_specials(length)
    elif nums and not specials:
        return nums_password(length)
    elif not nums and specials:
        return specials_password(length)
    elif not nums and not specials:
        password = choices(ascii_lowercase, k=length)
        password = "".join(password)
        return password

def nums_specials(length):
    special = "!?=+-()#"
    characters = ascii_lowercase + digits + special
    password = choices(characters, k=length)
    if any(i in password for i in ascii_lowercase) and any(i in password for i in digits) and any(i in password for i in special):
        return "".join(password)
    else:
        return nums_specials(length)

def nums_password(length):
    characters = ascii_lowercase + digits
    password = choices(characters, k=length)
    if any(i in password for i in ascii_lowercase) and any(i in password for i in digits):
        return "".join(password)
    else:
        return nums_password(length)

def specials_password(length):
    special = "!?=+-()#"
    characters = ascii_lowercase + special
    password = choices(characters, k=length)
    if any(i in password for i in ascii_lowercase) and any(i in password for i in special):
        return "".join(password)
    else:
        return specials_password(length)

for i in range(10):
    print(generate_strong_password(8, True, True))

print()

for i in range(10):
    print(generate_strong_password(8, False, True))

print()

for i in range(10):
    print(generate_strong_password(8, True, False))

print()
    
for i in range(10):
    print(generate_strong_password(8, False, False))
    
# Password generator, part 2 - Approach 2
# This approach starts by running the 'choice' function on lowercase alphabets (this ensures that at least one character is a lowercase alphabet).
# Depending on whether numbers and special characters are placed 'True' in the function argument, the function then runs a 'choice' function on each character type individually to ensure minimum constraint.
# After the first mandatory lowercase alphabet selection, each subsequent choice function runs are done through an add_characters function where 'randint' function determins whether the selected character (either from the minimum set or the complete set) is appended to the beginning or the end of the existing password string.
# Once all mandatory minimum character types are added, the while loop runs until the full length specified in the function argument is achieved.
# the while loop runs the add_character function on the complete choice set and randomly appends each selection at either the beginning or end of the password string.
# The only discernable pattern here is that when both numbers and special characters are True, there will be a 3-character string placed next to each other that will contain an alphabet, number, and a special character back-to-back (in any possible order and in any possible position within the string)
# This is becase the add_character function does not randomly append character between the existing password string, only to the beginning or the end.
# Additionally, the alphabet character is added first to ensure minimum requirement, then a digit is placed either at the beginning or the end of the alphabet to meet the minimum requirement, and subsequently a special character is added at the beginning or the end. 
# The placement of the first three (if all bool arguments are true) ensure minimum requirement but also introduces a pattern of 3 different consecutive character types back-to-back.
from random import choice, randint
from string import ascii_lowercase, digits
 
def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    # One letter at beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
 
    # If numbers is wanted, add at least one number
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits
 
    # same for special characters
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
 
    # build the rest of the password from the whole set
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)
 
    return passwd
 
# Add a random character from the given set either
# at the beginning or end of the string
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character
    
for i in range(10):
    print(generate_strong_password(8, True, True))

print()

for i in range(10):
    print(generate_strong_password(8, False, True))

print()

for i in range(10):
    print(generate_strong_password(8, True, False))

print()
    
for i in range(10):
    print(generate_strong_password(8, False, False))

# Dice roller - Review
# In this exercise you will write some functions which can be used in games that involve dice.
# Instead of normal dice this exercise specifies non-transitive dice.
# https://singingbanana.com/dice/article.htm
# https://www.youtube.com/watch?v=LrIp6CKUlH8

dieA = [3, 3, 3, 3, 3, 6]
dieB = [2, 2, 2, 5, 5, 5]
dieC = [1, 4, 4, 4, 4, 4]

def roll(die: list) -> int:
    return choice(die)

for i in range(20):
    print(roll(dieA), " ", end="")

print()

for i in range(20):
    print(roll(dieB), " ", end="")
    
print()

for i in range(20):
    print(roll(dieC), " ", end="")
    


roll1 = [roll(dieA), roll(dieB), roll(dieC)]
print(roll1)
winnder = roll1.index(max(roll1))


def play(die1: list, die2: list, die3: list, times: int) -> tuple:
    reference = ["die1_wins","die2_wins", "die3_wins", "draws"]
    win_dict = {}
    win_dict["die1_wins"] = 0
    win_dict["die2_wins"] = 0
    win_dict["die3_wins"] = 0
    win_dict["draws"] = 0
    for i in range(times):
        throw = [roll(die1), roll(die2), roll(die3)]
        if throw.count(max(throw)) > 1:
            win_dict["draws"] += 1
        else:
            winner = throw.index(max(throw))
            win_dict[reference[winner]] += 1
    return (win_dict["die1_wins"], win_dict["die2_wins"], win_dict["die3_wins"], win_dict["draws"])

def roll(die: list) -> int:
    return choice(die)

dieA = [4, 4, 11, 11, 18, 18]
dieB = [2, 2, 14, 14, 17, 17]
dieC = [7, 7, 10, 10, 16, 16]

# dieA > dieB
# dieA > dieC
# dieB > dieC

play(dieA, dieB, dieC, 1000)

# Dice roller - Approach 1
from random import choice

def roll(die: str) -> int:
    die_dict = {}
    die_dict["A"] = [3, 3, 3, 3, 3, 6]
    die_dict["B"] = [2, 2, 2, 5, 5, 5]
    die_dict["C"] = [1, 4, 4, 4, 4, 4]
    return choice(die_dict[die])

for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")

def play(die1: str, die2: str, times: int) -> tuple:
    reference = ["die1_wins","die2_wins", "draws"]
    win_dict = {}
    win_dict["die1_wins"] = 0
    win_dict["die2_wins"] = 0
    win_dict["draws"] = 0    
    for i in range(times):
        rolli = [roll(die1), roll(die2)]
        if rolli.count(max(rolli)) > 1:
            win_dict["draws"] += 1
        else:
            winner = rolli.index(max(rolli))
            win_dict[reference[winner]] += 1
    return (win_dict["die1_wins"], win_dict["die2_wins"], win_dict["draws"])

result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)

# Dice roller - Approach 2
from random import sample
def roll(die: str):
    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
 
    return sample(dices[die], 1)[0]
 
def play(die1: str, die2: str, times: int):
    v1 = 0
    v2 = 0
    t = 0
    for i in range(times):
        n1 = roll(die1)
        n2 = roll(die2)
        if n1>n2:
            v1 += 1
        elif n1<n2:
            v2 += 1
        else:
            t += 1
    return v1, v2, t

# Random words - Review
# Exercise Files\words.txt

with open("Exercise Files\words.txt") as words:
    match = []
    for word in words:
        word = word.strip()
        if word.startswith("xeno"):
            match.append(word)

print(match)

from random import sample

sample(match, k = 15)   

len(match)         

# Random words - Approach 1
from random import sample

def words(n: int, beginning: str) -> list:
    with open("Exercise Files\words.txt") as words:
        match = []
        for word in words:
            word = word.strip()
            if word.startswith(beginning):
                match.append(word)
    
    if len(match) < n:
        raise ValueError(f"n sample size of {n} is larger than the matched list of length {len(match)}")
    else:
        return sample(match, k = n)
        
word_list = words(3, "xeno")
for word in word_list:
    print(word)

# Random words - Approach 2
import random
 
def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError("Not enough suitable words can be found!")
    return random.sample(word_list, n)