# Defining methods

# Classes which contain only data attributes are not very different from dictionaries. 
# Below you will find two ways to model a bank account, first with a class definition, and then using a dictionary.

# Example 1: bank account with class definition
class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)


# Example 2: bank account with dictionary
peters_account = {"account_number": "12345-678", "owner": "Peter Python", "balance": 1500.0, "annual_interest": 0.0}

# With a dictionary the implementation is much shorter and more straightforward.
# With a class, however, the structure is more "tightly bound", so that we can expect all 'BankAccount' objects to be structurally alike.
# A class is also named. The 'BankAccount' class is referenced when creating a new bank account, and the type of the object is 'BankAccount', not 'dict'.

# Another significant advantage of classes is that in addition to data, they can contain functionality. 
# One of the guiding principles of object oriented programming is that an object is used to access both the data attached to an object and the functionality to process that data.

# Methods in classes

# A method is a subprogram or function that is bound to a specific class. 
# Usually a method only affects a single object. 
# A method is defined within the class definition, and it can access the data attributes of the class just like any other variable.

# Let's continue with the 'BankAccount' class introduced above. 
# Below we have a new method which adds interest to the account:
class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

    # This method adds the annual interest to the balance of the account
    def add_interest(self):
        self.balance += self.balance * self.annual_interest


peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
peters_account.add_interest()
print(peters_account.balance)

# The 'add_interest' method multiplies the balance of the account by the annual interest percentage, and then adds the result to the current balance. 
# The method acts only on the object which it is called on.

# Let's see how this works when we have created multiple instances of the class:

# The class BankAccount is defined in the previous example

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
paulas_account = BankAccount("99999-999", "Paula Pythonen", 1500.0, 0.05)
pippas_account = BankAccount("1111-222", "Pippa Programmer", 1500.0, 0.001)

# Add interest on Peter's and Paula's accounts, but not on Pippa's
peters_account.add_interest()
paulas_account.add_interest()

# Print all account balances
print(peters_account.balance)
print(paulas_account.balance)
print(pippas_account.balance)

# As you can see above, the annual interest is added only to those accounts which the method is called on. 
# As the annual interest rates are different for Peter's and Paula's accounts, the results are different for these two accounts. 
# The balance on Pippa's account does not change, because the 'add_interest' method is not called on the object 'pippas_account'.

# Encapsulation

# In object oriented programming the word client comes up from time to time. 
# This is used to refer to a section of code which creates an object and uses the service provided by its methods. 
# When the data contained in an object is used only through the methods it provides, the internal integrity of the object is guaranteed. 
# In practice this means that, for example, a 'BankAccount' class offers methods to handle the 'balance' attribute, so the balance is never accessed directly by the client. 
# These methods can then verify that the balance is not allowed to go below zero, for instance.

# An example of how this would work:
class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

    # This method adds the annual interest to the balance of the account
    def add_interest(self):
        self.balance += self.balance * self.annual_interest

    # This method "withdraws" money from the account
    # If the withdrawal is successful the method returns True, and False otherwise
    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True

        return False

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)

if peters_account.withdraw(1000):
    print("The withdrawal was successful, the balance is now", peters_account.balance)
else:
    print("The withdrawal was unsuccessful, the balance is insufficient")

# Let's try again
if peters_account.withdraw(1000):
    print("The withdrawal was successful, the balance is now", peters_account.balance)
else:
    print("The withdrawal was unsuccessful, the balance is insufficient")

# Maintaining the internal integrity of the object and offering suitable methods to ensure this is called encapsulation. 
# The idea is that the inner workings of the object are hidden from the client, but the object offers methods which can be used to access the data stored in the object.

# Adding a method does not automatically hide the attribute. 
# Even though the 'BankAccount' class definition contains the 'withdraw' method for withdrawing money, 
# the client code can still access and change the 'balance' attribute directly:
peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)

# Attempt to withdraw 2000
if peters_account.withdraw(2000):
    print("The withdrawal was successful, the balance is now", peters_account.balance)
else:
    print("The withdrawal was unsuccessful, the balance is insufficient")

    # "Force" the withdrawal of 2000
    peters_account.balance -= 2000

print("The balance is now:", peters_account.balance)

# It is possible to hide the data attributes from the client code, which can help in solving this problem. 
# We will return to this topic in the next part.

# Decreasing counter - Approach 1

# The exercise template contains a partially completed class 'DecreasingCounter':
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        pass

    # define the rest of your methods here
    
# The class can now be used as shown below, and should produce the following printout after completing the first part of the exercise:
counter = DecreasingCounter(10)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

'''
value: 10
value: 9
value: 8
'''

# Part 1: Decreasing the value of the counter
# Please complete the method decrease defined in the template, so that it decreases the value stored in the counter by one. 
# See the example above for expected behaviour.
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value -= 1

# Part 2: The counter must not have a negative value
# Please add functionality to your decrease method, so that the value of the counter will never reach negative values. 
# If the value of the counter is 0, it will not be further decreased.
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value -= 1 if self.value > 0 else 0

counter = DecreasingCounter(2)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

# Part 3: Setting the value to zero
# Please add a method 'set_to_zero' which sets the value of the counter to 0:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value -= 1 if self.value > 0 else 0
        
    def set_to_zero(self):
        self.value = 0

counter = DecreasingCounter(100)
counter.print_value()
counter.set_to_zero()
counter.print_value()

# Part 4: Resetting the counter
# Please add a method 'reset_original_value()' which resets the counter to its initial state:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value -= 1 if self.value > 0 else 0
        
    def set_to_zero(self):
        self.value = 0
        
    def reset_original_value(self):
        self.value = self.original_value

counter = DecreasingCounter(55)
counter.decrease()
counter.decrease()
counter.decrease()
counter.decrease()
counter.print_value()
counter.set_to_zero()
counter.print_value()
counter.reset_original_value()
counter.print_value()

# To finish off this section, lets have a look at a class which models the personal best of a player. 
# The class definition contains separate validator methods which ascertain that the arguments passed are valid. 
# The methods are called already within the constructor. This ensures the object created is internally sound.
from datetime import date

class PersonalBest:

    def __init__(self, player: str, day: int, month: int, year: int, points: int):
        # Default values
        self.player = ""
        self.date_of_pb = date(1900, 1, 1)
        self.points = 0

        if self.name_ok(player):
            self.player = player

        if self.date_ok(day, month, year):
            self.date_of_pb = date(year, month, day)

        if self.points_ok(points):
            self.points = points

    # Helper methods to check the arguments are valid
    def name_ok(self, name: str):
        return len(name) >= 2 # Name should be at least two characters long

    def date_ok(self, day, month, year):
        try:
            date(year, month, day)
            return True
        except:
            # an exception is raised if the arguments are not valid
            return False

    def points_ok(self, points):
        return points >= 0

if __name__ == "__main__":
    result1 = PersonalBest("Peter", 1, 11, 2020, 235)
    print(result1.points)
    print(result1.player)
    print(result1.date_of_pb)

    # The date was not valid
    result2 = PersonalBest("Paula", 4, 13, 2019, 4555)
    print(result2.points)
    print(result2.player)
    print(result2.date_of_pb) # Prints the default value 1900-01-01
    
# In the example above also the helper methods were called via the 'self' parameter name when they were used in the constructor. 
# It is possible to also include static method definitions in class definitions. 
# These are methods which can be called without ever creating an instance of the class. 
# We will return to this subject in the next part.

# The parameter name 'self' is only used when referring to the features of the object as an instance of the class. 
# These include both the 'data attributes' and the 'methods' attached to an object. 
# To make the terminology more confusing, the data attributes and methods are together sometimes referred to simply as the 'attributes of the object', 
# which is why in this material we have often specified data attributes when we mean the variables defined within the class. 
# This is where the terminology of some Python programmers slightly differs from the terminology used in object oriented programming more widely, 
# where attributes usually refers to just the data attributes of an object.

# It is also possible to create local variables within method definitions without referring to 'self'. 
# You should do so if there is no need to access the variables outside the method. 
# Local variables within methods have no special keywords; they are used just like any normal variables you have come across thus far.

# So, for example this would work:
class BonusCard:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def add_bonus(self):
        # The variable bonus below is a local variable.
        # It is not a data attribute of the object.
        # It can not be accessed directly through the object.
        bonus = self.balance * 0.25
        self.balance += bonus

    def add_superbonus(self):
        # The superbonus variable is also a local variable.
        # Usually helper variables are local variables because
        # there is no need to access them from the other
        # methods in the class or directly through an object.
        superbonus = self.balance * 0.5
        self.balance += superbonus

    def __str__(self):
        return f"BonusCard(name={self.name}, balance={self.balance})"
    
# First and last name - Approach 1

# Please write a class named 'Person' with a single attribute 'name', which is set with an argument given to the constructor.
# Please also add two methods:
# The method 'return_first_name' should return the first name of the person, 
# while the method 'return_last_name' should return the last name of the person.
# You may assume that the name passed to the constructor will contain exactly two name elements separated with a space character.
class Person:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def return_first_name(self) -> str:
        return self.name.split(" ")[0]
    
    def return_last_name(self) -> str:
        return self.name.split(" ")[1]


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())

# First and last name - Approach 2
class Person:
    def __init__(self, name: str):
        self.name = name
 
    def return_first_name(self):
        names = self.name.split(" ")
        return names[0]
 
    def return_last_name(self):
        names = self.name.split(" ")
        return names[-1]

# Statistics on numbers - Approach 1

# In this exercise you are asked to create a program for working with numbers, 
# similarly to the exercise completed in Part 2 - Simple Loops, "Sum, mean, number counter and positives and negatives counter". 
# This time you will define a class for the purpose.

# Part 1 - Count the numbers

# Please write a class named 'NumberStats' with the following methods:
    # the method 'add_number' adds a new number to the statistical record
    # the method 'count_numbers' returns the count of how many numbers have been added

# At this point there is no need to store the numbers themselves in any data structure. 
# It is enough to simply remember how many have been added. 
# The 'add_number' method does take an argument, but there is no need to process the actual value in any way just yet.

# The exercise template contains the following skeleton for the class definition:
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.addcount = 0

    def add_number(self, number:int):
        self.addcount += 1

    def count_numbers(self):
        return self.addcount

stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())

# Part 2 - The sum and the mean
# Please add the following methods to your class definition:
    # the method 'get_sum' should return the sum of the numbers added (if no numbers have been added, the method should return 0)
    # the method 'average' should return the mean of the numbers added (if no numbers have been added, the method should return 0)

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.addcount = 0

    def add_number(self, number:int):
        self.addcount += 1
        self.numbers += number

    def count_numbers(self):
        return self.addcount
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        return (self.numbers / self.addcount) if self.numbers > 0 else 0
        
stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())

# Part 3 - User input
# Please write a main program which keeps asking the user for integer numbers until the user types in -1. 
# The program should then print out the sum and the mean of the numbers typed in.
# Your program should use a 'NumberStats' object to keep a record of the numbers added.

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.addcount = 0

    def add_number(self, number:int):
        self.addcount += 1
        self.numbers += number

    def count_numbers(self):
        return self.addcount
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        return (self.numbers / self.addcount) if self.numbers > 0 else 0

stats = NumberStats()
print("Please type in integer numbers:")
while True:
    number = int(input())
    if number != -1:
        stats.add_number(number)
    else:
        break

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")

# Part 4 - Multiple sums 
# Please add to your main program so that it also counts separately the sum of the even and the odd numbers added.
# NB: do not change your 'NumberStats' class definition in this part of exercise. 
# Instead, define three 'NumberStats' objects. One of them should keep track of all the numbers, another should track the even numbers, and the third should track the odd numbers typed in.
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.addcount = 0
        self.evensum = 0
        self.oddsum = 0

    def add_number(self, number:int):
        self.numbers += number
        self.addcount += 1
        self.evensum += number if number % 2 == 0 else 0
        self.oddsum += number if number % 2 != 0 else 0

    def count_numbers(self):
        return self.addcount
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        return (self.numbers / self.addcount) if self.numbers > 0 else 0
    
    def even_number_sum(self):
        return self.evensum
    
    def odd_number_sum(self):
        return self.oddsum

stats = NumberStats()
print("Please type in integer numbers:")
while True:
    number = int(input())
    if number != -1:
        stats.add_number(number)
    else:
        break

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {stats.even_number_sum()}")
print(f"Sum of odd numbers: {stats.odd_number_sum()}")

# Statistics on numbers - Approach 2

class  NumberStats:
    def __init__(self):
        self.numbers = []
 
    def add_number(self, number:int):
        self.numbers.append(number)
 
    def count_numbers(self):
        return len(self.numbers)
 
    def get_sum(self):
        return sum(self.numbers)
 
    def average(self):
        if not self.numbers:
            return 0.0
        else:
            return self.get_sum() / self.count_numbers()
 
stats = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    number = int(input("Give a number: "))
    if number == -1:
        break
 
    stats.add_number(number)
    if number % 2 == 0:
        even.add_number(number)
    else:
        odd.add_number(number)
 
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())