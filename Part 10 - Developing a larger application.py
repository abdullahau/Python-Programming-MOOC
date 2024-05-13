# Developing a larger application

# Managing complexity:

# Python features covered in the course material include control structures (while, for), functions, and basic data structures (lists, tuples, dictionaries).
# Objects and classes covered in the advanced section are not always necessary, but they become useful in managing complexity in larger and more complicated programs.
# "Separation of concerns" is a fundamental design principle in programming, aimed at organizing a program into distinct sections, each addressing a separate concern.
# Functions and object-oriented programming (OOP) are common approaches to managing larger programs.
# Objects and classes allow for the collection of data and code processing within a single unit, while encapsulating the data they control to hide internal details from other parts of the program.

# A worked example

# Program division into classes and objects involves adhering to the "single-responsibility principle".
# Object-oriented programming models real-world objects with classes.
# Objects such as "person," "name," and "phone number" can represent entities in a phone book application.
# The phone book itself can be a class responsible for managing person objects and their data.
# Core "application logic" includes classes for managing the phone book and constitute the programming logic of our application
# Handling "user interface" or user interaction with the application can be a seperate responsibility on its own.
# Other classes, such as for "file handling" for persistent storage, may also be necessary.
# There is no strict rule on where to begin programming, but starting with the "application logic" is often a good approach.

# Step 1: an outline for the application logic

# Let's start with the class _PhoneBook_. A skeleton implementation could look like this:
class PhoneBook:
    def __init__(self):
        self.__persons = []

    def add_number(self, name: str, number: str):
        pass

    def get_numbers(self, name: str):
        pass

# This class consists of a list of persons along with methods for both adding and fetching data.

# Each person may be connected with multiple numbers, so let's implement the internal structure of `persons` with a dictionary. 
# A dictionary allows us to search for keys by name, and the value attached to a dictionary key can be a list. 
# So far it looks like we don't really need a separate class to represent a person - an entry in a dictionary will do.

# Let's implement the methods listed above, and test our phone book:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None

        return self.__persons[name]

phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_numbers("Eric"))
print(phonebook.get_numbers("Emily"))

# The method `get_numbers` returns `None` if a name is not included in the phone book. 
# If the name is found, it returns the list of numbers attached to the name.

# Step 2: an outline for the user interface

# With the core application logic out of the way, it is time to implement a text-based user interface. 
# We will need a new class, `PhoneBookApplication`, with the following initial functionality:
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break

application = PhoneBookApplication()
application.execute()

# The constructor method creates a new PhoneBook, which is "stored" in a "private attribute". 
# The method `execute(self)` starts the program's text-based user interface, the core of which is the `while` loop, 
# which keeps asking the user for commands until they type in the command for exiting.

# There is also a method for intructions, `help(self)`, which is called before entering the loop, 
# so that the instructions are printed out.

# Now, let's add some actual functionality. First, we implement adding new data to the phone book:
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                number = input("number: ")
                self.__phonebook.add_number(name, number)

application = PhoneBookApplication()
application.execute()

# If the user types in _1_ for adding a new number, the user interface asks for a name and a number, 
# and adds these to the PhoneBook using the appropriate method defined in the class.

# The only responsibility of the user interface is to communicate with the user. 
# Any other functionality, such as storing a new name-number pair, is the responsibility of the PhoneBook object.

# There is room for improvement in the structure of our user interface class. 
# Let's create a method `add_entry(self)` which handles the command for adding a new entry:
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")

    # separation of concerns in action: a new method for adding an entry
    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()

application = PhoneBookApplication()
application.execute()

# The _separation of concerns_ principle extends to the level of methods, too. 
# We could have the entire functionality of the user interface in a single complicated `while` loop, but it is better to separate each functionality into its own method. 
# The responsibility of the `execute()` method is just delegating the commands typed in by the user to the relevant methods. This helps with managing the growing complexity of our program. 
# For example, if we want to later change the way adding entries works, it is immediately clear that we must then focus our efforts on the `add_entry()` method.

# Let's include functionality for searching for entries in our user interface. 
# This should have its own method, too:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None

        return self.__persons[name]

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()

# We now have a simple working phone book application ready for testing. The following is an example run:

# For such a simple application we have written quite a lot of code. 
# If we'd written it all within the one `while` loop we could probably have gotten away with a lot less code. 
# It is, however, quite easy to read the code, the structure is clear, and we should have no trouble adding new features.

# Step 3: importing data from a file

# Let's assume we already have some phone numbers stored in a file, and we want to read this as the program starts up. 
# The data file is in the following CSV format:
'''
Eric;02-1234567;045-4356713
Emily;040-324344
'''

# Handling files is clearly its own area of responsibility, so it merits a class of its own:
class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers

        return names

# The constructor method takes the name of the file as its argument. 
# The method `load_file(self)` reads the contents of the file. 
# It splits each line into two parts: a name and a list of numbers. 
# It then adds these to a dictionary, using the name as the key and the list as the value.

# The method uses a nifty Python feature: it is possible to first select some items from a list separately, and then take the rest of the items in a new list. 
# You can see an example of this below. You may remember that the string method `split` returns a list.

my_list = [1, 2, 3, 4, 5]
first, second, *rest = my_list
print(first)
print(second)
print(rest)

# The `*` in front of the variable name `rest` in the assignment statement means that this last variable should contain all the remaining items in the list, from the third one onwards.

# We should absolutely test the file handler separately before including it in our application:
t = FileHandler("phonebook.txt")
print(t.load_file())

'''
{'Eric': ['02-1234567', '045-4356713'], 'Emily': ['040-324344']}
'''

# As the file handler seems to work fine, we can add it to our application. 
# Let's assume we want to read the file first thing every time the program is run. 
# The logical place for reading the file would be the constructor of the `PhoneBookApplication` class:

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    # the rest of the program

# This functionality should also be tested. Once we've made certain the contents of the file are accessible through the user interface of our application, we can move on to the next stage.

# Step 4: export data to a file

# The final feature in our basic version of the application is saving the contents of the phone book back in the same file the data was read from.
# This involves a change to the `PhoneBook` class. We need to be able to export the contents of the phone book:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    # ...

    # return all entries (in dictionary format)
    def all_entries(self):
        return self.__persons
    
# The actual saving to the file should be handled by the `FileHandler` class. 
# Let's add the method `save_file` which takes a dictionary representation of the phone book as its argument:

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        # ...

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")

# The saving should happen as the program exits. 
# Let's add a method for this purpose to the user interface, and call it before breaking out of the `while` loop:

class PhoneBookApplication:
    # the rest of the code for the user interface

    # a method which gets executed as the program exits
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":

                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()

# Full Code Thus Far:
class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers

        return names
    
    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")    

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None

        return self.__persons[name]
    
    # return all entries (in dictionary format)
    def all_entries(self):
        return self.__persons    

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("PhoneBook Application\\phonebook.txt")
        
        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)         

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)
            
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())            

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()
     
# Phone book expansion, version 1 - Approach 1
# In this exercise you will create a small expansion to the phone book application. 
# The code from the above example is in the exercise template. 
# Please add a command which lets the user search the phone book by number. 

# Please implement this addition with respect to the current structure of the program. 
# This means that in the `PhoneBookApplication` class you should add an appropriate helper method to allow for the new functionality, 
# and also add a new branch to the `while` loop. In the `PhoneBook` class you should add a method which allows for searching with a number.

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers

        return names
    
    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")    

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None

        return self.__persons[name]
    
    def get_name(self, number: str):
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name
        return None        
    
    # return all entries (in dictionary format)
    def all_entries(self):
        return self.__persons    

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("PhoneBook Application\\phonebook.txt")
        
        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)         

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)
    
    def search_number(self):
        number = input("number: ")
        name = self.__phonebook.get_name(number)
        if name == None:
            print("unknown number")
            return
        print(name)
            
            
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())            

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_number()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()

# Objects in a dictionary

# In the next exercise you are asked to change your phone book so that the values in the dictionary are _objects_, not lists.

# There is nothing intrinsically strange about this, but this is the first time on this course that something like this is suggested, so let's go through a simpler example before diving into the exercise.

# Here we have an application which keeps track of how many exercises students have completed on a course. 
# Each student's exercise count is stored in a simple object:
class ExerciseCounter:
    def __init__(self):
        self.__exercises = 0

    def done(self):
        self.__exercises += 1

    def how_many(self):
        return self.__exercises

# The following main function uses the above class:
students = {}

print("let's do some exercises")
while True:
    name = input("student: ")
    if len(name) == 0:
        break

    # create a new object if it doesn't exist yet
    if not name in students:
        students[name] = ExerciseCounter()

    # add a new done exercise to the counter
    students[name].done()

print()
print("exercises completed:")

for student, exercises in students.items():
    print(f"{student}'s exercises: {exercises.how_many()}")
    
# There are a couple of things to consider in the above example. 
# When the user inputs a name, the program first checks if the name is already a key in the dictionary. 
# If the name is not present, a new object is created and added as an entry in the dictionary:
if not name in students:
    students[name] = ExerciseCounter()

# After this we can be _sure_ the object exists, attached to the name of the student which is used as the key. 
# Either it was just created, or it already existed from a previous iteration of the loop. 
# Either way, we can now retrieve the object with the key, and call the method `done`:
students[name].done()

# The above line actually contains two separate events. 
# We could just as well use a helper variable and write it on two separate lines of code:

students_counter = students[name]
students_counter.done()

# NB: Even though the object is here assigned to a helper variable, the object still exists in the dictionary just as before.  
# The helper variable contains a _reference_ to the object in the dictionary.

# Phone book expansion, version 2

# In this exercise you will create another version of the `PhoneBookApplication`. 
# You will add addresses to the data which can be attached to a name. 
# For simplicity's sake the functionality for saving to file has been removed, 
# and some other methods have been renamed to better accommodate the change.

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = []
        self.__persons[name].append(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        if numbers == None:
            print("number unknown") 
            return 
        for number in numbers:
            print(number)       

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# Part 1: A separate class for a person's data

# Please change the way the data of a person is handled. Implement a class named `Person`, 
# which takes care of the phone numbers and addresses of persons. The class should work as follows:

class Person:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__numbers = []
        self.__address = None
    
    def name(self) -> str:
        return self.__name
    
    def numbers(self) -> str:
        return self.__numbers
    
    def address(self) -> str:
        return self.__address
    
    def add_number(self, number: str):
        self.__numbers.append(number)
    
    def add_address(self, address: str):
        self.__address = address
    
    def __str__(self):
        pass    

person = Person("Eric")
print(person.name())
print(person.numbers())
print(person.address())
person.add_number("040-123456")
person.add_address("Mannerheimintie 10 Helsinki")
print(person.numbers())
print(person.address())

# Part 2: PhoneBook uses the class Person

# Please change the internal implementation of your application so that your `PhoneBook` class uses objects of class `Person` to store the data in the phone book. 
# That is, the attribute `__persons` should still contain a dictionary, but the values should be Person-objects and not lists. 
# The user of your application should notice no difference; the changes must not affect the user interface.

# **WARNING:** whenever you make structural changes to your code, as described in this exercise, always take baby steps and test at every possible stage. Do not try and make all the changes at once. 
# That is a sure way of **running into serious problems with your code**.

# A suitable first step might be to write some code for checking the functionality of the `PhoneBook` class directly. 

# Notice the new name for the method for fetching an entry from the phone book. 
# The automatic tests do not check what the printout from your `get_entry` method is, but make sure no errors are raised by the above code, and that the result makes sense within your implementation.

# When you've made the necessary changes in your program and have absolutely verified the functionality within the `PhoneBook` class, you can move on to the user interface, and see if everything still works as expected.
class Person:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__numbers = []
        self.__address = None
    
    def name(self) -> str:
        return self.__name
    
    def numbers(self) -> str:
        return self.__numbers
    
    def address(self) -> str:
        return self.__address
    
    def add_number(self, number: str):
        self.__numbers.append(number)
    
    def add_address(self, address: str):
        self.__address = address
    
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)        
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
        
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)        

    def search(self):
        name = input("name: ")
        entry = self.__phonebook.get_entry(name)
        if entry is None:
            print("number unknown")
            print("address unknown")
            return
        if len(entry.numbers()) == 0:
            print("number unknown") 
        else:
            for number in entry.numbers():
                print(number)
        if entry.address() is None:
            print("address unknown")
        else:
            print(entry.address())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()

# Part 2 Test:
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_entry("Eric"))
print(phonebook.get_entry("Emily"))

# Part 3: Adding an Address

# Please implement the functionality for adding an address to an entry in your phone book. 
class Person:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__numbers = []
        self.__address = None
    
    def name(self) -> str:
        return self.__name
    
    def numbers(self) -> str:
        return self.__numbers
    
    def address(self) -> str:
        return self.__address
    
    def add_number(self, number: str):
        self.__numbers.append(number)
    
    def add_address(self, address: str):
        self.__address = address
    
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)        
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
        
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)        

    def search(self):
        name = input("name: ")
        entry = self.__phonebook.get_entry(name)
        if entry is None:
            print("number unknown")
            print("address unknown")
            return
        if len(entry.numbers()) == 0:
            print("number unknown") 
        else:
            for number in entry.numbers():
                print(number)
        if entry.address() is None:
            print("address unknown")
        else:
            print(entry.address())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()

# Phone book expansion, version 2 - Approach 2
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None
 
    def name(self):
        return self.__name
 
    def numbers(self):
        return self.__numbers
 
    def add_number(self, number: str):
        self.__numbers.append(number)
 
    def address(self):
        return self.__address
 
    def add_address(self, address: str):
        self.__address = address
 
class PhoneBook:
    def __init__(self):
        self.__persons = {}
 
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
 
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)
 
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
 
    def all_entries(self):
        return self.__persons
 
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
 
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")
 
 
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)
 
    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
 
    def search(self):
        name = input("name: ")
        data = self.__phonebook.get_entry(name)
        if data==None:
            print("number unknown")
            print("address unknown")
            return
 
        numbers = data.numbers()
        if len(numbers)==0:
            print("number unknown") 
        else: 
            for number in numbers:
                print(number)
 
        address = data.address()
        if address!=None:
            print(address)
        else:
            print("address unknown")
 
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

# CourseRecords - Approach 1
# Please write an interactive application for keeping track of your studies. 
# The internal structure is up to you, but this would be a good opportunity to practice creating a similar structure as in the PhoneBook example above.

# Each course name should result in a single entry in the records. 
# A grade may be raised by re-entering the course details, but the grade should never be lowered.

# Your program should work as follows:
'''
1 add course
2 get course data
3 statistics
0 exit

command: **1**
course: **ItP**
grade: **3**
credits: **5**

command: **2**
course: **ItP**
ItP (5 cr) grade 3

command: **1**
course: **ItP**
grade: **5**
credits: **5**

command: **2**
course: **ItP**
ItP (5 cr) grade 5

command: **1**
course: **ItP**
grade: **1**
credits: **5**

command: **2**
course: **ItP**
ItP (5 cr) grade 5

command: **2**
course: **Introduction to Java**
no entry for this course

command: **1**
course: **ACiP**
grade: **1**
credits: **10**

command: **1**
course: **ItAI**
grade: **2**
credits: **5**

command: **1**
course: **Algo101**
grade: **4**
credits: **1**

command: **1**
course: **CompModels**
grade: **5**
credits: **8**

command: **3**
5 completed courses, a total of 29 credits
mean 3.4
grade distribution
5: xx
4: x
3:
2: x
1: x

command: **0**
'''

class Course:
    def __init__(self, name: str, grade: int, credit: int) -> None:
        self.__name = name
        self.__grade = grade
        self.__credit = credit
    
    def name(self) -> str:
        return self.__name
    
    def grade(self) -> int:
        return self.__grade
    
    def credit(self) -> int:
        return self.__credit

class CourseRecords:
    def __init__(self) -> None:
        self.__courserecord = {}
    
    def add_course(self, name: str, grade: int, credit: int):
        if name not in self.__courserecord:
            self.__courserecord[name] = Course(name, grade, credit)
        elif grade > self.__courserecord[name].grade():
            self.__courserecord[name] = Course(name, grade, credit)
    
    def course_data(self, name: str):
        if name in self.__courserecord:
            print(f"{name} ({self.__courserecord[name].credit()} cr) grade {self.__courserecord[name].grade()}")
        else:
            print("no entry for this course")
            
    def statistics(self):
        total_completed = len(self.__courserecord)
        total_credit = 0
        sum_grade = 0
        grade_list = []
        for entry in self.__courserecord.values():
            total_credit += entry.credit()
            sum_grade += entry.grade()
            grade_list.append(entry.grade())
        mean = sum_grade / total_completed
        print(f"{total_completed} completed courses, a total of {total_credit} credits")
        print(f"mean {mean:0.1f}")
        print("grade distribution")
        line = ""
        for i in range(5, 0, -1):
            x = "x" * grade_list.count(i)
            line += f"{i}: {x}\n"
        print(line[:-1])

class CourseApplication:
    def __init__(self):
        self.__courseapp = CourseRecords()
        
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credit: "))
        self.__courseapp.add_course(course, grade, credit)
    
    def get_course_data(self):
        course = input("course: ")
        self.__courseapp.course_data(course)
    
    def get_statistics(self):
        self.__courseapp.statistics()
        
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()
            else:
                self.help()    


application = CourseApplication()
application.execute()


# CourseRecords - Approach 2
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name 
        self.__grade = grade
        self.__credits = credits
 
    def grade(self):
        return self.__grade
 
    def credits(self):
        return self.__credits
 
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
 
class StudyRecords:
    def __init__(self):
       self.courses = {}    
 
    def add_completion(self, course_name, grade, op):
        if course_name in self.courses and self.courses[course_name].grade() > grade:
            return
 
        self.courses[course_name] = Course(course_name, grade, op)
 
    def get_completion(self, course_name):
        if not course_name in self.courses:
            return None
 
        return self.courses[course_name]        
 
    def get_statistics(self):
        number_of_courses = len(self.courses)
        credits = 0
        sum_of_grades = 0
        grades = [0, 0, 0, 0, 0, 0, 0]
 
        for courses in self.courses.values():
            credits += courses.credits()
            sum_of_grades += courses.grade()
            grades[courses.grade()] += 1
        
        return {
            "number_of_courses": number_of_courses,
            "credits": credits,
            "average": sum_of_grades / number_of_courses,
            "grades": grades
        }
 
class Application:
    def __init__(self):
        self.register = StudyRecords()     
 
    def ohje(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
 
    def new_completion(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        op = int(input("credits: "))
        self.register.add_completion(course_name, grade, op)
 
    def get_completion(self):
        course_name = input("course: ")
        courses = self.register.get_completion(course_name)
        if courses is None:
            print("no entry for this course")
        else:
            print(courses)        
 
    def statistics(self):
        t = self.register.get_statistics() 
 
        print(f"{t['number_of_courses']} completed courses, a total of {t['credits']} credits")
        print(f"mean {t['average']:.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            grade_hits = t['grades'][i]
            row = "x"*grade_hits
            print(f"{i}: {row}")        
 
    def execute(self):
        self.ohje()
 
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command=="1":
                self.new_completion()
            elif command=="2":
                self.get_completion()
            elif command=="3":
                self.statistics()
 
Application().execute()

# Epilogue

# To finish off this part of the material, let's return to the user interface of the phone book example for a moment.

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

    # the rest of the program

application = PhoneBookApplication()
application.execute()

# A `PhoneBookApplication` object contains both a `PhoneBook` object and a `FileHandler` object. 
# The name of the file passed to the FileHandler is, at the moment, hard-coded into the `PhoneBookApplication` class. 
# This is a completely irrelevant detail when it comes to the _user interface_ of the application. 
# In fact, it breaks the _separation of concerns_ principle: where a `PhoneBook` object saves its contents should be of no concern to a `PhoneBookApplication`, 
# yet if we wanted to change the location, we'd have to change the code of `PhoneBookApplication`.

# It would be a better idea to create a FileHandler object somewhere _outside_ the `PhoneBookApplication` class, and pass it as an argument to the application:
class PhoneBookApplication:
    def __init__(self, storage_service):
        self.__phonebook = PhoneBook()
        self.__storage_service = storage_service

    # the rest of the user interface

# create a FileHandler
storage_service = FileHandler("phonebook.txt")
# pass it as an argument to PhoneBookApplication's constructor
application = PhoneBookApplication(storage_service)
application.execute()

# This removes an _unnecessary dependency_ from the `PhoneBookApplication` class. 
# If the name of the file changes, the user interface no longer needs to be changed. 
# We just need to pass a different argument to the constructor:
class PhoneBookApplication:
    def __init__(self, filename):
        self.__phonebook = PhoneBook()
        self.__filename = filename

    # the rest of the user interface

# use a different filename
storage_service = FileHandler("new_phonebook.txt")
application = PhoneBookApplication(storage_service)
application.execute()

# This change also allows us to consider more exotic storage locations, for instance, a cloud service on the internet. 
# We just need to implement a class which uses the cloud service, and offers `PhoneBookApplication` the exact same methods as `FileHandler`.

# An instance of this new "cloud handler" class can be passed as an argument to the constructor, and not a single line of code has to be changed in the user interface:
class CloudHandler:
    # code for saving the contents of the phone book
    # in a cloud service on the internet

storage_service = CloudHandler("amazon-cloud", "username", "passwrd")
application = PhoneBookApplication(storage_service)
application.execute()

# As you have seen before, using techniques like this carries a price tag, as there is more code to write, so a programmer needs to consider whether that is an acceptable tradeoff.

# The technique outlined above is called _dependency injection_. 
# As the name implies, the idea is to provide any dependency required by an object from _outside_ the object. 
# It is a very useful tool in a programmer's toolbox, as it makes it easier to implement new features in programs and facilitates automatic testing. 