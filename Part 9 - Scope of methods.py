# Scope of methods

# The methods defined within a class can be hidden in exactly the same way as the attributes were in the previous section. 
# If the method begins with two underscores `__`, it is not directly accessible by the client.

# So, the technique is the same for both methods and attributes, but the use cases are usually a little different. 
# Private attributes often come paired with getter and setter methods for controlling access to them. 
# Private methods, on the other hand, are usually intended for internal use only, as helper methods for processes which the client does not need to know about.

# A private method can be used within the class just like any other method, of course remembering to include the `self` prefix. 
# The following is a simple class representing the recipient of email letters. 
# It includes a private helper method for checking the email address is in a valid format:

class Recipient:
    def __init__(self, name: str, email: str):
        self.__name = name
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("The email address is not valid")

    def __check_email(self, email: str):
        # A simple check: the address must be over 5 characters long 
        # and contain a dot and an @ character
        return len(email) > 5 and "." in email and "@" in email

# Attempting to call the private method directly causes an error:
peter = Recipient("Peter Emailer", "peter@example.com")
peter.__check_email("someone@example.com")

# Within the class the method can be accessed normally, and it makes sense to use it also for setting a new value for the address. 
# Let's add getter and setter methods for the email address:

class Recipient:
    def __init__(self, name: str, email: str):
        self.__name = name
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("The email address is not valid")

    def __check_email(self, email: str):
        # A simple check: the address must be over 5 characters long 
        # and contain a dot and an @ character
        return len(email) > 5 and "." in email and "@" in email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("The email address is not valid")

# Python scope and namespace

# We have defined _scope_ as the sections of a program where a (variable) name is visible or available.
# Looking at the term from another direction, it also refers to what is visible from a specific point in program code.
# Another related term is _namespace_, which refers to the names specifically available within a defined Python unit, such as a class or a function definition.

# The scope within a method is different from the scope within a class, which is again different from the scope at the client code which creates an instance of the class. 
# A method has access to its local variables, but also to the attributes and other methods in the class it is a part of, even if they are private. 
# The class also has access to these, its own members, but it cannot directly access the local variables within its methods. 
# The client code has access to only the public methods and attributes defined in the class, but of course also some other names in the environment in which it exists.

# It may seem counter-intuitive that a class would not have access to all its contents, but it is essential for ensuring integrity. 
# For example, it might make sense to use the same local variable name in various different methods within the same class, if they perform somehow similar functionalities. 
# If the class had direct access to all of the local variables within the methods, they would have to be named differently, or else it would not be clear which version of the variable was meant where. 
# We have already seen with attributes declared with `self` that helper variables should not be made accessible outside a method, so adding the variables as attributes or global variables should not be an option. 
# There has to be a way to keep names in different parts of the program separate, and this is what namespaces are for.

# The idea of a namespace helps with understanding how the same name can happily coexist in different functions, classes or modules at the same time. 
# If a name is specific to a namespace, such as a method definition, it is not directly accessible outside it, and so there is no reason why another namespace could not use the same name. 
# Mastering namespaces and scopes is essential in becoming a proficient programmer, and you will get much practice on this course.

# Do I need a private method?

# In the following example the class `DeckOfCards` is a model for a deck of 52 cards. 
# It contains the helper method `__reset_deck`, which creates a new shuffled deck of cards. 
# The private method is at the moment only called in the constructor method, so the implementation could arguably be placed directly in the constructor. 
# However, using a separate method makes the code easier to read and also makes it possible to access the functionality later in other methods if necessary.

from random import shuffle

class DeckOfCards:
    def __init__(self):
        self.__reset_deck()

    def __reset_deck(self):
        self.__deck = []
        # Add all 52 cards to the deck
        suits = ["spades", "hearts", "clubs", "diamonds"]
        for suit in suits:
            for number in range(1, 14):
                self.__deck.append((suit, number))
        # Shuffle the deck
        shuffle(self.__deck)

    def deal(self, number_of_cards: int):
        hand = []
        # Move the top cards in the deck to the hand
        for i in range(number_of_cards):
            hand.append(self.__deck.pop())
        return hand


deck = DeckOfCards()
hand1 = deck.deal(5)
print(hand1)
hand2 = deck.deal(5)
print(hand2)

# Shuffle formula
def shuffle_deck():
    deck = []
    suits = ["spades", "hearts", "clubs", "diamonds"]
    for suit in suits:
        for number in range(1, 14):
            deck.append((suit, number))
    shuffle(deck)
    return deck

deck = shuffle_deck()
len(deck)
print(deck)

# Private methods are generally less common than private attributes. 
# As a rule of thumb, a method should be hidden whenever the client has no need to directly access it. 
# This is especially the case when it is possible that the client could adversely affect the integrity of the object by calling the method.

# Service charge - Apporach 1

# Please create a class named `BankAccount` which models a bank account. 
# The class should contain:
    # a constructor which takes the name of the owner (str), account number (str) and balance (float) as arguments
    # a method `deposit(amount: float)` for depositing money to the account
    # a method `withdraw(amount: float)` for withdrawing money from the account
    # a getter method `balance` which returns the balance of the account

# The class should also contain the private method
    # `__service_charge()`, which decreases the balance on the account by one percent. 
    # Whenever either of the methods `deposit` or `withdraw` is called, this method should also be called. 
    # The service charge is calculated and subtracted only after the actual operation is completed (that is, after the amount specified has been added to or subtracted from the balance).

# All data attributes within the class definition should be private.

class BankAccount:
    def __init__(self, owner: str, acount_number: str, balance: float) -> None:
        self.__owner = owner
        self.__acount = acount_number
        self.__balance = balance
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()
    
    def __service_charge(self):
        self.__balance *= (1 - 0.01)

account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)

# Service charge - Approach 2
class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance
 
    def __service_charge(self):
        self.__balance *= 0.99
 
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()
 
    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()
 
    @property
    def balance(self):
        return self.__balance