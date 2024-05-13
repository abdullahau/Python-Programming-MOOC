# Access modifiers

# If a trait is defined as private in the base class, it is not directly accessible in any derived classes. 

# Let's take a look at an example. 
# In the `Notebook` class below the notes are stored in a list, and the list attribute is private:
class Notebook:
    """ A Notebook stores notes in string format """

    def __init__(self):
        # private attribute
        self.__notes = []

    def add_note(self, note):
        self.__notes.append(note)

    def retrieve_note(self, index):
        return self.__notes[index]

    def all_notes(self):
        return ",".join(self.__notes)

# If the integrity of the class is key, making the list attribute `notes` private makes sense. 
# The class provides the client with suitable methods for adding and browsing notes, after all. 
# This approach becomes problematic if we define a new class `NotebookPro`, which inherits the `Notebook` class. 
# The private list attribute is not accessible to the client, but neither is it accessible to the derived classes. 
# If we try to access it, as in the `find_notes` method below, we get an error:

class NotebookPro(Notebook):
    """ A better Notebook with search functionality """
    def __init__(self):
        # This is OK, the constructor is public despite the underscores
        super().__init__()

    # This causes an error
    def find_notes(self, search_term):
        found = []
        # the attribute __notes is private
        # the derived class can't access it directly
        for note in self.__notes:
            if search_term in note:
                found.append(note)

        return found

# Protected traits

# Many object oriented programming languages have a feature, usually a special keyword, for _protecting_ traits. 
# This means that a trait should be hidden from the clients of the class, but kept accessible to its subclasses. 
# Python in general abhors keywords, so no such feature is directly available in Python. 
# Instead, there is a _convention_ of marking protected traits in a certain way. 

# Remember, a trait can be hidden by prefixing its name with two underscores:
def __init__(self):
    self.__notes = []

# The agreed convention to _protect_ a trait is to prefix the name with a _single_ underscore. 
# Now, this is _just_ a convention. Nothing prevents a programmer from breaking the convention, but it is considered a bad programming practice.
def __init__(self):
    self._notes = []

# Below we have the entire Notebook example, with protected `_notes` instead of private `__notes`:
class Notebook:
    """ A Notebook stores notes in string format """

    def __init__(self):
        # protected attribute
        self._notes = []

    def add_note(self, note):
        self._notes.append(note)

    def retrieve_note(self, index):
        return self._notes[index]

    def all_notes(self):
        return ",".join(self._notes)

class NotebookPro(Notebook):
    """ A better Notebook with search functionality """
    def __init__(self):
        # This is OK, the constructor is public despite the underscores
        super().__init__()

    # This works, the protected attribute is accessible to the derived class
    def find_notes(self, search_term):
        found = []
        for note in self._notes:
            if search_term in note:
                found.append(note)

        return found

# Below we have a handy table for the visibility of attributes with different access modifiers:
# Access modifier | Example       | Visible to client | Visible to derived class
# :--------------:|:-------------:|:-----------------:|:------------------------:
# Public          | `self.name`   | yes               | yes
# Protected       | `self._name`  | no                | yes
# Private         | `self.__name` | no                | no


# Access modifiers work the same with all traits: attributes and methods. 
# For example, in the `Person` class below we have the protected method `capitalize_initials`. 
# It can be used from the derived class `Footballer`:

class Person:
    def __init__(self, name: str):
        self._name = self._capitalize_initials(name)

    def _capitalize_initials(self, name):
        name_capitalized = []
        for n in name.split(" "):
            name_capitalized.append(n.capitalize())

        return " ".join(name_capitalized)

    def __repr__(self):
        return self.__name

class Footballer(Person):

    def __init__(self, name: str, nickname: str, position: str):
        super().__init__(name)
        # the method is available as it is protected in the base class
        self.__nickname = self._capitalize_initials(nickname)
        self.__position = position

    def __repr__(self):
        r =  f"Footballer - name: {self._name}, nickname: {self.__nickname}"
        r += f", position: {self.__position}"
        return r

# Test the classes
if __name__ == "__main__":
    jp = Footballer("peter pythons", "pyper", "forward")
    print(jp)
    
# Supergroup

# The exercise template contains the class definition for a `SuperHero`.

# Please define a class named `SuperGroup` which represents a group of superheroes. 
# The class should contain the following members:
    # **Protected** attributes name (str), location (str) and members (list)
    # A constructor which takes the name and location of the group as arguments, in that order
    # Getter methods for the name and location attributes
    # A method named `add_member(hero: SuperHero)` which adds a new member to the group
    # A method named `print_group` which prints out information about the group and its members, following the format specified below

class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup(SuperHero):
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []
        
    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location
    
    def add_member(self, hero: SuperHero):
        self._members.append(hero)
        
    def print_group(self):
        print(f"{self._name}, {self._location}\nMembers:")
        for heroes in self._members:
            print(heroes)

superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
invisible = SuperHero("Invisible Inca", "Invisibility")
revengers = SuperGroup("Revengers", "Emerald City")

revengers.add_member(superperson)
revengers.add_member(invisible)
revengers.print_group()

# Secret magic potion

# The exercise template contains the class definition for a `MagicPotion` which allows you to save a recipe for a magic potion. 
# The class definition contains a constructor along with the methods
    # `add_ingredient(ingredient: str, amount: float)` and
    # `print_recipe()`

# Please define a class named `SecretMagicPotion` which inherits the `MagicPotion` class and allows you to also protect the recipe with a password.

# The new class should have a constructor which also takes the password string as an argument.

# The class should also contain the following methods:
    # `add_ingredient(ingredient: str, amount: float, password: str)`
    # `print_recipe(password: str)`

# If the password argument given to either of these methods is wrong, the methods should raise a `ValueError` exception.

# If the password is correct, each method should call the relevant method in the parent class. 
# Do not copy and paste anything from the MagicPotion class.

class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self.__password = password
    
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__password:
            self._ingredients.append((ingredient, amount))
        else:
            raise ValueError("Wrong password!")
    
    def print_recipe(self, password: str):
        if password == self.__password:
            print(f"{self._name}:")
            for ingredient in self._ingredients:
                print(f"{ingredient[0]} {ingredient[1]} grams")
        else:
            raise ValueError("Wrong password!")

diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")

diminuendo.print_recipe("pocushocus") # WRONG password!

# Secret Magic Portion - Approach 2
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []
 
    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))
    
    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")
 
 
class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self.__password = password
 
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__password:
            super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Wrong password!")
 
    def print_recipe(self, password: str):
        if password == self.__password:
            super().print_recipe()
        else:
            raise ValueError("Wrong password!")

diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")

# Secret Magic Portion - Approach 3
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self.__password = password
    
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__password:
            self._ingredients.append((ingredient, amount))
        else:
            raise ValueError("Wrong password!")
    
    def print_recipe(self, password: str):
        if password == self.__password:
            super().print_recipe()
        else:
            raise ValueError("Wrong password!")

diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")