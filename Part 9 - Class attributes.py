# Class attributes

# The _traits_ of objects are a central concept in object oriented programming. 
# The term encompasses the methods and variables defined in the class definition. 
# Again, not all Python programmers use the term "traits", some preferring _attributes_, _features_ or _members_. 
# Traits is quite accepted in the wider object oriented programming world, so that is the term we use here.

# Thus far we have dealt mostly with _traits of objects_. 
# These include the methods and attributes accessible in any instance of a class. 
# In fact, classes _themselves_ can also have traits, which are sometimes called _static traits_, or more specifically _class variables_ and _class methods_.

# Class variables

# Each instance of a class has its own specific values for each attribute defined in the class, as we've seen in the examples in the previous sections. 
# But what if we wanted to have some data that is shared by the different instances? 
# Enter _class variables_, also known as static variables. 
# A class variable is a variable which is accessed through the class itself, not through the instances created based on the class. 
# At any given time during the execution of the program a class variable has one single value, no matter how many instances of the class are created.

# A class variable is declared without the `self` prefix, and usually outside any method definition as it should be accessible from anywhere within the class, or even from outside the class.

class SavingsAccount:
    general_rate = 0.03

    def __init__(self, account_number: str, balance: float, interest_rate: float):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate

    def add_interest(self):
        # The total interest rate equals 
        # the general rate + the interest rate of the account
        total_interest = SavingsAccount.general_rate + self.__interest_rate
        self.__balance += self.__balance * total_interest

    @property
    def balance(self):
        return self.__balance

# As the variable `general_rate` is defined within the class but outside any method definitions, and it does not use the `self` prefix, it is a class variable.

# A class variable is accessed through the name of the class, for example like this:
# The general rate exists independently of any object instances
print("The general interest rate is", SavingsAccount.general_rate)

account = SavingsAccount("12345", 1000, 0.05)
# Add the total interest accrued to the balance on the account
account.add_interest()
print(account.balance)

# So, the class variables are accessed through the name of the class, for instance with `SavingsAccount.general_rate`, while instance variables are accessed through the name of the object variable, such as `account.balance`. 
# An instance variable naturally only exists when an instance of the class has been created, but a class variable is available everywhere and at any point in time where the class itself is available.

# Class variables are useful when there is need for values which are shared by all instances of the class. 
# In the example above we assumed the total interest rate of all savings accounts is formed from two components: the general rate of interest is shared by all accounts, but each account also has it's own interest rate in an instance variable. 
# The general rate may also change, but the change will then affect all instances of the class equally.

class SavingsAccount:
    general_rate = 0.03

    def __init__(self, account_number: str, balance: float, interest_rate: float):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate

    def add_interest(self):
        # The total interest rate equals 
        # the general rate + the interest rate of the account
        total_interest = SavingsAccount.general_rate + self.__interest_rate
        self.__balance += self.__balance * total_interest

    @property
    def balance(self):
        return self.__balance

    @property
    def total_interest(self):
        return self.__interest_rate + SavingsAccount.general_rate
    
account1 = SavingsAccount("12345", 100, 0.03)
account2 = SavingsAccount("54321", 200, 0.06)

print("General interest rate:", SavingsAccount.general_rate)
print(account1.total_interest)
print(account2.total_interest)

# The general rate of interest is now 10 percent
SavingsAccount.general_rate = 0.10

print("General interest rate:", SavingsAccount.general_rate)
print(account1.total_interest)
print(account2.total_interest)

# When the general rate of interest changes, the total interest rate for all instances of the class changes. 
# As you can see above, it is possible to add a getter method with the `@property` decorator even though there isn't an attribute of the same name in the class. 
# This method returns the sum of the general rate of interest and the account specific interest rate.

# Note that when a new instance of the class is generated the Class Variable is also replicated in the new instance.
# Consider the following example:

class NewClass:
    class_rate = 1

# We can access the 'class_rate' from outside the class as such:
print(NewClass.class_rate)

# When we create a new instance of NewClass, we can also access the Class Variable as an Instance Variable.

class_instance = NewClass()
print(class_instance.class_rate)

# Let us change the value of the Instance Variable or the Object Attribute as follows:
class_instance.class_rate = 2
print(class_instance.class_rate)
print(NewClass.class_rate)

# We can note that while the Instance Variable that was created when a new instance of the class was generated has changed, the Class Vairable remains unchanged.
# Now, lets change the Class Variable from the client code and print the value of the new Class Variable
NewClass.class_rate = 3
print(NewClass.class_rate)

# However, the previously generated instance of the class still holds a modified version of the Instance Variable and is unaffected by the change in Class Variable.
print(class_instance.class_rate)

# Let's have a look at another example. 
# The class `PhoneNumber` is used to define a single phone number, but it also contains some country codes in a dictionary. 
# This dictionary is a class variable, and as such is shared by all the instances of the class, because the country code for phone numbers from a single country is always the same.

class PhoneNumber:
    country_codes = {"Finland": "+358", "Sweden": "+46", "United States": "+1"}

    def __init__(self, name: str, phone_number: str, country: str):
        self.__name = name
        self.__phone_number = phone_number
        self.__country = country

    @property
    def phone_number(self):
        # When the country code prefix is added 
        # the initial zero is removed from the phone number
        return PhoneNumber.country_codes[self.__country] + " " + self.__phone_number[1:]

paulas_no = PhoneNumber("Paula Pythons", "050 1234 567", "Finland")
print(paulas_no.phone_number)

# Each 'PhoneNumber' object contains the name of the owner, the number itself, and the country of the phone number. 
# When the attribute containing the phone number is accessed with the getter method, the appropriate country code is retrieved from the class variable dictionary based on the country attribute, and the result is prefixed to the number.

# The example implementation above is not yet very functional otherwise. 
# In the following example we've added getter and setters for all attributes:

class PhoneNumber:
    country_codes = {"Finland": "+358", "Sweden": "+46", "United States": "+1"}

    def __init__(self, name: str, phone_number: str, country: str):
        self.__name = name
        # This is a call to the phone_number.setter method
        self.phone_number = phone_number
        # This is a call to the country.setter method
        self.country = country

    # the getter method for phone_number combines the country code 
    # and the attribute phone_number
    @property
    def phone_number(self):
        # the initial zero is removed as the country code is prefixed
        return PhoneNumber.country_codes[self.__country] + " " + self.__phone_number[1:]

    @phone_number.setter
    def phone_number(self, number):
        # Making sure the number contains only numbers and space characters
        for character in number:
            if character not in "1234567890 ":
                raise ValueError("A phone number can only contain numbers and spaces")
        self.__phone_number = number

    # a getter for only the number itself without the country code
    @property
    def local_number(self):
        return self.__phone_number

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        # Making sure the country is a key in the dictionary of country codes
        if country not in PhoneNumber.country_codes:
            raise ValueError("This country is not on the list.")
        self.__country = country

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f"{self.phone_number} ({self.__name})"

if __name__ == "__main__":
    pn = PhoneNumber("Peter Pythons", "040 111 1111", "Sweden")
    print(pn)
    print(pn.phone_number)
    print(pn.local_number)
    
# Postcodes - Approach 1

# The exercise template contains the class definition `City` which is a model for a single city.

# Please add a class variable named `postcodes` which refers to a dictionary. The keys of the dictionary are names of cities, and the values attached are the postcodes for those cities. Both are strings.
# The dictionary should contain (at least) the following postcodes:
    # Helsinki 00100
    # Turku 20100
    # Tampere 33100
    # Rovaniemi 96100
    # Oulu 90100

class City:
    postcodes = {'Helsinki': '00100', 
                 'Turku': '20100', 
                 'Tampere': '33100', 
                 'Rovaniemi': '96100', 
                 'Oulu': '90100'}
    
    def __init__(self, name: str, population: int):
        self.__name = name
        self.__population = population

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    def __str__(self):
        return f"{self.__name} ({self.__population} residents.)"

# Class methods

# A class method, also called a static method, is a method which is not attached to any single instance of the class. 
# A class method can be called without creating any instances of the class. 

# Class methods are usually tools which have something to do with the purpose of the class, but which are detached in the sense that it should not be necessary to create instances of the class in order to be able to call them. 
# Class methods are usually public, so that they can be called both from outside the class and from within the class, including from within instances of the class.

# A class method is defined with the `@classmethod` annotation. 
# The first parameter is always `cls`. The variable name `cls` is similar to the `self` parameter.
# The difference is that `cls` points to the class while `self` point to an instance of the class. 
# Neither parameter is included in the argument list when the function is called; Python fills in the appropriate value automatically.

# In the following example we have a class modelling vehicle registrations. 
# The `Registration` class contains a static method for checking whether a license plate is valid. 
# The method is a static class method because it is useful to be able to check if a license plate is valid even before a single Registration object is created:

class Registration:
    def __init__(self, owner: str, make: str, year: int, license_plate: str):
        self.__owner = owner
        self.__make = make
        self.__year = year

        # Call the license_plate.setter method
        self.license_plate = license_plate

    @property
    def license_plate(self):
        return self.__license_plate

    @license_plate.setter
    def license_plate(self, plate):
        if Registration.license_plate_valid(plate):
            self.__license_plate = plate
        else:
            raise ValueError("The license plate is not valid")

    # A class method for validating the license plate
    @classmethod
    def license_plate_valid(cls, plate: str):
        if len(plate) < 3 or "-" not in plate:
            return False

        # Check the beginning and end sections of the plate separately
        letters, numbers = plate.split("-")

        # the beginning section can have only letters
        for character in letters:
            if character.lower() not in "abcdefghijklmnopqrstuvwxyzåäö":
                return False

        # the end section can have only numbers
        for character in numbers:
            if character not in "1234567890":
                return False

        return True

registration = Registration("Mary Motorist", "Volvo", "1992", "abc-123")

if Registration.license_plate_valid("xyz-789"):
    print("This is a valid license plate!")

# The validity of a license plate can be checked even without creating a single instance of the class, for example with `Registration.license_plate_valid("xyz-789")`. 
# The same method is called within the constructor of the class. 
# NB: even within the constructor this method is accessed through the name of the class, not `self`!

# List helper - Approach 1

# Please create a class named `ListHelper` which contains the following two class methods.
    # `greatest_frequency(my_list: list)` returns the most common item on the list
    # `doubles(my_list: list)` returns the number of unique items which appear at least twice on the list

# It should be possible to use these methods without creating an instance of the class.

class ListHelper:
    @classmethod
    def __unique_and_frequency(cls, my_list: list):
        list_unique = []
        for item in my_list:
            if item not in list_unique:
                list_unique.append(item)
        
        frequency = []
        for item in list_unique:
            frequency.append(my_list.count(item))
        
        return list_unique, frequency     
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        list_unqiue, frequency = cls.__unique_and_frequency(my_list)
        return list_unqiue[frequency.index(max(frequency))]
    
    @classmethod
    def doubles(cls, my_list: list):
        list_unqiue, frequency = cls.__unique_and_frequency(my_list)
        counter = 0
        for num in frequency:
            if num > 1:
                counter += 1
        return counter

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))

# List helper - Approach 2
class ListHelper:
    @classmethod
    def __unique_and_frequency(cls, my_list: list):
        list_unique = []
        for item in my_list:
            if item not in list_unique:
                list_unique.append(item)
        
        frequency = []
        for item in list_unique:
            frequency.append(my_list.count(item))
        
        return list_unique, frequency     
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        list_unqiue, frequency = cls.__unique_and_frequency(my_list)
        return list_unqiue[frequency.index(max(frequency))]
    
    @classmethod
    def doubles(cls, my_list: list):
        list_unqiue, frequency = cls.__unique_and_frequency(my_list)
        return len(frequency) - frequency.count(1)

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))

# List helper - Approach 3
class ListHelper:
 
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None
 
        max_frequency = 0
        max_item = None
        for item in my_list:
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency:
                max_frequency = frequency
                max_item = item
 
        return max_item
 
    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)
 
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
 
        return doubles