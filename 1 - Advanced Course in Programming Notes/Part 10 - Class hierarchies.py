# Class hierarchies

# Special classes for special purposes

# Sometimes you come across a situation where you have already defined a class, but then realize you need special traits in some, but not all, instances of the class. 
# Then again, sometimes you realize you've defined two very similar classes with only minor differences. 
# As programmers we aim to always repeat ourselves as little as possible, while maintaining clarity and readability. 
# So how can we accommodate for different implementations of intrinsically similar objects?

# Let's have a look at two class definitions: `Student` and `Teacher`. 
# Getter and setter methods have been left out for now, in order to keep the example short.

class Student:

    def __init__(self, name: str, id: str, email: str, credits: str):
        self.name = name
        self.id = id
        self.email = email
        self.credits = credits

class Teacher:

    def __init__(self, name: str, email: str, room: str, teaching_years: int):
        self.name = name
        self.email = email
        self.room = room
        self.teaching_years = teaching_years
        
# Even in a stripped down example, like the above, we already have quite a bit of repetition: both classes contain attributes `name` and `email`. 
# It would be a good idea to have a single attribute definition, so that a single function would suffice for editing both attributes. 

# For example, imagine the school's email address changed. All addresses would have to be updated. 
# We _could_ write two separate versions of essentially the same function:

def update_email(o: Student):
    o.email = o.email.replace(".com", ".edu")

def update_email2(o: Teacher):
    o.email = o.email.replace(".com", ".edu")
    

# Writing practically the same thing twice is unnecessary repetition, not to mention it doubles the possibilities for errors. 
# It would be a definite improvement if we could use a single function to work with instances of both classes.

# Both classes also have attributes which are unique to them. 
# Simply combining _all_ attributes in a single class would mean _all_ instances of the class would then have unnecessary attributes, just different ones for different instances. 
# That doesn't seem like an ideal situation, either.

# Inheritance

# Object oriented programming languages usually feature a technique called _inheritance_. 
# A class can _inherit_ the traits of another class. 
# In addition to these inherited traits a class can also contain traits which are unique to it.

# Knowing this, it would make sense for the `Teacher` and `Student` classes to have a common base or parent class `Person`:

class Person:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        
# The new class contains those traits which are shared by the other two classes. 
# Now `Student` and `Teacher` can _inherit_ these traits and add their own besides.

# The syntax for inheritance simply involves adding the base class name in parentheses on the header line:

class Person:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def update_email_domain(self, new_domain: str):
        old_domain = self.email.split("@")[1]
        self.email = self.email.replace(old_domain, new_domain)


class Student(Person):

    def __init__(self, name: str, id: str, email: str, credits: str):
        self.name = name
        self.id = id
        self.email = email
        self.credits = credits


class Teacher(Person):

    def __init__(self, name: str, email: str, room: str, teaching_years: int):
        self.name = name
        self.email = email
        self.room = room
        self.teaching_years = teaching_years

if __name__ == "__main__":
    saul = Student("Saul Student", "1234", "saul@example.com", 0)
    saul.update_email_domain("example.edu")
    print(saul.email)

    tara = Teacher("Tara Teacher", "tara@example.fi", "A123", 2)
    tara.update_email_domain("example.ex")
    print(tara.email)

# Both `Student` and `Teacher` inherit the `Person` class, so both have the traits defined in the `Person` class, including the method `update_email_domain`. 
# The same method works for instances of both the derived classes.

# Let's have a look at another example. We have a `Bookshelf` which inherits the class `BookContainer`:
class Book:
    """ This class models a simple book """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class BookContainer:
    """ This class models a container for books """

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.name} ({book.author})")


class Bookshelf(BookContainer):
    """ This class models a shelf for books """

    def __init__(self):
        super().__init__()

    def add_book(self, book: Book, location: int):
        self.books.insert(location, book)

# The class `Bookshelf` contains the method `add_book`. 
# A method with the same name is defined in the base class `BookContainer`. 
# This is called _overriding_: if a derived class has a method with the same name as the base class, the derived version overrides the original in instances of the derived class.

# The idea in the example above is that a new book added to a BookContainer always goes to the top, but with a Bookshelf you can specify the location yourself. 
# The method `list_books` works the same for both classes, as there is no overriding method in the derived class.

# Side note: list `.insert()` method
# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')

print('List:', vowel)

# Output: List: ['a', 'e', 'i', 'o', 'u']

# Let's try out these classes:

class Book:
    """ This class models a simple book """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class BookContainer:
    """ This class models a container for books """

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.name} ({book.author})")


class Bookshelf(BookContainer):
    """ This class models a shelf for books """

    def __init__(self):
        super().__init__()

    def add_book(self, book: Book, location: int):
        self.books.insert(location, book)


if __name__ == "__main__":
    # Create some books for testing
    b1 = Book("Old Man and the Sea", "Ernest Hemingway")
    b2 = Book("Silent Spring", "Rachel Carson")
    b3 = Book("Pride and Prejudice", "Jane Austen")

    # Create a BookContainer and add the books
    container = BookContainer()
    container.add_book(b1)
    container.add_book(b2)
    container.add_book(b3)

    # Create a Bookshelf and add the books (always to the beginning)
    shelf = Bookshelf()
    shelf.add_book(b1, 0)
    shelf.add_book(b2, 0)
    shelf.add_book(b3, 0)


    # Tulostetaan
    print("Container:")
    container.list_books()

    print()

    print("Shelf:")
    shelf.list_books()

# So, the Bookshelf class also has access to the `list_books` method. 
# Through inheritance the method is a member of all the classes derived from the `BookContainer` class.

# Inheritance and scope of traits

# A derived class inherits all traits from its base class. 
# Those traits are directly accessible in the derived class, unless they have been defined as private in the base class (with two underscores before the name of the trait).

# As the attributes of a Bookshelf are identical to a BookContainer, there was no need to rewrite the constructor of Bookshelf. 
# We simply called the constructor of the base class:
class Bookshelf(BookContainer):

    def __init__(self):
        super().__init__()

# Any trait in the base class can be accessed from the derived class with the function `super()`. 
# The `self` argument is left out from the method call, as Python adds it automatically.

# But what if the attributes are not identical; can we still use the base class constructor in some way? 
# Let's have a look at a class named `Thesis` which inherits the `Book` class. 
# The derived class _can_ still call the constructor from the base class:

class Book:
    """ This class models a simple book """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class Thesis(Book):
    """ This class models a graduate thesis """

    def __init__(self, name: str, author: str, grade: int):
        super().__init__(name, author)
        self.grade = grade

# The constructor in the `Thesis` class calls the constructor in the base class `Book` with the arguments for `name` and `author`. 
# Additionally, the constructor in the derived class sets the value for the attribute `grade`. 
# This naturally cannot be a part of the base class constructor, as the base class has no such attribute.

class Book:
    """ This class models a simple book """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class Thesis(Book):
    """ This class models a graduate thesis """

    def __init__(self, name: str, author: str, grade: int):
        super().__init__(name, author)
        self.grade = grade


if __name__ == "__main__":
    thesis = Thesis("Python and the Universe", "Peter Pythons", 3)

    # Print out the values of the attributes
    print(thesis.name)
    print(thesis.author)
    print(thesis.grade)

# Even if a derived class _overrides_ a method in its base class, the derived class can _still_ call the overridden method in the base class. 
# In the following example we have a basic `BonusCard` and a special `PlatinumCard` for especially loyal customers. 
# The `calculate_bonus` method is overridden in the derived class, but the overriding method calls the base method:

class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class BonusCard:

    def __init__(self):
        self.products_bought = []

    def add_product(self, product: Product):
        self.products_bought.append(product)

    def calculate_bonus(self):
        bonus = 0
        for product in self.products_bought:
            bonus += product.price * 0.05

        return bonus

class PlatinumCard(BonusCard):

    def __init__(self):
        super().__init__()

    def calculate_bonus(self):
        # Call the method in the base class
        bonus = super().calculate_bonus()

        # ...and add five percent to the total
        bonus = bonus * 1.05
        return bonus

# So, the bonus for a 'PlatinumCard' is calculated by calling the overriden method in the base class, and then adding an extra 5 percent to the base result. 
# An example of how these classes are used:

if __name__ == "__main__":
    card = BonusCard()
    card.add_product(Product("Bananas", 6.50))
    card.add_product(Product("Satsumas", 7.95))
    bonus = card.calculate_bonus()

    card2 = PlatinumCard()
    card2.add_product(Product("Bananas", 6.50))
    card2.add_product(Product("Satsumas", 7.95))
    bonus2 = card2.calculate_bonus()

    print(bonus)
    print(bonus2)
    
# Laptop computer

# The exercise template contains a class definition for a `Computer`, which has the attributes `model` and `speed`.
# Please define a class named `LaptopComputer` which _inherits_ the class `Computer`. 
# The constructor of the new class should take a third argument: `weight`, of type integer.

# Please also include a `__str__` method in your class definition. 

class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self.__weight = weight
    
    def __str__(self):
        return f'{super().model}, {super().speed} MHz, {self.__weight} kg'
    
laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)

# Game Museum

# The exercise template contains class definitions for a `ComputerGame` and a `GameWarehouse`. 
# A GameWarehouse object is used to store ComputerGame objects.

# Please familiarize yourself with these classes. 
# Then define a new class named `GameMuseum` which inherits the `GameWarehouse` class.

# The GameMuseum class should _override_ the `list_games()` method, so that it returns a list of only those games which were made before the year 1990.

# The new class should also have a constructor which _calls the constructor from the parent class `GameWarehouse`_. The constructor takes no arguments.

class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games

# list Comprehension Approach 
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()
    
    def list_games(self):
        return [game for game in super().list_games() if game.year < 1990]

# Approach 2
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()
 
    def list_games(self):
        gamelist = []
        for game in super().list_games():
            if game.year < 1990:
                gamelist.append(game)
 
        return gamelist

museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
for game in museum.list_games():
    print(game.name)

# Areas

# The exercise template contains a class definition for a `Rectangle`. 
# It represents a [rectangle shape](https://en.wikipedia.org/wiki/Rectangle). 

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

# A Rectangle works like this:
rectangle = Rectangle(2, 3)
print(rectangle)
print("area:", rectangle.area())

# Part 1: Square

# Please define a class named `Square` which inherits the `Rectangle` class. 
# The sides of a [square](https://en.wikipedia.org/wiki/Square) are all of equal length, which makes the square a special case of the rectangle. 
# The new class should not contain any new attributes.

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self, side: int):
        # Provide the side as width and height for the
        # superclass constructor
        super().__init__(width=side, height=side)
        
    def __str__(self):
        # Given that the attribute 'width' and 'height' are inherited from the suprtclass during intantiation
        # 'self.width' and 'self.height' attribuees can be called directly for th instance
        return f"square {self.width}x{self.height}"
    
square = Square(4)
print(square)
print("area:", square.area())

# Word game

# The exercise template contains the class definition for a `WordGame`. 
# It provides some basic functionality for playing different word-based games:

import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

'''
Word game:
round 1
player1: longword
player2: ??
player 2 won
round 2
player1: i'm the best
player2: wut?
player 1 won
round 3
player1: who's gonna win
player2: me
player 1 won
game over, wins:
player 1: 2
player 2: 1
'''

# In this "basic" version of the game the winner is determined randomly. 
# The input from the players has no effect on the result.

# Part 1: Longest word wins

# Please define a class named `LongestWord`. 
# It is a version of the game where whoever types in the longest word on each round wins.

# The new version of the game is implemented by _inheriting_ the `WordGame` class. 
# The `round_winner` method should also be suitably overridden. 

import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1 
        elif len(player1_word) < len(player2_word):
            return 2

p = LongestWord(3)
p.play()

# Part 2: Most vowels wins

# Please define another WordGame class named `MostVowels`. 
# In this version of the game whoever has squeezed more vowels into their word wins the round.

import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1 
        elif len(player1_word) < len(player2_word):
            return 2

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouAEIOU"
        player1_vowels = [character for character in player1_word if character in vowels]
        player2_vowels = [character for character in player2_word if character in vowels] 
        if len(player1_vowels) > len(player2_vowels):
            return 1
        elif len(player1_vowels) < len(player2_vowels):
            return 2

# Part 3: Rock paper scissors

# Finally, please define a class named `RockPaperScissors` which allows you to play a game of [rock paper scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors).
# The rules of the game are as follows:
    # - rock beats scissors (the rock can break the scissors but the scissors can't cut the rock)
    # - paper beats rock (the paper can cover the rock)
    # - scissors beats paper (the scissors can cut the paper)

# If the input from either player is invalid, they lose the round. 
# If both players type in something else than _rock_, _paper_ or _scissors_, the result is a tie.

import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1 
        elif len(player1_word) < len(player2_word):
            return 2

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouAEIOU"
        player1_vowels = [character for character in player1_word if character in vowels]
        player2_vowels = [character for character in player2_word if character in vowels] 
        if len(player1_vowels) > len(player2_vowels):
            return 1
        elif len(player1_vowels) < len(player2_vowels):
            return 2

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        rps_dict = {"rock paper": 2, 
                    "rock scissors": 1, 
                    "rock rock": None,
                    "paper rock": 1,
                    "paper scissors": 2,
                    "paper paper": None,
                    "scissors rock": 2,
                    "scissors paper": 1,
                    "scissors scissors": None}
        rps_list = ["rock", "paper", "scissors"]
        if player1_word in rps_list and player2_word in rps_list:
            return rps_dict[f"{player1_word} {player2_word}"]
        elif player1_word not in rps_list and player2_word in rps_list:
            return 2
        elif player1_word in rps_list and player2_word not in rps_list:
            return 1

p = RockPaperScissors(4)
p.play()

# Word game - Approach 2
import random
 
class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds
 
    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)
 
    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
 
            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie
 
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")
 
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            # Any number can be returned for tie according to
            # definition
            return 0
 
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    #  Help method for calculating the vowels
    def count_vowels(self, word: str):
        vok = "aeiouyåöäö"
        vowels = 0
        for character in word:
            if character in vok:
                vowels += 1
        return vowels
 
 
    def round_winner(self, player1_word: str, player2_word: str):
        if self.count_vowels(player1_word) > self.count_vowels(player2_word):
            return 1
        elif self.count_vowels(player2_word) > self.count_vowels(player1_word):
            return 2
        else:
            return 0
 
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    def round_winner(self, player1_word: str, player2_word: str):
        choices = {"rock" : 0, "paper": 1, "scissors": 2}
        # Not good first
        if player1_word not in choices.keys() and player2_word not in choices.keys():
            return 0
 
        if player1_word not in choices.keys():
            return 2
 
        if player2_word not in choices.keys():
            return 1
 
        # Use dictionary to calculate the difference between
        # choices. For example: player 1 selects paper, value is 1
        # player2 selects rock, value is 0
        # player 1 wins when the difference is 1 or -2
        # player 2 wins when the difference is -1 ot 2
        # 0 means that both selected the same choice
        difference = choices[player1_word] - choices[player2_word]
        
        if difference == 0:
            return 0
 
        if difference == 1 or difference == -2:
            return 1
 
        return 2