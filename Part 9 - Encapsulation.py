# Encapsulation

# In object oriented programming the term _client_ refers to a program which uses a class, or instances of a class. A class offers the client _services_ through which the client can access the objects created based on the class. 
# The goals here are that:
    # 1) the use of a class and/or objects is as simple as possible from the client's point of view
    # 2) the _integrity_ of any object is preserved at all times

# The integrity of an object means that the _state_ of an object always remains acceptable. 
# In practice this means that the values of the object's attributes are always acceptable. 
# For example, an object representing a date should never have 13 as the value of the month, an object modelling a student should never have a negative number as the value of study credits attained, and so forth.

# Let's take a look at a class named Student:

class Student:
    def __init__(self, name: str, student_number: str):
        self.name = name
        self.student_number = student_number
        self.study_credits = 0

    def add_credits(self, study_credits):
        if study_credits > 0:
            self.study_credits += study_credits

# The `Student` object offers its clients the method `add_credits`, which allows the client to add a specified number of credits to the student's total. 
# The method ensures the value passed as the argument is above zero. The following code adds study credits on three occasions:

sally = Student("Sally Student", "12345")
sally.add_credits(5)
sally.add_credits(5)
sally.add_credits(10)
print("Study credits:", sally.study_credits)

# Despite the method definition it is still possible to access the `study_credits` attribute directly. 
# This could result in an erroneous state where the integrity of the object is lost:

sally = Student("Sally Student", "12345")
sally.study_credits = -100
print("Study credits:", sally.study_credits)

# A common feature in object oriented programming languages is that classes can usually hide their attributes from any prospective clients. 
# Hidden attributes are usually called _private_. 
# In Python this privacy is achieved by adding two underscores `__` to the beginning of the attribute name:

class CreditCard:
    # the attribute number is private, while the attribute name is accessible
    def __init__(self, number: str, name: str):
        self.__number = number
        self.name = name

# A private attribute is not directly visible to the client. 
# Trying to refer to it causes an error. 
# In the above example the `name` attribute can be easily accessed and changed:

card = CreditCard("123456","Randy Riches")
print(card.name)
card.name = "Charlie Churchmouse"
print(card.name)

# Trying to print out the card number, however, causes and error:
card = CreditCard("123456","Randy Riches")
print(card.__number)

# Hiding attributes from clients is called _encapsulation_. As the name implies, the attribute is "enclosed in a capsule". 
# The client is then offered a suitable interface for accessing and processing the data stored in the object.

# Let's add another encapsulated attribute: the balance on the credit card. 
# This time we'll also add publicly visible methods which allow the client to access and change the balance:

class CreditCard:
    def __init__(self, number: str, name: str, balance: float):
        self.__number = number
        self.name = name
        self.__balance = balance

    def deposit_money(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def withdraw_money(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def retrieve_balance(self):
        return self.__balance

card = CreditCard("123456", "Randy Riches", 5000)
print(card.retrieve_balance())
card.deposit_money(100)
print(card.retrieve_balance())
card.withdraw_money(500)
print(card.retrieve_balance())
# The following will not work because the balance is not sufficient
card.withdraw_money(10000)
print(card.retrieve_balance())

# The balance cannot be changed directly because the attribute is private, but we've included the methods `deposit_money` and `withdraw_money` for changing the value. 
# The method `retrieve_balance` returns the value stored in balance. 
# The methods include some rudimentary checks for retaining the integrity of the object: for instance, the card cannot be overdrawn.

# Car - Approach 1

# Please implement a class named `Car` which has two private, _encapsulated_ variables: the amount of petrol in the tank (0 to 60 litres) and odometer reading (in kilometres). 
# The car consumes one litre of petrol per kilometre.

# The class should also contain the following methods:
    # - `fill_up()` which fills up the tank
    # - `drive(km:int)` which drives the car for the distance indicated, or for however long the petrol in the tank allows
    # - `__str__` which returns a string representation of the car as per the examples below


class Car:
    def __init__(self) -> None:
        self.__fuel = 0
        self.__odometer = 0
    
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__fuel} litres"
    
    def fill_up(self) -> None:
        self.__fuel = 60
            
    def drive(self, km:int) -> None:
        if km <= self.__fuel and km > 0:
           self.__odometer += km
           self.__fuel -= km 
        elif km > self.__fuel and km > 0:
            self.__odometer += self.__fuel
            self.__fuel = 0

car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)

car = Car()
car.fill_up()
car.drive(10)
car.drive(20)
car.drive(10)
car.drive(20)
car.drive(5)
car.fill_up()
car.drive(10)
car.drive(30)
print(car)

# Car - Approach 2
class Car:
    def __init__(self):
        self.__petrol = 0
        self.__driven = 0
 
    def fill_up(self):
        self.__petrol = 60
 
    def drive(self, km: int):
        if km > self.__petrol:
            km = self.__petrol
 
        self.__driven += km
        self.__petrol -= km
 
    def __str__(self):
        return f"Car: odometer reading {self.__driven} km, petrol remaining {self.__petrol} litres"

# A brief note on private attributes, Python and object oriented programming
# There are ways around the underscore `__` notation for hiding attributes, which you may come across if you search for resources online. 
# No Python attribute is truly private, and this is intentional on the part of the creators of Python. 
# On the other hand, a Python programmer is generally expected to respect the visibility guidelines set in classes, and it takes a special effort to get around these. 
# In other object oriented programming languages, such as Java, private variables are often truly hidden, and it is best if you think of private Python variables as such as well.

# Getters and setters

# In object oriented programming, methods which are dedicated to accessing and changing attributes are usually called _getters_ and _setters_. 
# Not all Python programmers use the terms "getter" and "setter", but the concept of _properties_ outlined below is very similar, which is why we will use the generally accepted object oriented programming terminology here. 

# So, above we created some public methods for accessing private attributes, but there is a more straightforward, "pythonic" way of accessing attributes. 
# Let's have a look at a simple class named `Wallet` with a single, private attribute `money`:
class Wallet:
    def __init__(self):
        self.__money = 0

# We can add getter and setter methods for accessing the private attribute using the `@property` decorator:
class Wallet:
    def __init__(self):
        self.__money = 0

    # A getter method
    @property
    def money(self):
        return self.__money

    # A setter method
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money
            
# First, we define a getter method, which returns the amount of money currently in the wallet. 
# Then we define a setter method, which sets a new value for the money attribute while making sure the new value is not negative.

wallet = Wallet()
print(wallet.money)

wallet.money = 50
print(wallet.money)

wallet.money = -30
print(wallet.money)

# As far as the client is concerned, using these new methods is no different from directly accessing an attribute. 
# Parentheses are not necessary; instead it is perfectly acceptable to state `wallet.money = 50`, as if we were simply assigning a value to a variable. 
# Indeed, the purpose was to hide (i.e. encapsulate) the internal implementation of the attribute while offering an easy way of accessing and modifying the data stored in the object.

# The previous example has a small problem: the client is not notified of the failure to set a negative value for the money attribute. 
# When a value supplied is clearly wrong, it is usually a good idea to raise an exception and thus let the client know. 
# In this case the exception should probably be of type `ValueError` to signify that the value supplied was unacceptable.

# Here we have an improved version of the class, along with some code for testing it:
class Wallet:
    def __init__(self):
        self.__money = 0

    # A getter method
    @property
    def money(self):
        return self.__money

    # A setter method
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money
        else:
            raise ValueError("The amount must not be below zero")

wallet = Wallet()
wallet.money = -30
print(wallet.money)

# Note: the getter method, i.e. the `@property` decorator, must be introduced before the setter method, or there will be an error when the class is executed. 
# This is because the `@property` decorator defines the name of the "attribute" offerred to the client. 
# The setter method, added with `.setter`, simply adds a new functionality to it.

# Recording - Approach 1

# Please create a class named `Recording` which models a single recording. 
# The class should have one private variable: `__length` of type integer.

# Please implement the following:
    # * a constructor which takes the length as an argument
    # * a getter method `length` which returns the length of the recording
    # * a setter method which sets the length of the recording

class Recording:
    def __init__(self, length:int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Length cannot be a negative number")
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Length cannot be a negative number")

the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)

# The following example has a class with two private attributes, along with getters and setters for both. 
# Please try the program out with different values passed as arguments:

class Player:
    def __init__(self, name: str, player_number: int):
        self.__name = name
        self.__player_number = player_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name may not be an empty string")

    @property
    def player_number(self):
        return self.__player_number

    @player_number.setter
    def player_number(self, player_number: int):
        if player_number > 0:
            self.__player_number = player_number
        else:
            raise ValueError("The player number must be a positive integer")

player = Player("Betty Ballmer", 10)
print(player.name)
print(player.player_number)

player.name = "Buster Ballmer"
player.player_number = 11
print(player.name)
print(player.player_number)

# let's take a look at a class which models a simple diary. 
# All attributes are private, but they are handled through differing interfaces: 
# the owner of the diary has getter and setter methods, 
# but the diary entries are processed with "traditional" methods. 
# In this case it makes sense to deny the client all access to the internal data structure of the diary. 
# Only the public methods are directly visible to the client. 

# Encapsulation also ensures that the internal implementation of the class can be changed at will, 
# provided that the public interface stays intact. 
# The client does not have to know or care whether the internal data structure is based on lists, dictionaries, or something completely different.

class Diary:
    def __init__(self, owner: str):
        self.__owner = owner
        self.__entries = []

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        if owner != "":
            self.__owner = owner
        else:
            raise ValueError("The owner may not be an empty string")

    def add_entry(self, entry: str):
        self.__entries.append(entry)

    def print_entries(self):
        print("A total of", len(self.__entries), "entries")
        for entry in self.__entries:
            print("- " + entry)

diary = Diary("Peter")
print("Owner:", diary.owner)
diary.owner = "Abdullah"
diary.add_entry("Today I ate porridge")
diary.add_entry("Today I learned object oriented programming")
diary.add_entry("Today I went to bed early")
diary.print_entries()
print("Owner:", diary.owner)

# Weather station - Approach 1

# Please create a class named `WeatherStation` which is used to store observations about the weather. 
# The class should have the following public attributes:
    # a constructor which takes the name of the station as its argument
    # a method named `add_observation(observation: str)` which adds an observation as the last entry in a list
    # a method named `latest_observation()` which returns the latest observation added to the list. If there are no observations yet, the method should return an _empty string_.
    # a method named `number_of_observations()` which returns the total number of observations added
    # a `__str__` method which returns the name of the station and the total number of observations added as per the example below.

# All attributes should be encapsulated, so they can't be directly accessed. 
# It is up to you how you implement the class, as long as the public interface is exactly as described above.

class WeatherStation:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observations = []
    
    def add_observation(self, observation: str) -> None:
        self.__observations.append(observation)
    
    def latest_observation(self):
        if len(self.__observations) != 0:
            return self.__observations[-1]
        else:
            return ""
    
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self) -> str:
        return f"{self.__name}, {len(self.__observations)} observations"


station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)

# Weather station - Approach 2
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = 0
        self.__latest_observation = ""
 
    def add_observation(self, observation: str):
        self.__latest_observation = observation
        self.__observations += 1
 
    def latest_observation(self):
        return self.__latest_observation
 
    def number_of_observations(self):
        return self.__observations 
 
    def __str__(self):
        return f"{self.__name}, {self.__observations} observations"