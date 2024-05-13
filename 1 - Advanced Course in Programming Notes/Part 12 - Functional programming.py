# Functional programming

# Functional programming minimizes changes in program state, often avoiding variables and relying on function chains.
# Common techniques in functional programming include lambda expressions and comprehensions, which process data without altering program state.
# Functional programming is a programming paradigm alongside imperative, procedural, and object-oriented programming.
# Divisions between programming paradigms can vary, but understanding different approaches is crucial for making programming choices.
# Python supports various programming paradigms, allowing programmers to choose the most suitable method for each problem.
# Python provides tools for functional programming, offering versatility in programming approaches.

# map

# The `map` function executes some operation on each item in an iterable series. 
# This sounds a lot like the effect a comprehension has, but the syntax is different.

# Let's assume we have list of strings which we want to convert into a list of integers:

str_list = ["123","-10", "23", "98", "0", "-110"]

integers = map(lambda x : int(x), str_list)

print(integers) # this tells us the type of object we're dealing with

for number in integers:
    print(number)
    
# The general syntax for the `map` function is
# `map(<function>, <series>)`
# where `function` is the operation we want to execute on each item in the `series`.

# The `map` function returns an object of type `map`, which is iterable, and can be converted into a list:

def capitalize(my_string: str):
    first = my_string[0]
    first = first.upper()
    return first + my_string[1:]

test_list = ["first", "second", "third", "fourth"]

capitalized = map(capitalize, test_list)

capitalized_list = list(capitalized)
print(capitalized_list)


# As you can see from the examples above, the `map` function accepts both an anonymous lambda function and a named function defined with the `def` keyword.

# We could achieve the same result with a list comprehension:
def capitalize(my_string: str):
    first = my_string[0]
    first = first.upper()
    return first + my_string[1:]

test_list = ["first", "second", "third", "fourth"]

capitalized_list = [capitalize(item) for item in test_list]
print(capitalized_list)

# ...or we could go through the original list with a `for` loop and save the processed items in a new list with the `append` method. 
# Typically, in programming there are many different solutions to each problem. 
# There are rarely any absolutely right or wrong answers. 
# Knowing many different approaches helps you choose the most appropriate one for each situation, or one that best suits your own tastes.

# It is worth pointing out that the `map` function does not return a list, but an _iterator_ object of type map. 
# An iterator behaves in many ways like a list, but there are exceptions, as can be seen in the following example:
def capitalize(my_string: str):
    first = my_string[0]
    first = first.upper()
    return first + my_string[1:]

test_list = ["first", "second", "third", "fourth"]

# store the return value from the map function
capitalized = map(capitalize, test_list)

for word in capitalized:
  print(word)

print("print the same again:")
for word in capitalized:
  print(word)
  
# Above we tried to print out the contents of the `map` iterator twice, but the second attempt produced no printout. 
# The reason is that `map` is an iterator; passing through it with a `for` loop "depletes" it, much like a generator is depleted once its maximum value is reached. 
# Once the items in the iterator have been traversed with a `for` loop, there is nothing left to go through.

# If you need to go through the contents of a `map` iterator more than once, you could, for example, convert the map into a list:
test_list = ["first", "second", "third", "fourth"]

# convert the return value of the map function into a list
capitalized = list(map(capitalize, test_list))

for word in capitalized:
  print(word)

print("print the same again:")
for word in capitalized:
  print(word)

# The map function and your own classes

# You can naturally also process instances of your own classes with the `map` function. 
# There are no special gimmicks involved, as you can see in the example below:

class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float):
        self.__account_number = account_number
        self.name = name
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

a1 = BankAccount("123456", "Randy Riches", 5000)
a2 = BankAccount("12321", "Paul Pauper", 1)
a3 = BankAccount("223344", "Mary Millionaire ", 1000000)

accounts = [a1, a2, a3]

clients = map(lambda t: t.name, accounts)
for name in clients:
  print(name)

balances = map(lambda t: t.get_balance(), accounts)
for balance in balances:
  print(balance)
  
# Here we first collect the names of the account holders with the `map` function. 
# An anonymous lambda function is used to retrieve the value of the `name` attribute from each BankAccount object:
clients = map(lambda t: t.name, accounts)

# Similarly, the balance of each BankAccount is collected. 
# The lambda function looks a bit different, because the balance is retrieved with a method call, not from the attribute directly:
balances = map(lambda t: t.get_balance(), accounts)

# Attempted courses

# The exercise template contains the class definition for a `CourseAttempt`. It works like this:
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
print(attempt.student_name)
print(attempt.course_name)
print(attempt.grade)
print(attempt)

# Part 1 - Names of Students

# Please write a function named `names_of_students(attempts: list)` which takes a list of CourseAttempt objects as its argument. 
# The function should return a new list with the names of the students who have attempted the course.
def names_of_students(attempts: list):
    return list(map(lambda c: c.student_name, attempts))

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in names_of_students([s1, s2, s3]):
    print(name)
    
# Part 2 - Courses

# Please write a function named `course_names(attempts: list)` which takes a list of CourseAttempt objects as its argument. 
# The function should return a new list containing the names of the courses on the original list in alphabetical order. 
# Each course name should appear only once on the list.
def course_names(attempts: list):
    return sorted(list(set(map(lambda c: c.course_name, attempts))))

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in course_names([s1, s2, s3]):
    print(name)

# Attempted Courses - Approach 2
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade
 
    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
 
def names_of_students(course_names: list):
    def student(attempt: CourseAttempt):
        return attempt.student_name
 
    return map(student, course_names)
    # same using lambda function
    # return map(lambda k: k.student_name, course_names)
 
def course_names(course_names: list):
    names = map(lambda k: k.course_name, course_names)
    # remove duplicates by using a set
    return sorted(list(set(names)))


# filter

# The built-in Python function `filter` is similar to the `map` function, but, as the name implies, it doesn't take all the items from the source. 
# Instead, it filters them with a criterion function, which is passed as an argument. 
# If the criterion function returns `True`, the item is selected.

# Let's look at an example using `filter`:
integers = [1, 2, 3, 5, 6, 4, 9, 10, 14, 15]

even_numbers = filter(lambda number: number % 2 == 0, integers)

for number in even_numbers:
    print(number)
    
# It might make the above example a bit clearer if we used a named function instead:
def is_it_even(number: int):
    if number % 2 == 0:
        return True
    return False

integers = [1, 2, 3, 5, 6, 4, 9, 10, 14, 15]

even_numbers = filter(is_it_even, integers)

for number in even_numbers:
    print(number)

# These two programs are functionally completely identical. 
# It is mostly a matter of opinion which you consider the better approach.

# Let's have a look at another filtering example. 
# This program models fishes, and selects only those which weigh at least 1000 grams:
class Fish:
    """ The class models a fish of a certain species and weight """
    def __init__(self, species: str, weight: int):
        self.species = species
        self.weight = weight

    def __repr__(self):
        return f"{self.species} ({self.weight} g.)"

if __name__ == "__main__":
    f1 = Fish("Pike", 1870)
    f2 = Fish("Perch", 763)
    f3 = Fish("Pike", 3410)
    f4 = Fish("Cod", 2449)
    f5 = Fish("Roach", 210)

    fishes = [f1, f2, f3, f4, f5]

    over_a_kilo = filter(lambda fish : fish.weight >= 1000, fishes)

    for fish in over_a_kilo:
        print(fish)

# We could just as well use a list comprehension and achieve the same result:
over_a_kilo = [fish for fish in fishes if fish.weight >= 1000]

# The return value of filter is an iterator

# The `filter` function resembles the `map` function in also that it returns an _iterator_. 
# There are situations where you should be especially careful with `filter` as iterators can only be traversed once. 
# So, trying to print out the collection of large fishes twice will not work quite as straightforwardly as you might think:

f1 = Fish("Pike", 1870)
f2 = Fish("Perch", 763)
f3 = Fish("Pike", 3410)
f4 = Fish("Cod", 2449)
f5 = Fish("Roach", 210)

fishes = [f1, f2, f3, f4, f5]

over_a_kilo = filter(lambda fish : fish.weight >= 1000, fishes)

for fish in over_a_kilo:
    print(fish)

print("print the same again:")

for Fish in over_a_kilo:
    print(Fish)

# If you need to go through the contents of a `filter` iterator more than once, you could convert the result into a list:

fishes = [f1, f2, f3, f4, f5]

# convert the return value of the filter function into a list
over_a_kilo = list(filter(lambda fish : fish.weight >= 1000, fishes))

# Filtering attempts

# In this exercise we will continue with the `CourseAttempt` class.
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Part 1 - Accepted attempts

# Please write a function named `accepted(attempts: list)` which takes a list of CourseAttempt objects as its argument. 
# The function should return a new list of CourseAttempt objects, including only those items from the original list whose grade is at least 1.

def accepted(attempts: list):
    return list(filter(lambda c: c.grade >= 1, attempts))

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

for attempt in accepted([s1, s2, s3]):
    print(attempt)

# Part 2 - Attempts with grade

# Please write a function named `attempts_with_grade(attempts: list, grade: int)` which takes a list of CourseAttempt objects and an integer as its arguments. 
# The function should return a new list containing only those CourseAttempt objects from the original list whose grade matches the second argument.

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda c: c.grade == grade, attempts))

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
    print(attempt)

# Part 3 - Students who passed the course

# Please write a function named `passed_students(attempts: list, course: str)` which takes a list of CourseAttempt objects and a course name as its arguments. 
# The function should return an _alphabetically ordered_ list of names of those students who passed the course, i.e. their grade for the given course was higher than 0.

def passed_students(attempts: list, course: str):
    return sorted(list(map(lambda x: x.student_name, filter(lambda c: c.grade > 0 and c.course_name == course, attempts))))

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
    print(attempt)

# Filtering Attempts - Approach 2
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade
 
    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
 
 
def accepted(attempts: list):
    return filter(lambda s: s.grade>0, attempts)
 
def attempts_with_grade(attempts: list, grade: int):
    return filter(lambda s: s.grade==grade, attempts)
 
def passed_students(attempts: list, course: str):
    course_attempts = filter(lambda s: s.course_name==course and s.grade>0, attempts)
    course_students = map(lambda s: s.student_name, course_attempts)
    return sorted(course_students)

# reduce

# https://docs.python.org/3/library/functools.html#functools.reduce

# Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. 
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 
# The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. 
# If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. 
# If initializer is not given and iterable contains only one item, the first item is returned.

from functools import reduce

# Example 1
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])

# Example 2
my_list = [2, 3, 1, 5]

sum_of_numbers = reduce(lambda x, y: x + y, my_list, 0)
print(sum_of_numbers)

# Example 3
my_list = [2, 3, 1, 5]

product = reduce(lambda x, y: x * y, my_list, 1)
print(product)

# Example 4
my_list = [2, 3, 1, 5, 7, 10, 1, 0]

largest = reduce(lambda x, y: x if x > y else y, my_list)
print(largest)

# A third cornerstone function in this introduction to functional programming principles is `reduce`, from the `functools` module. 
# As the name implies, its purpose is to _reduce_ the items in a series into a single value.

# The `reduce` function starts with an operation and an initial value (aggregator - optionally given or taken as first item in list). 
# It performs the given operation on each item in the series in turn, so that the value changes at each step. 
# Once all items have been processed, the resulting value is returned.

# We have done summation of lists of integers in different ways before, but here we have an example with the help of the `reduce` function. 
# Notice the `import` statement; in Python versions 3 and higher it is necessary to access the `reduce` function. 
# In older Python versions the `import` statement was not needed, so you may come across examples without it online.

from functools import reduce

my_list = [2, 3, 1, 5]

sum_of_numbers = reduce(lambda reduced_sum, item: reduced_sum + item, my_list, 0)

print(sum_of_numbers)


# Let's take a closer look at what's happening here. 
# The `reduce` function takes three arguments: a function, a series of items, and an initial value. 
# In this case, the series is a list of integers, and as we are calculating a sum, a suitable initial value is zero.

# The first argument is a function, which represents the operation we want to perform on each item. 
# Here the function is an anonymous lambda function:
lambda reduced_sum, item: reduced_sum + item

# This function takes two arguments: the current reduced value (aggregator) and the item whose turn it is to be processed (next time on the iterable object). 
# These are used to calculate a new value for the reduced value. 
# In this case the new value is the sum of the old value and the current item.

# It may be easier to comprehend what the `reduce` function actually does if we use a normal named function instead of a lambda function. 
# That way we can also include helpful printouts:

from functools import reduce

my_list = [2, 3, 1, 5]

# a helper function for reduce, adds one value to the current reduced sum
def sum_helper(reduced_sum, item):
  print(f"the reduced sum is now {reduced_sum}, next item is {item}")
  # the new reduced sum is the old sum + the next item
  return reduced_sum + item

sum_of_numbers = reduce(sum_helper, my_list, 0)

print(sum_of_numbers)

# First, the function takes care of the item with value 2. 
# To begin with, the reduced sum is 0, which is the initial value passed to the `reduce` function. 
# The function calculates and returns the sum of these two: `0 + 2 = 2`.

# This is the value stored in `reduced_sum` as the `reduce` function processes the next item on the list, with value 3. 
# The function calculates and returns the sum of these two: `2 + 3 = 5`. 
# This result is then used when processing the next item, and so forth, and so forth.

# Now, summation is simple, as there is even the built-in `sum` function for this purpose. 
# But how about multiplication? Only minor changes are needed to create a reduced product:

from functools import reduce

my_list = [2, 2, 4, 3, 5, 2]

product_of_list = reduce(lambda product, item: product * item, my_list, 1)

print(product_of_list)

# As we are dealing with multiplication the initial value is not zero. 
# Instead, we use 1. What would happen if we used 0 as the initial value?

# Above we have dealt largely with integers, but `map`, `filter` and `reduce` can all handle a collection of objects of any type.

# As an example, let's generate a sum total of the balances of all accounts in a bank, with the help of `reduce`:

class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float):
        self.__account_number = account_number
        self.name = name
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

a1 = BankAccount("123456", "Randy Riches", 5000)
a2 = BankAccount("12321", "Paul Pauper", 1)
a3 = BankAccount("223344", "Mary Millionaire ", 1000000)

accounts = [a1, a2, a3]

from functools import reduce

def balance_sum_helper(balance_sum, account):
  return balance_sum + account.get_balance()

balances_total = reduce(balance_sum_helper, accounts, 0)

print("The total of the bank's balances:")
print(balances_total)

# The above can also be implemented with an anonymous/lambda function as such:
balances_total = reduce(lambda x, y: x + y.get_balance(), accounts, 0)

print("The total of the bank's balances:")
print(balances_total)

# Here the initial value argument for the reduce function is compulsory as each individual object needs to call the method "get_balance()". 
# Such a method call cannot be made from the aggregator variable in the lambda function as the object does not belong to the item's class once aggregated.

# Similarly, the `balance_sum_helper` function grabs the balance of each bank account, with the method dedicated for the purpose in the `BankAccount` class definition:
def balance_sum_helper(balance_sum, account):
  return balance_sum + account.get_balance()

# Hint: Reduce without an initial value

# You do not need to always pass a third argument to the `reduce` function. 
# For instance, summation would work just as well _without_ the initial value:
my_list = [2, 3, 1, 5]

sum_of_numbers = reduce(lambda reduced_sum, item: reduced_sum + item, my_list)

print(sum_of_numbers)

# If the initial value is left out, `reduce` takes the first item in the list as the initial value and starts reducing from the second item onwards.

# **NB:** if the items in the series are of a different type than the intended reduced result, the third argument is mandatory. 
# The example with the bank accounts would not work without the initial value. That is, trying this
balances_total = reduce(balance_sum_helper, accounts)

# produces the following error.
'''
TypeError: unsupported operand type(s) for +: 'BankAccount' and 'int'
'''

# In the above case, when `reduce` tries to execute the `balance_sum_helper` function for the first time, the arguments it uses are the _two first items in the list_, which are both of type BankAccount. 
# Specifically, the value assigned to the parameter `balance_sum` is the first item in the list.  
# The `balance_sum_helper` function tries to add an integer value to it, but adding an integer directly to a BankAccount object is not a supported operation.

# However, If we implement the `__add__` method within our class definition, the addition operator `+` becomes available on our BankAccount objects.
# This method now makes available the addition operation to any instance of the BankAccount object with any number.  
# The function placed within the reduce function first obtains the balance from the initial object in the list, places it in the aggregator and subsequently increases the aggregator with each object on the list.
class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float):
        self.__account_number = account_number
        self.name = name
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def __add__(self, amount: int):
        return self.__balance + amount

a1 = BankAccount("123456", "Randy Riches", 5000)
a2 = BankAccount("12321", "Paul Pauper", 1)
a3 = BankAccount("223344", "Mary Millionaire ", 1000000)

accounts = [a1, a2, a3]

from functools import reduce

balances_total = reduce(lambda x, y: x + y.get_balance(), accounts)

print("The total of the bank's balances:")
print(balances_total)

# Study credits

# In this exercise we will work with a slightly modified version of the `CourseAttempt` class. 
# The name of the student is omitted, but the number of credits is included. The class works as follows:
from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
    
attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
print(attempt)
print(attempt.course_name)
print(attempt.credits)
print(attempt.grade)

# Part 1 - The sum of all credits
# Please implement a function named `sum_of_all_credits` which takes a list of course attempts as its argument. 
# The function sums up the total number of study credits covered by the courses. 

def sum_of_all_credits(credit_list: list[CourseAttempt]):
    return reduce(lambda x, y: x + y.credits, credit_list, 0)

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_all_credits([s1, s2, s3])
print(credit_sum)

# Part 2 - The sum of passed credits
# Please implement a function named `sum_of_passed_credits` which takes a list of course attempts as its argument. 
# The function sums up the credits for the course attempts with grade 1 or above. 

# With only reduce function
def sum_of_passed_credits(credit_list: list[CourseAttempt]):
    return reduce(lambda x, y: x + y.credits if y.grade > 0 else x, credit_list, 0)

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_passed_credits([s1, s2, s3])
print(credit_sum)

# With reduce and filter
def sum_of_passed_credits(credit_list: list[CourseAttempt]):
    return reduce(lambda x, y: x + y.credits, filter(lambda x: x.grade > 1, credit_list), 0)

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_passed_credits([s1, s2, s3])
print(credit_sum)

# Part 3 - Average grade for passed courses

# Please implement a function named `average` which takes a list of course attempts as its argument. 
# The function calculates the average grade for the course attempts with grade 1 or above.

def average(credit_list: list[CourseAttempt]):
    passed_grades = list(filter(lambda x: x.grade > 0, credit_list))
    sum_of_passed_grades = reduce(lambda x, y: x + y.grade, passed_grades, 0)
    return sum_of_passed_grades / len(passed_grades)

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
ag = average([s1, s2, s3])
print(ag)


# Study credits - Approach 2

from functools import reduce
 
class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits
 
    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
 
def credit_summer(cr_sum, attempt):
    return cr_sum + attempt.credits
 
def sum_of_all_credits(attempts: list):
    return reduce(credit_summer, attempts, 0)
 
def sum_of_passed_credits(attempts: list):
    accepted = filter(lambda s: s.grade > 0, attempts)
    return reduce(credit_summer, accepted, 0)
 
def average(attempts: list):
    def grade_summer(cr_sum, attempt):
        return cr_sum + attempt.grade 
 
    accepted = list(filter(lambda s: s.grade > 0, attempts))
    sum_of_grades = reduce(grade_summer, accepted, 0)
 
    return sum_of_grades / len(accepted)