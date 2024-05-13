# Classes and objects

# Lists, tuples, dictionaries and strings are rather special cases in Python programming. 
# Python syntax features a unique, pre-defined method of declaring an object belonging to each of these types:

# Lists are declared with square brackets
my_list = [1,2,3]

# Strings are declared with quotation marks
my_string = "Hi there!"

# Dictionaries are declared with curly brackets
my_dict = {"one": 1, "two:": 2}

# Tuples are declared with parentheses
my_tuple = (1,2,3)

# When some other type of object is declared, we need to call a special initialization function called a constructor.

# Let's have a look at working with fractions through the 'Fraction' class.
# we are using the class Fraction from the module fractions
from fractions import Fraction

# create some new fraactions
half = Fraction(1,2)

third = Fraction(1,3)

another = Fraction(3,11)

# print these out
print(half)
print(third)
print(another)

# Fractions can be added together, for example
print(half + third)

# Constructor method calls look a little different than the normal method calls we have come across before. 
# For one, they are not attached to any object with the dot notation (as the constructor call is needed to create an object in the first place). 
# The constructor method is also capitalized

# A class is the blueprint of an object

# In the example above we imported the 'Fraction' class from the module 'fractions'. 
# New fraction objects were created by calling the constructor method of the Fraction class.

# A class definition contains the structure and functionalities of any object which represents it.
# That is why classes are sometimes referred to as the blueprints of objects.
# So, a class definition tells you what kind of data an object contains, and defines also the methods which can be used on the object.
# Object oriented programming refers to a programming paradigm where the functionality of the program is tied into the use of classes and objects created based on them.

# A single class definition can be used to create multiple objects. 
# As mentioned before, objects are independent. Changes made to one object generally do not affect the other objects representing the same class. 
# Each object has its own unique set of data attributes. 

# It might be helpful to consider this simplification of the class-object relationship:
    # a class defines the variables
    # when an object is created, those variables are assigned values

# So, we can use an object of type 'Fraction' to access the numerator and denominator of a fractional number:
from fractions import Fraction

number = Fraction(2,5)

# Print the numerator
print(number.numerator)

# ...and the denominator
print(number.denominator)

# The Fraction class definition contains declarations for the variables numerator and denominator. 
# Each object created based on the class has its own specific values assigned to these variables.

# Similarly, objects created based on the date class each contain their own unique values for the year, month and day of the date:
from datetime import date

xmas_eve = date(2020, 12, 24)
midsummer = date(2020, 6, 20)

# print only the month attribute of both objects
print(xmas_eve.month)
print(midsummer.month)

# The 'date' class definition contains declarations of the 'year', 'month' and 'day' variables. 
# When a new 'date' object is created based on the class, these variables are assigned values. 
# Each object has its own unique values assigned to these variables.

# Functions which work with objects

# Passing an object as an argument to a function should be familiar by now.

# Here we have a function which checks if the 'date' object passed as an argument falls on a weekend:
def is_it_weekend(my_date: date):
    weekday = my_date.isoweekday()
    return weekday == 6 or weekday == 7

# This function uses the method 'isoweekday', which is defined in the 'date' class definition, 
# and returns an integer value so that if the date given is a Monday, it returns 1, and if it is a Tuesday, it returns 2, and so forth.
# https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday

# You can use the above function like this:
xmas_eve = date(2020, 12, 24)
midsummer = date(2020, 6, 20)

print(is_it_weekend(xmas_eve))
print(is_it_weekend(midsummer))

# Methods vs variables

# When working with an object of type 'date' you may notice there is a slight difference between 
# how the variables contained in the object are accessed, as opposed to how the methods attached to the objects are used:

my_date = date(2020, 12, 24)

# calling a method
weekday = my_date.isoweekday()

# accessing a variable
my_month = my_date.month

print("The day of the week:", weekday)
print("The month:", my_month)

# The day of the week the date falls on is available through the method 'isoweekday':
weekday = my_date.isoweekday()
# This is a method call, so there are parentheses after the name of the method. 
# Leaving the parentheses out does not cause an error, but the results are weird:
weekday =  my_date.isoweekday
print("The day of the week:", weekday)

# The month of a date object is a variable, so the value attached can be accessed with a reference.
my_month = my_date.month
# Notice there are no parentheses here. Adding parentheses would cause an error:
my_month = my_date.month()

# List of years - Approach 1
# Please write a function named list_years(dates: list) which takes a list of date type objects as its argument. 
# The function should return a new list, which contains the years in the original list in chronological order, from earliest to latest.
from datetime import date

def list_years(dates: list):
    sorted_years = []
    for i in range(len(dates)):
        sorted_years.append(dates[i].year)
    sorted_years.sort()
    return sorted_years

# List comprehension method
from datetime import date

def list_years(dates: list):
    sorted_years = [dates[i].year for i in range(len(dates))]
    sorted_years.sort()
    return sorted_years

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

dates = [date1, date2, date3]

print(list_years(dates))

# List of years - Approach 2
from datetime import date
 
def list_years(dates: list):
    years = []
    for dt in dates:
        years.append(dt.year)
 
    years.sort()
    return years

# Shopping list 
# The exercise template contains a pre-defined 'ShoppingList' class, which can be used to model a shopping list. 
# Your task is to add a method to the class definition. You do not need to change any methods already defined.

# Assuming we have a 'ShoppingList' object referenced in a variable named 'shopping_list', the object can be handled with the following methods:
print(shopping_list.number_of_items())
print(shopping_list.item(1))
print(shopping_list.amount(1))
print(shopping_list.item(2))
print(shopping_list.amount(2))

'''
2
Bananas
4
Milk
1
'''
# We can also do this:
# the items on the shopping list are indexed from 1
for i in range(1, shopping_list.number_of_items()+1):
    item = shopping_list.item(i)
    amount = shopping_list.amount(i)
    print(f"{item}: {amount} units")

'''
Bananas 4 units
Milk 1 units
'''

# As you can see, a 'ShoppingList' works a bit like a normal list, but it is accessed via the methods provided by the 'ShoppingList' class. 
# Unlike normal Python lists, indexing starts from 1, not 0.

# Please write a function named 'total_units(my_list: ShoppingList)', which takes a 'ShoppingList' type object as its argument. 
# The function should calculate the total number of units listed, and return the value.
if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))
    
'''
16
'''

# NB: the definition of the 'ShoppingList' class is already included in the exercise template. 
# You do not need to use an 'import' statement to import it, unlike in the examples above with the Python standard library classes 'Fraction' and 'date'.

# DO NOT CHANGE THE CODE OF THE CLASS
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]
    
# Shopping list - Approach 1
def total_units(my_list: ShoppingList):
    total = 0
    for i in range(1, my_list.number_of_items()+1):
        total += my_list.amount(i)
    return total

# Shopping list - Comprehension method
def total_units(my_list: ShoppingList):
    total = sum(my_list.amount(i) for i in range(1, my_list.number_of_items()+1))
    return total
