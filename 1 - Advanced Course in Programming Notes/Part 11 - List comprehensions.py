# List comprehensions

# One of the situations where programming is at its most powerful is processing sequences of items and events. 
# Computers are good at repeating things. 
# For example, in the previous parts of this material we have been iterating over strings, lists and dictionaries in various ways.

# Let's assume we have a list of integers, and we would need the same list of items in string format. 
# A traditional way of completing the task could look like this:
numbers = [1, 2, 3, 6, 5, 4, 7]

strings = []
for number in numbers:
    strings.append(str(number))

# List Comprehension Method
numbers = [1, 2, 3, 6, 5, 4, 7]    
strings = [str(number) for number in numbers]
print(strings)

# List comprehensions

# There is also a more "pythonic" way of generating lists from existing lists. 
# These are called _list comprehensions_.

# The idea is to fit on a single line both the description of what should be done to each item on the list, 
# and the assignment of the result to a new list.

# In the above example, the operation performed on each item on the list was very simple: 
# each integer was converted into a string. Let's see what this would look like implemented with a list comprehension:
numbers = [1, 2, 3, 6, 5, 4, 7]
strings = [str(number) for number in numbers]

# The second line above contains many of the same elements as the more traditional iterative apporach, but the syntax is different. 
# One way of generalising a list comprehension statement would be:
# `[<expression> for <item> in <series>]`

# The square brackets around the list comprehension statement signal to Python that the result should be a new list. 
# One by one, each item in the original list is processed, and the result is stored in the new list, just like in the iterative approach above. 
# As a result we have a new list with exactly as many items as were in the original, and all items have been processed in an identical fashion.

# List comprehensions can handle much more complicated operations as well. 
# We can perform calculations, such as multiplying the original items by ten:
numbers = list(range(1,10))
print(numbers)

numbers_multiplied = [number * 10 for number in numbers]
print(numbers_multiplied)

# In fact, the expression within the list comprehension statement can be any Python expression. 
# You can even call functions you've defined yourself:
def factorial(n: int):
    """ The function calculates the factorial n! for integers above zero """
    k = 1
    while n >= 2:
        k *= n
        n -= 1
    return k

if __name__ == "__main__":
    numbers = [5, 2, 4, 3, 0]
    factorials = [factorial(number) for number in numbers]
    print(factorials)
    
# With the more familiar `for` loop the same process could be expressed like this:
def factorial(n: int):
    """ The function calculates the factorial n! for integers above zero """
    k = 1
    while n >= 2:
        k *= n
        n -= 1
    return k

if __name__ == "__main__":
    numbers = [5, 2, 4, 3, 0]
    factorials = []
    for number in numbers:
        factorials.append(factorial(number))
    print(factorials)
    
# List comprehensions allow us to express the same functionality more consisely, usually without losing any of the readability.

# We can also return a list comprehension statement from a function directly. 
# If we needed a function for producing factorials for lists of numbers, we could achieve it very concisely:
def factorials(numbers: list):
    return [factorial(number) for number in numbers]

# Square roots

# Please write a function named `square_roots(numbers: list)` which takes a list of integers as its argument. 
# The function should return a new list containing the square roots of the original integers. 

# The function should use a list comprehension. 
# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

def square_roots(numbers: list):
    return [number ** (1/2) for number in numbers]

lines = square_roots([1,2,3,4])
for line in lines:
    print(line)
    
# Square roots - Approach 2
from math import sqrt
 
def square_roots(numbers: list):
    return [sqrt(number) for number in numbers]

# Rows of stars - Approach 1

# Please write a function named `rows_of_stars(numbers: list)` which takes a list of integers as its argument. 
# The function should return a new list containing rows of stars. 
# The length of each row should correspond to the integer at the same index in the original list. 
# The function should use a list comprehension to achieve this.

# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

def rows_of_stars(numbers: list):
    return ["*" * star for star in numbers]


rows = rows_of_stars([1,2,3,4])
for row in rows:
    print(row)

print()

rows = rows_of_stars([4, 3, 2, 1, 10])
for row in rows:
    print(row)
    
# Best exam result - Approach 1 (Change "Grade" attribute to list of integers)

# The exercise template contains the class definition `ExamResult`. 
# The class has the following public attributes:
'''
name
grade1
grade2
grade3
'''

class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade = [grade1, grade2, grade3]

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade[0]}' +
            f', grade2: {self.grade[1]}, grade3: {self.grade[2]}')

# Please write a function named `best_results(results: list)` which takes a list of ExamResult objects as its argument.

# The function should return a new list containing only the best result from each ExamResult object. 
# The function should use a list comprehension to achieve this.

# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

def best_results(results: list) -> list:
    return [max(result.grade) for result in results]

result1 = ExamResult("Peter",5,3,4)
result2 = ExamResult("Pippa",3,4,1)
result3 = ExamResult("Paul",2,1,3)
results = [result1, result2, result3]
print(best_results(results))

# Best exam result - Approach 2 (class with iterator method)
class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade_list = [grade1, grade2, grade3]

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')
        
    def __iter__(self):
      self.a = 0
      return self
    
    def __next__(self):
        if self.a <= len(self.grade_list)-1:
            grade = self.grade_list[self.a]
            self.a += 1
            return grade 
        else:
            raise StopIteration
        

def best_results(results: list) -> list:
    return [max([grade for grade in result]) for result in results]

result1 = ExamResult("Peter",5,3,4)
result2 = ExamResult("Pippa",3,4,1)
result3 = ExamResult("Paul",2,1,3)
results = [result1, result2, result3]
print(best_results(results))

# # Best exam result - Approach 3

class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
 
    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')
 
def best_results(result: list):
    return [max(s.grade1, s.grade2, s.grade3) for s in result]

# Lengths - Approach 1

# Please write a function named `lengths(lists: list)` which takes a list containing lists of integers as its argument. 
# The function should return a new list, containing the lengths of the lists within the argument list.

# The function should use a list comprehension to achieve this. 
# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

def lengths(lists: list) -> list:
    return [len(l) for l in lists]

lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
print(lengths(lists))

# Filtering items

# In the examples above all of our lists remained the same length before and after a list comprehension operation. 
# In each case, all the items in the original list were used as the basis of the new list. 
# But sometimes we only need _some_ of the original items. How can this be achieved?

# A list comprehension statement also allows for a condition, so that we can check the items against the condition and select only those which match. 
# The general syntax is as follows:
# `[<expression> for <item> in <series> if <Boolean expression>]`

# The statement above is otherwise identical to the general form introduced in the beginning of this section, 
# but now there is an if statement at the end.
# Only those items from the original list for which the Boolean expression is true are used as the basis of the new list.

# In the example below we select all the even items from the original list as the basis of the new list. 
# In fact, these items are not further processed in any way; they are assigned to the new list as is:
numbers = [1, 1, 2, 3, 4, 6, 4, 5, 7, 10, 12, 3]

even_items = [item for item in numbers if item % 2 == 0]
print(even_items)

# The expression in the list comprehension statement above is just a simple `item`, which means that no operations are to be performed on the items in the list. 
# The expression could be any Python expression, just like in the previous examples. 
# For example, the following list comprehension statement takes all the even items in a list, multiplies each by ten, and stores the result in a new list:
numbers = [1, 1, 2, 3, 4, 6, 4, 5, 7, 10, 12, 3]

even_items = [item * 10 for item in numbers if item % 2 == 0]
print(even_items)

# As you come across more and more complicated list comprehensions, 
# you may find it useful to try reading the condition first. 
# After all, the items are processed only if they pass the test, so it often makes sense to first figure out which items pass the filtering stage. 
# Sometimes the expression in a list comprehension statement would not even be possible for all the items in the original list.

# For example, the factorial operation is only defined for non-negative integers. 
# If we can't be sure a list only contains values of zero or above, the contents have to be filtered before passing them on to the factorial function we made before:
def factorial(n: int):
    """ The function calculates the factorial n! for integers above zero """
    k = 1
    while n >= 2:
        k *= n
        n -= 1
    return k

if __name__ == "__main__":
    numbers = [-2, 3, -1, 4, -10, 5, 1]
    factorials = [factorial(number) for number in numbers if number >= 0]
    print(factorials)

# As we saw in our very first list comprehension example, where integers were converted into strings, 
# the items in the new list do not have to be of the same type as the items in the original list. 
# Continuing from the factorial example above, we can create a tuple from each original item and its processed counterpart, 
# and store these in a list, combining everything we've learned so far in a single list comprehension statement:

def factorial(n: int):
    """ The function calculates the factorial n! for integers above zero """
    k = 1
    while n >= 2:
        k *= n
        n -= 1
    return k

if __name__ == "__main__":
    numbers = [-2, 3, 2, 1, 4, -10, 5, 1, 6]
    # the variable name abbreviated here so that this would be easier to read
    factorials = [(n, factorial(n)) for n in numbers if n > 0 and n % 2 == 0]
    print(factorials)

# Picking the above example apart, we have the Boolean expression `n > 0 and n % 2 == 0`. 
# This means that only items which are both positive and divisible by two are accepted for further processing from the original list. 

# These positive, even numbers are then each in turn processed into the format `(n, factorial(n))`. 
# This is a tuple, where the first item is the number itself, and the second item is the result returned by the factorial function.


# Remove smaller than

# Please write a function named `remove_smaller_than(numbers: list, limit: int)` which takes a list of integers and a limit value (also in integer format) as its arguments.

# The function should use a list comprehension to produce a new list without the values which are smaller than the limit value.

# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

def remove_smaller_than(numbers: list, limit: int) -> list:
    return [number for number in numbers if number >= limit]

numbers = [1,65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))

# Begin with a vowel - Approach 1

# Please write a function named `begin_with_vowel(words: list)` which takes a list of strings as its argument.

# The function should use a list comprehension technique to create and return a new list, containing only those words from the original list which begin with a vowel (a, e, i, o, u). 
# Both lowercase and uppercase letters should be accepted.

# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

def begin_with_vowel(words: list) -> list:
    return [word for word in words if word[0].lower() in "aeiou"]

word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)
    
# Alternative execution with list comprehensions

# Often when we have a conditional statement, we also include an `else` branch. 
# As we can use conditions in list comprehensions, the else branch is also available with list comprehensions. 
# The general syntax of the conditional used with list comprehensions looks like this:
# `<expression 1> if <condition> else <expression 2>`

# We came across these single line conditionals, or ternary operators, already in Par 7 - More Python features. 
# The expression above evaluates to either `expression 1` or `expression 2`, depending on whether the condition is true or false.

# As a refresher on the subject, if we needed to print out the larger of two numbers, and we wanted to use just a single print statement, we could fit it all on a single line:

number1 = int(input("Type in number 1:"))
number2 = int(input("Type in number 2:"))
print (number1 if number1 > number2 else number2)

# Combining the ternary operator syntax with a list comprehension statement yields the following general structure:
# `[<expression 1> if <condition> else <expression 2> for <item> in <series>]`

# This may look a little confusing, as the conditional structure now comes before the actual list comprehension part.
# This is just the way the syntax has been defined, at least at the moment. 
# If there is also an `else` branch, the conditional comes first. 
# If there is just an `if`, it goes to the end. You can try swapping them around and see what happens.

# Including an else operator means that we will again process every item from the original list.
# Depending on whether the condition is true or false, either `expression 1` or `expression 2` is performed on each item on the list.

# The following example checks if the items on a list are zero or above. 
# Any such item is accepted as is, but all negative items are negated, so that the sign is changed from negative to positive. 
# The result is a list containing the absolute values of the items in the original list.

numbers = [1, -3, 45, -110, 2, 9, -11]
abs_vals = [number if number >= 0 else -number for number in numbers]
print(abs_vals)

# Reiterating what happens above: if the condition `number >= 0` is true, the item undergoes expression `number`, and the result is the item itself. 
# If the condition is false, the item undergoes expression `-number`, so that it becomes positive in value.

# In the following example we have the function `string_lengths` which takes a list as its argument, and returns another list with the lengths of any strings in the original list. 
# This function is okay with list items of any type, however. If the item is a string, it calculates its length. If the item is anything else, it inserts -1 in the list it returns.

def string_lengths(my_list: list):
    """ The function returns the lengths of strings in a new list """
    return [len(item) if type(item) == str else -1 for item in my_list]

if __name__ == "__main__":
    test_list = ["hi", 3, True, "there", -123.344, "toodlepip", 2, False]
    lengths = string_lengths(test_list)
    print(lengths)
    
# Lottery numbers - Approach 1

# Part 1 - LotteryNumbers matched
# Please write a class named `LotteryNumbers` which takes the week number (an integer value) and a list of seven integers as its constructor arguments. 
# The list should contain the correct lottery numbers for the given week.

# Please also write a method named `number_of_hits(numbers: list)` which takes a list of integers as its argument. 
# The method returns the number of correct entries in the parameter list.

# The method should use a list comprehension to achieve this. 
# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

class LotteryNumbers:
    def __init__(self, week: int, lottery_numbers: list) -> None:
        self.__week = week
        self.__lottery_numbers = lottery_numbers
    
    def number_of_hits(self, numbers: list) -> int:
        return len([number for number in numbers if number in self.__lottery_numbers])
        

week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
my_numbers = [1,4,7,11,13,19,24]

print(week5.number_of_hits(my_numbers))

# Part 2: LotteryNumbers matched in place
# Please write a method named `hits_in_place(numbers)` which takes a list of seven integers as its argument, 
# and returns a new list of seven integers. 
# The new list contains only those items from the original list which match the week's correct numbers. 
# These must remain at the same indexes as they were in the original list. 
# The rest of the indexes should be filled with values `-1`.

# The method should use a list comprehension to achieve this. 
# The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

class LotteryNumbers:
    def __init__(self, week: int, lottery_numbers: list) -> None:
        self.__week = week
        self.__lottery_numbers = lottery_numbers
    
    def number_of_hits(self, numbers: list) -> int:
        return len([number for number in numbers if number in self.__lottery_numbers])
    
    def hits_in_place(self, numbers: list) -> list:
        return [numbers[i] if numbers[i] in self.__lottery_numbers else -1 for i in range(7)]


week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))

# Lottery numbers - Approach 2
class LotteryNumbers:
    def __init__(self, round: int, winning_numbers: list):
        self.round = round
        self.__winning_numbers = winning_numbers
 
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__winning_numbers])
 
    def hits_in_place(self, numbers: list):
        return [number if number in self.__winning_numbers else -1 for number in numbers]