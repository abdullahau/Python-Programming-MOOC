# Generators

# We have already come across situations where we're dealing with a series of items, and we'd need the next item(s) in the series, 
# but we wouldn't necessarily want to formulate the entire series up to that point each time a new item is required. 
# Some recursive series, such as the Fibonacci number, are a good example of such a situation. 
# If each function call recursively generates the entire series up to the desired point, 
# we end up generating the beginning of the series many times over.

# Python _generators_ are a way of producing just the next item in a series when it is needed, essentially running the generation process for the series only once (for a given execution of a program). 
# They work mostly like normal functions, as they can be called and will return values, but the value a generator function returns differs from a normal function. 
# A normal function should return the same value every time, given the same arguments. 
# A generator function, on the other hand, should remember its current state and return the next item in the series, which may be different from the previous item.

# Just as there are many ways of solving most any programming problem, there are many ways of achieving a functionality similar to generators, 
# but generators can help make the program easier to understand, and can in certain situations save memory or other computational resources.

# The keyword yield

# A generator function must contain the keyword `yield`, which marks out the value which the function returns. 
# Let's take a look at a function which generates integer numbers, starting from zero and ending at a pre-determined maximum value:

def counter(max_value: int):
    number = 0
    while number <= max_value:
        yield number
        number += 1

# Now the `counter` function can be passed as an argument to the function `next()`:

if __name__ == "__main__":
    numbers = counter(10)
    print("First value:")
    print(next(numbers))
    print("Second value:")
    print(next(numbers))

# As you can see from the example above, the keyword `yield` is similar to the keyword `return`: both are used to define a return value. 
# The difference is that `yield` doesn't "close" the function in the same sense as `return`. 
# A generator function with the `yield` keyword keeps track of its state, and the next time it is called, it will continue from the same state.

# This generator also requires a maximum value, which was `10` in the example above. 
# When the generator runs out of values, it will raise a `StopIteration` exception:
if __name__ == "__main__":
    # creates a generator with maximum value 1
    numbers = counter(1)
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))

# The exception can be caught with a `try` - `except` block:
if __name__ == "__main__":
    numbers = counter(1)
    try:
        print(next(numbers))
        print(next(numbers))
        print(next(numbers))
    except StopIteration:
        print("ran out of numbers")

# Traversing through all the items in a generator is easily done with a `for` loop:
if __name__ == "__main__":
    numbers = counter(5)
    for number in numbers:
        print(number)

# Generators do not have to have a defined maximum value or termination point. 
# They can generate values infinitely (within other computational and physical constraints, naturally). 

# Pay mind, though: traversing a generator with a `for` loop only works if the generator terminates at some point. 
# If the generator is built on an infinite loop, trying to traverse it with a simple `for` loop will cause an endless execution, just like a `while` loop with no end or break condition would.

# Even numbers

# Please write a generator function named `even_numbers(beginning: int, maximum: int)` which takes two integers as its arguments. 
# The function should produce even numbers starting from `beginning` and ending with, at most, `maximum`.

def even_numbers(beginning: int, maximum: int):
    number = beginning if beginning % 2 == 0 else beginning + 1 
    while number <= maximum:
        yield number
        number += 2

numbers = even_numbers(2, 10)
for number in numbers:
    print(number)

numbers = even_numbers(11, 21)
for number in numbers:
    print(number)
    
# Prime numbers

# A prime number is a number which is divisible only by itself and the number 1. 
# By convention prime numbers are defined as positive integers from the number 2 upwards. 
# The first six prime numbers are 2, 3, 5, 7, 11 and 13.

# Please write a generator function `prime_numbers()` which creates a new generator. 
# The generator should return new prime numbers, one by one in sequence, from 2 onwards. 
# NB: this generator never terminates. It will generate numbers for as long as they are needed.

# Trial Division Method - Tests weather each candidate number is divisible by each prime returned before
def prime_numbers():
    prime = 2
    printed_list = []
    while True:
        yield prime
        printed_list.append(prime)
        prime = max(printed_list) + 1
        i = 0
        while i < len(printed_list):
            if prime % printed_list[i] != 0:
                i += 1
            else:
                prime += 1
                i = 0

numbers = prime_numbers()
for i in range(30):
    print(next(numbers))
    

# Trial Division Method - Approach 2
def prime_numbers():
    number = 1
    while True:
        if is_prime(number):
            yield number
        number += 1
 
# Helper method for checking if number is prime
def is_prime(number: int):
    if number < 2:
        return False
    # Possible divisor is between 2 and number-1
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# **Hint:** you can use a loop to check if a number is a prime number. 
# If we are checking the number `x`, the loop would go through the numbers `2` to `x-1`. 
# If `x` is divisible by any one of these, it is not a prime number.


# Prime Sieve Method

limit = 114

ints_to_limit = list(range(2,limit+1))

prime_numbers = []
composites = []
prime = 2

while True:
    prime_numbers.append(prime)
    for comp in ints_to_limit:
        if comp % prime == 0:
            composites.append(comp)
    ints_to_limit = sorted(list(set(ints_to_limit) - set(composites)))
    try:
        prime = ints_to_limit[0]
    except IndexError:
        break

for num in prime_numbers:
    print(num)
    
# Prime Sieve Method 2
limit = 114

ints_to_limit = list(range(2,limit+1))

prime_numbers = []
composites = []
prime = 2

while True:
    prime_numbers.append(prime)
    for comp in range(prime, limit+1, prime):
        composites.append(comp)
    ints_to_limit = sorted(list(set(ints_to_limit) - set(composites)))
    try:
        prime = ints_to_limit[0]
    except IndexError:
        break

for num in prime_numbers:
    print(num)
    
# Prime Sieve Method 3
limit = 114

ints_to_limit = list(range(2,limit+1))

prime_numbers = []
composites = []
prime = 2

while True:
    prime_numbers.append(prime)
    prime_comp = list(range(prime, limit+1, prime))
    composites = list(set(composites + prime_comp))
    ints_to_limit = sorted(list(set(ints_to_limit) - set(composites)))
    try:
        prime = ints_to_limit[0]
    except IndexError:
        break

for num in prime_numbers:
    print(num)


# Generator comprehensions

# You do not necessarily need a function definition to create a generator. 
# We can use a structure similar to a list comprehension instead. 
# This time we use _round_ brackets to signify a generator instead of a list or a dictionary:

# This generator returns squares of integers
squares = (x ** 2 for x in range(1, 64))

print(squares) # the printout of a generator object isn't too informative

for i in range(5):
    print(next(squares))
    
# In the following example we print out substrings of the English alphabet, each three characters long. 
# This prints out the first 10 items in the generator:

substrings = ("abcdefghijklmnopqrstuvwxyz"[i : i + 3] for i in range(24))

# print out first 10 substrings
for i in range(10):
    print(next(substrings))
    
# Random words

# Please write a function named `word_generator(characters: str, length: int, amount: int)` which returns a new generator for generating random words based on the parameters given.

# A random word is generated by selecting from the string named `characters` as many characters as is indicated by the argument `length`. 
# The same character can appear many times in a random word.
# The generator returns as many words as specified by the argument `amount` before terminating.
from random import choices

def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        yield "".join(choices(characters,k=length))

wordgen = word_generator("abcdefg", 3, 5)
for word in wordgen:
    print(word)

# Random Words - Approach 2
from random import choices

def word_generator(characters: str, length: int, amount: int):
    return ("".join(choices(characters,k=length)) for i in range(amount))

wordgen = word_generator("abcdefg", 3, 5)
for word in wordgen:
    print(word)

# Random Words - Approach 3
from random import choice
 
def word_generator(letters: str, length: int, amount:int):
    return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))
