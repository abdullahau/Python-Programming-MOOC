# Object oriented programming techniques

# A class can contain a method which returns an object of the very same class.
 
# For example, below we have the class `Product`, 
# whose method `product_on_sale` returns a new Product object with the same name as the original but with a price which is 25 % lower:

class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    def product_on_sale(self):
        on_sale = Product(self.__name, self.__price * 0.75)
        return on_sale

apple1 = Product("Apple", 2.99)
apple2 = apple1.product_on_sale()
print(apple1)
print(apple2)

# Let's review the purpose of the variable `self`: within a class definition it refers to the object itself. 
# Typically it is used to refer to the object's own traits, its attributes and methods. 
# The variable can be used to refer to the entire object as well, 
# for example if the object itself needs to be returned to the client code. 

# In the example below we've added the method `cheaper` to the class definition. 
# It takes another Product as its argument and returns the cheaper of the two:
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def cheaper(self, Product):
        if self.__price < Product.price:
            return self
        else:
            return Product

apple = Product("Apple", 2.99)
orange = Product("Orange", 3.95)
banana = Product("Banana", 5.25)

print(orange.cheaper(apple))
print(orange.cheaper(banana))

# While this works just fine, it is a very specialised case of comparing two objects. 
# It would be better if we could use the Python comparison operators directly on these `Product` objects.

# Overloading operators

# Python contains some specially named built-in methods for working with the standard arithmetic and comparison operators. 
# The technique is called _operator overloading_. 
# If you want to be able to use a certain operator on instances of self-defined classes, you can write a special method which returns the correct result of the operator. 
# We have already used this technique with the `__str__` method: Python knows to look for a method named like this when a string representation of an object is called for.

# Let's start with the operator `>` which tells us if the first operand is greater than the second. 
# The `Product` class definition below contains the method `__gt__`, which is short for *g*reater *t*han. 
# This specially named method should return the correct result of the comparison. 
# Specifically, it should return `True` if and only if the current object is greater than the object passed as an argument. 
# The criteria used can be determined by the programmer. 
# By _current object_ we mean the object on which the method is called with the dot `.` notation.

class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def __gt__(self, another_product):
        return self.price > another_product.price

# In the implementation above, the method `__gt__` returns `True` if the price of the current product is greater than the price of the product passed as an argument. 
# Otherwise the method returns `False`.

# Now the comparison operator `>` is available for use with objects of type Product:

orange = Product("Orange", 2.90)
apple = Product("Apple", 3.95)

if orange > apple:
    print("Orange is greater")
else:
    print("Apple is greater")

if apple > orange:
    print("Apple is greater")
else:
    print("Orange is greater")

# As stated above, it is up to the programmer to determine the criteria by which it is decided which is greater and which is lesser. 
# We could, for instance, decide that the order should not be based on price, but be alphabetical by name instead. 
# This would mean that `orange` would now be "greater than" `apple`, as "orange" comes alphabetically last.

class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    def __gt__(self, another_product):
        return self.name > another_product.name

orange = Product("Orange", 4.90)
apple = Product("Apple", 3.95)

if orange > apple:
    print("Orange is greater")
else:
    print("Apple is greater")

if apple > orange:
    print("Apple is greater")
else:
    print("Orange is greater")

# More operators

# Here we have a table containing the standard comparison operators, along with the methods which need to be implemented if we want to make them available for use on our objects:

# Operator | Traditional meaning     | Name of method
# :-------:|:-----------------------:|:-----------------------:
# `<`      | Less than               | `__lt__(self, another)`
# `>`      | Greater than            | `__gt__(self, another)`
# `==`     | Equal to                | `__eq__(self, another)`
# `!=`     | Not equal to            | `__ne__(self, another)`
# `<=`     | Less than or equal to   | `__le__(self, another)`
# `>=`     | Greter than or equal to | `__ge__(self, another)`

# You can also implement some other operators, including the following arithmetic operators:

# Operator | Traditional meaning              | Name of method
# :------ :|:--------------------------------:|:------------------------------:
# `+`      | Addition                         | `__add__(self, another)`
# `-`      | Subtraction                      | `__sub__(self, another)`
# `*`      | Multiplication                   | `__mul__(self, another)`
# `/`      | Division (floating point result) | `__truediv__(self, another)`
# `//`     | Division (integer result)        | `__floordiv__(self, another)`

# More operators and method names are easily found online. 
# Remember also the `dir` command for listing the methods available for use on a given object.

# It is very rarely necessary to implement all the arithmetic and comparison operators in your own classes. 
# For example, division is an operation which rarely makes sense outside numerical objects. 
# What would be the result of dividing a Student object by three, or by another Student object? 
# Nevertheless, some of these operators are often very useful with also your own classes. 
# The selection of methods to implement depends on what makes sense, knowing the properties of your objects.

# Let's have a look at a class which models a single note. 
# If we implement the `__add__` method within our class definition, the addition operator `+` becomes available on our Note objects:

from datetime import datetime

class Note:
    def __init__(self, entry_date: datetime, entry: str):
        self.entry_date = entry_date
        self.entry = entry

    def __str__(self):
        return f"{self.entry_date}: {self.entry}"

    def __add__(self, another):
        # The date of the new note is the current time
        new_note = Note(datetime.now(), "")
        new_note.entry = self.entry + " and " + another.entry
        return new_note

entry1 = Note(datetime(2016, 12, 17), "Remember to buy presents")
entry2 = Note(datetime(2016, 12, 23), "Remember to get a tree")

# These notes can be added together with the + operator
# This calls the  __add__ method in the Note class
both = entry1 + entry2
print(both)
print(entry1)
print(entry2)

# A string representation of an object

# You have already implemented quite a few `__str__` methods in your classes. 
# As you know, the method returns a string representation of the object. 
# Another quite similar method is `__repr__` which returns a _technical_ representation of the object. 
# The method `__repr__` is often implemented so that it returns the program code which can be executed to return an object with _identical contents_ to the current object. (like a logger)

# The function `repr` returns this technical string representation of the object. 
# The technical representation is used also whenever the `__str__` method has not been defined for the object. 
# The example below will make this clearer:

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"

person1 = Person("Anna", 25)
person2 = Person("Peter", 99)
print(person1)
print(person2)

# Notice how the `__repr__`  method itself uses the `repr` function to retrieve the technical representation of the string. 
# This is necessary to include the `'` characters in the result.

# The following class has definitions for both `__repr__` and `__str__`:
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"

    def __str__(self):
        return f"{self.name} ({self.age} years)"

Person = Person("Anna", 25)
print(Person)
print(repr(Person))

# It is worth mentioning that with data structures, such as lists, Python always uses the `__repr__` method for the string representation of the contents. 
# This can sometimes look a bit baffling:
persons = []
persons.append(Person("Anna", 25))
persons.append(Person("Peter", 99))
persons.append(Person("Mary", 55))
print(persons)


# Example 2
class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):        
        return self.name.split()[-1]    

    def giveRaise(self, percent):
        self.pay = float(self.pay * (1 + percent))

    def __repr__(self): # or __str__
        return '[Person: %s, %s]' % (self.name, self.pay)

sue = Person('Sue Jones', job = 'dev', pay = 100000)
print(sue.name, sue.pay)

sue.giveRaise(.10)      # instead of hardcoding
print('$%0.2f'% sue.pay)

print(sue)

# Money

# The exercise template contains an outline for a class named `Money`. 
# This exercise asks you to implement some additional methods and to fix some small problems in the template.

class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros}.{self.cents:02f}"
    
# Part 1: Fix the string representation

# The `__str__` method in the class definition doesn't work quite right. 

class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros}.{self.cents:02d} eur"

e1 = Money(4, 10)
e2 = Money(2, 5)  # two euros and five cents

print(e1)
print(e2)

# Part 2: Equal amounts

# Please define a new method named `__eq__(self, another)` which allows you to use the `==` comparison operator on Money objects. 

class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self) -> str:
        return f"{self.euros}.{self.cents:02d} eur"
    
    def __eq__(self, another: 'Money') -> bool:
        return (self.euros + (self.cents / 100)) == (another.euros + (another.cents / 100))

e1 = Money(4, 10)
e2 = Money(2, 5)
e3 = Money(4, 10)

print(e1)
print(e2)
print(e3)
print(e1 == e2)
print(e1 == e3)

# Part 3: Other comparison operators

# Please implement the appropriate methods for the comparison operators `<`, `>` and `!=`.
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents
        self.total = self.euros + (self.cents / 100)

    def __str__(self) -> str:
        return f"{self.euros}.{self.cents:02d} eur"
    
    def __eq__(self, another: 'Money') -> bool:
        return self.total == another.total
    
    def __lt__(self, another: 'Money') -> bool:
        return self.total < another.total
    
    def __gt__(self, another: 'Money') -> bool:
        return self.total > another.total
    
    def __ne__(self, another: 'Money') -> bool:
        return self.total != another.total
    

e1 = Money(4, 10)
e2 = Money(2, 5)

print(e1 != e2)
print(e1 < e2)
print(e1 > e2)

# Part 4: Addition and subtraction

# Please implement the addition and subtraction operators `+` and `-` for Money objects. 
# Both should return a new object of type Money. 
# Neither the object itself nor the object passed as an argument should be changed as a result.

# NB: the value of a Money object cannot be negative. 
# If an attempt to subtract would result in a negative result, the method should raise a `ValueError` exception.
from decimal import *

class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents
        self.total = self.euros + (self.cents / 100)

    def __str__(self) -> str:
        return f"{self.euros}.{self.cents:02d} eur"
    
    def __eq__(self, another: 'Money') -> bool:
        return self.total == another.total
    
    def __lt__(self, another: 'Money') -> bool:
        return self.total < another.total
    
    def __gt__(self, another: 'Money') -> bool:
        return self.total > another.total
    
    def __ne__(self, another: 'Money') -> bool:
        return self.total != another.total
    
    def __add__(self, another: 'Money') -> 'Money':
        getcontext().prec = 2
        total = self.total + another.total
        euros = int(total)
        cents = int((Decimal(total) - Decimal(euros)) * 100)
        return Money(euros, cents)
    
    def __sub__(self, another: 'Money') -> 'Money':
        total = self.total - another.total
        if total >= 0:
            getcontext().prec = 2
            euros = int(total)
            cents = int((Decimal(total) - Decimal(euros)) * 100)
            return Money(euros, cents)
        else:
            raise ValueError("a negative result is not allowed")


e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2-e1

# Part 4: Approach 2
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents
        self.total = self.euros + (self.cents / 100)

    def __str__(self) -> str:
        return f"{self.euros}.{self.cents:02d} eur"
    
    def __eq__(self, another: 'Money') -> bool:
        return self.total == another.total
    
    def __lt__(self, another: 'Money') -> bool:
        return self.total < another.total
    
    def __gt__(self, another: 'Money') -> bool:
        return self.total > another.total
    
    def __ne__(self, another: 'Money') -> bool:
        return self.total != another.total
    
    def __add__(self, another: 'Money') -> 'Money':
        total_cents = self.cents + another.cents
        total_euros = self.euros + another.euros
        if total_cents >= 100:
            total_euros += 1
            total_cents -= 100
        return Money(total_euros, total_cents)
    
    def __sub__(self, another: 'Money') -> 'Money':
        total_euros = self.euros - another.euros
        total_cents = self.cents - another.cents
        if (total_cents < 0 and total_euros == 0) or total_euros < 0:
            raise ValueError("a negative result is not allowed")
        else:
            if total_cents < 0:
                total_cents += 100
                total_euros -= 1
            return Money(total_euros, total_cents)

e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2-e1

# https://peps.python.org/pep-0484/#forward-references -> Forward references are used when a type hint contains names that have not been defined yet 
# A situation where this occurs commonly is the definition of a container class, where the class being defined occurs in the signature of some of the methods.

# Part 5: The value must not be directly accessible

# The class still has a small integrity issue. 
# The user can "cheat" by accessing the attributes directly and changing the value stored in the Money object:
# Please encapsulate the implementation of the attributes defined in the class so that the cheat used above is not possible. 
# The class should have no public attributes, and no getter or setter methods for the euros or the cents.

class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__total = self.__euros + (self.__cents / 100)

    def __str__(self) -> str:
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, another: 'Money') -> bool:
        return self.__total == another.__total
    
    def __lt__(self, another: 'Money') -> bool:
        return self.__total < another.__total
    
    def __gt__(self, another: 'Money') -> bool:
        return self.__total > another.__total
    
    def __ne__(self, another: 'Money') -> bool:
        return self.__total != another.__total
    
    def __add__(self, another: 'Money') -> 'Money':
        total_cents = self.__cents + another.__cents
        total_euros = self.__euros + another.__euros
        if total_cents >= 100:
            total_euros += 1
            total_cents -= 100
        return Money(total_euros, total_cents)
    
    def __sub__(self, another: 'Money') -> 'Money':
        total_euros = self.__euros - another.__euros
        total_cents = self.__cents - another.__cents
        if (total_cents < 0 and total_euros == 0) or total_euros < 0:
            raise ValueError("a negative result is not allowed")
        else:
            if total_cents < 0:
                total_cents += 100
                total_euros -= 1
            return Money(total_euros, total_cents)
        
# ⭐ ⭐ ⭐ Money - Approach 2 
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
 
    def __str__(self):
        # f-string has a handy feature for adding leading zeros:
        # :02d for example means, that output has at least 2 digit
        return f"{self.__euros}.{self.__cents:02d} eur"
 
    # Helper method for returning the value in cents
    # --> makes the comparisons easier
    def __value(self):
        return self.__euros * 100 + self.__cents
 
    # Another helper method which converts cents to value
    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100
 
    def __eq__(self, other: "Money"):
        return self.__value() == other.__value()
 
    def __lt__(self, other: "Money"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "Money"):
        return self.__value() > other.__value()
 
    def __ne__(self, other: "Money"):
        return self.__value() != other.__value()
 
    def __add__(self, other: "Money"):
        msum = Money(0,0)
        msum.__set_value(self.__value() + other.__value())
        return msum
 
    def __sub__(self, other: "Money"):
        difference = self.__value() - other.__value()
        if difference < 0:
            raise ValueError("a negative result is not allowed")
        dmoney = Money(0,0)
        dmoney.__set_value(self.__value() - other.__value())
        return dmoney
    
# Simple date - Approach 1

# In this exercise you are asked to implement the class `SimpleDate` which allows you to handle dates. 
# For simplicity's sake we assume here that _each month has 30 days_.

# Because of this simplification you should not use the `datetime` module from the Python standard library. 
# You will implement similar functionality by yourself instead.

# Part 1: Comparisons

# Please implement the outline of the class, along with methods allowing for comparisons with the operators `<`, `>`, `==` and `!=`. 
# You can use the following code to test your implementation:

class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year
        self.__days = (self.__year * 360) + (self.__month * 30) + self.__date
        
    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"
    
    def __lt__(self, another: 'SimpleDate') -> bool:
        return self.__days < another.__days
    
    def __gt__(self, another: 'SimpleDate') -> bool:
        return self.__days > another.__days
    
    def __eq__(self, another: 'SimpleDate') -> bool:
        return self.__days == another.__days
    
    def __ne__(self, another: 'SimpleDate') -> bool:
        return self.__days != another.__days
        
d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)
d3 = SimpleDate(28, 12, 1985)

print(d1)
print(d2)
print(d1 == d2)
print(d1 != d2)
print(d1 == d3)
print(d1 < d2)
print(d1 > d2)

# Part 2: Increment

# Please implement the addition operator `+` which allows you to add a given number of days to a SimpleDate object.
# The operator should return a new SimpleDate object. The original object should not be changed.

class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year
        
    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"
    
    def __date_to_days(self) -> int:
        return ((self.__year - 1) * 360) + ((self.__month - 1) * 30) + (self.__date - 1)
    
    def __days_to_date(self, days: int) -> "SimpleDate":
        year_cal, remainder = divmod(days, 360)
        month_cal, day_cal = divmod(remainder, 30)
        return day_cal+1, month_cal+1, year_cal+1        
    
    def __lt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() < another.__date_to_days()
    
    def __gt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() > another.__date_to_days()
    
    def __eq__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() == another.__date_to_days()
    
    def __ne__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() != another.__date_to_days()
    
    def __add__(self, days: int) -> 'SimpleDate':
        current_date = self.__date_to_days() + days
        date = self.__days_to_date(current_date)
        return SimpleDate(date[0], date[1], date[2])
    
    def __sub__(self, another: 'SimpleDate') -> 'SimpleDate':
        current_date = self.__date_to_days() - another.__date_to_days()
        return current_date

d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)

d3 = d1 + 3
d4 = d2 + 400

print(d1)
print(d2)
print(d3)
print(d4)

# Days to date conversion
date = 30
month = 12
year = 2024

days = (date - 1) + ((month - 1) * 30) +  ((year - 1) * 360)

year_cal, remainder = divmod(days, 360)
month_cal, day_cal = divmod(remainder, 30)

print(f"{day_cal+1}/{month_cal+1}/{year_cal+1}")

# Part 3: Difference
# Please implement the subtraction operator `-` which allows you to find out the difference in days between two SimpleDate objects. 
# As we assumed each month to have 30 days, a year within the confines of this exercise is 12*30 = 360 days long.

class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year
        
    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"
    
    def __date_to_days(self) -> int:
        return ((self.__year - 1) * 360) + ((self.__month - 1) * 30) + (self.__date - 1)
    
    def __days_to_date(self, days: int) -> "SimpleDate":
        year_cal, remainder = divmod(days, 360)
        month_cal, day_cal = divmod(remainder, 30)
        return day_cal+1, month_cal+1, year_cal+1        
    
    def __lt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() < another.__date_to_days()
    
    def __gt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() > another.__date_to_days()
    
    def __eq__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() == another.__date_to_days()
    
    def __ne__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() != another.__date_to_days()
    
    def __add__(self, days: int) -> 'SimpleDate':
        current_date = self.__date_to_days() + days
        date = self.__days_to_date(current_date)
        return SimpleDate(date[0], date[1], date[2])
    
    def __sub__(self, another: 'SimpleDate') -> 'SimpleDate':
        current_date = self.__date_to_days() - another.__date_to_days()
        return abs(current_date)

d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(2, 11, 2020)
d3 = SimpleDate(28, 12, 1985)

print(d2-d1)
print(d1-d2)
print(d1-d3)

# Simple Date - Approach 2
class SimpleDate:
    def __init__(self, pv: int, month: int, year: int):
        self.__pv = pv
        self.__month = month
        self.__year = year
 
    def __str__(self):
        return f'{self.__pv}.{self.__month}.{self.__year}'
 
    # Comparisons are easier, when date is converted to days
    def __value(self):
        return self.__year * 360 + self.__month * 30 + self.__pv
 
    # Converst days back to date
    def __to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)
 
    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()
 
    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()
        
    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()
 
    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)
 
    def __sub__(self, other: "SimpleDate"):
        # abs(x) returns the absolute value of x
        return abs(self.__value() - other.__value())

# Above Class fails the Below Test
dec = SimpleDate(29,12,2023)
dec_end = dec + 1
print(dec_end)
    
# ⭐ ⭐ ⭐ Simple Date - Approach 3
class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year
        
    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"
    
    def __date_to_days(self) -> int:
        return ((self.__year - 1) * 360) + ((self.__month - 1) * 30) + (self.__date - 1)
    
    def __days_to_date(self, days: int) -> "SimpleDate":
        year_cal, remainder = divmod(days, 360)
        month_cal, day_cal = divmod(remainder, 30)
        return SimpleDate(day_cal+1, month_cal+1, year_cal+1)     
    
    def __lt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() < another.__date_to_days()
    
    def __gt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() > another.__date_to_days()
    
    def __eq__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() == another.__date_to_days()
    
    def __ne__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() != another.__date_to_days()
    
    def __add__(self, days: int) -> 'SimpleDate':
        return self.__days_to_date(self.__date_to_days() + days)
    
    def __sub__(self, another: 'SimpleDate') -> 'SimpleDate':
        current_date = self.__date_to_days() - another.__date_to_days()
        return abs(current_date)

d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(2, 11, 2020)
d3 = SimpleDate(28, 12, 1985)

print(d2-d1)
print(d1-d2)
print(d1-d3)

# Iterators

# We know that the `for` statement can be used to _iterate_ through many different data structures, files and collections of items. 
# A typical use case would be the following function:
def count_positives(my_list: list):
    n = 0
    for item in my_list:
        if item > 0:
            n += 1
    return n

# The function goes through the items in the list one by one, and keeps track of how many of the items were positive.

# It is possible to make your own classes iterable, too. 
# This is useful when the core purpose of the class involves storing a collection of items. 
# The Bookshelf class from a previous example would be a good candidate, as it would make sense to use a `for` loop to go through the books on the shelf. 
# The same applies to, say, a student register.
# Being able to iterate through the collection of students could be useful.

# To make a class iterable you must implement the iterator methods `__iter__` and  `__next__`. 
# We will return to the specifics of these methods after the following example:

class Book:
    def __init__(self, name: str, author: str, page_count: int):
        self.name = name
        self.author = author
        self.page_count = page_count

class Bookshelf:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    # This is the iterator initialization method
    # The iteration variable(s) should be initialized here
    def __iter__(self):
        self.n = 0
        # the method returns a reference to the object itself as 
        # the iterator is implemented within the same class definition
        return self

    # This method returns the next item within the object
    # If all items have been traversed, the StopIteration event is raised
    def __next__(self):
        if self.n < len(self._books):
            # Select the current item from the list within the object
            book = self._books[self.n]
            # increase the counter (i.e. iteration variable) by one
            self.n += 1
            # return the current item
            return book
        else:
            # All books have been traversed
            raise StopIteration

# The method `__iter__` initializes the iteration variable or variables. 
# In this case it suffices to have a simple counter containing the index of the current item in the list. 
# We also need the method `__next__`, which returns the next item in the iterator. 
# In the example above the method returns the item at index `n` from the list within the Bookshelf object, and the iterator variable is also incremented. 

# When all objects have been traversed, the `__next__` method raises the `StopIteration` exception. 
# The process is no different from raising any other exceptions, but this exception is automatically 
# handled by Python and its purpose is to signal to the code calling the iterator (e.g. a `for` loop) that the iteration is now over.

# Our Bookshelf is now ready for iteration, for example with a `for` loop:
if __name__ == "__main__":
    b1 = Book("The Life of Python", "Montague Python", 123)
    b2 = Book("The Old Man and the C", "Ernest Hemingjavay", 204)
    b3 = Book("A Good Cup of Java", "Caffee Coder", 997)

    shelf = Bookshelf()
    shelf.add_book(b1)
    shelf.add_book(b2)
    shelf.add_book(b3)

    # Print the names of all the books
    for book in shelf:
        print(book.name)

# An iterable shopping list

# The exercise template contains the `ShoppingList` class from the exercise in part 8. 
# Please adjust the class so that it is iterable.
# The `__next__` method of your iterator should return tuples, where the first item is the name of the product and the second item is the amount.

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
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < len(self.products):
            item = self.products[self.n]
            self.n += 1
            return item
        else:
            raise StopIteration

def total_units(my_list: ShoppingList):
    total = sum(my_list.amount(i) for i in range(1, my_list.number_of_items()+1))
    return total

shopping_list = ShoppingList()
shopping_list.add("bananas", 10)
shopping_list.add("apples", 5)
shopping_list.add("pineapple", 1)

for product in shopping_list:
    print(f"{product[0]}: {product[1]} units")