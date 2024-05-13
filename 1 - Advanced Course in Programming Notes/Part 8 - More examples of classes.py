# Example 1: the Rectangle class
# Let's have a look at a class which models a rectangle in two-dimensional space:
class Rectangle:
    def __init__(self, left_upper: tuple, right_lower: tuple):
        self.left_upper = left_upper
        self.right_lower = right_lower
        self.width = right_lower[0]-left_upper[0]
        self.height = right_lower[1]-left_upper[1]

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def move(self, x_change: int, y_change: int):
        corner = self.left_upper
        self.left_upper = (corner[0]+x_change, corner[1]+y_change)
        corner = self.right_lower
        self.right_lower = (corner[0]+x_change, corner[1]+y_change)
        
# A new 'Rectangle' is created with two tuples as arguments. 
# These tuples contain the x and y coordinates of the upper left corner and the lower right corner. 
# The constructor calculates the height and width of the rectangle based on these values.

# The methods 'area' and 'perimeter' calculate the area and perimeter of the rectangle based on the height and width. 
# The method 'move' moves the rectangle by the x and y values given as arguments.

# The rectanlge is represented in a coordinate system where the x coordinates increase from left to right, and the y coordinates increase from top to bottom. 
# This is a common way of handling coordinates in programming because it is often easier and more natural to consider the top left corner of the computer screen as the point where x and y equal zero.

# The following program tests the 'Rectangle' class:
rectangle = Rectangle((1, 1), (4, 3))
print(rectangle.left_upper)
print(rectangle.right_lower)
print(rectangle.width)
print(rectangle.height)
print(rectangle.perimeter())
print(rectangle.area())

rectangle.move(3, 3)
print(rectangle.left_upper)
print(rectangle.right_lower)

# Printing an object

# When you have an object created from a class defined by yourself, 
# the default reaction to calling the print command with that object as its argument is not very informative:
rectangle = Rectangle((1, 1), (4, 3))
print(rectangle)

# The printout should look a bit like this:
'''
<__main__.Rectangle object at 0x000002A908361D30>
'''

# Obviously, we want more control over what is printed out. 
# The easiest way to do this is to add a special '__str__' method to the class definition. 
# Its purpose is to return a snapshot of the state of the object in string format. 
# If the class definition contains a '__str__' method, the value returned by the method is the one printed out when the print command is executed.

# So, let's add a '__str__' method definition to our 'Rectangle' class:

class Rectangle:
    def __init__(self, left_upper: tuple, right_lower: tuple):
        self.left_upper = left_upper
        self.right_lower = right_lower
        self.width = right_lower[0]-left_upper[0]
        self.height = right_lower[1]-left_upper[1]

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def move(self, x_change: int, y_change: int):
        corner = self.left_upper
        self.left_upper = (corner[0]+x_change, corner[1]+y_change)
        corner = self.right_lower
        self.right_lower = (corner[0]+x_change, corner[1]+y_change)
        
    def __str__(self):
        return f"rectangle {self.left_upper} ... {self.right_lower}"

# Now the print command produces something more user-friendly:
rectangle = Rectangle((1, 1), (4, 3))
print(rectangle)

# The "__str__" method is perhaps more often used for formulating a string representation of the object with the 'str' function, as seen in the following program:
rectangle = Rectangle((1, 1), (4, 3))
str_rep = str(rectangle)
print(str_rep)

# There are many more special underscored methods which can be defined for classes. 
# One rather similar to the '__str__' method is the '__repr__' method. 
# '__repr__' method's purpose is to provide a technical representation of the state of the object.

# Stopwatch - Approach 1
# The exercise template contains the following skeleton for the 'Stopwatch' class:

# So, the method tick adds one second to the stopwatch. The maximum value for both seconds and minutes is 59. 
# Your class definition should also contain a '__str__' method, which returns a string representation of the state of the stopwatch.

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.counter = 0
    
    def tick(self):
        self.counter += 1
        hours, remainder = divmod(self.counter, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
        
        
    def __str__(self) -> str:
        return f"{self.minutes:02d}:{self.seconds:02d}"

# Please add to the class definition so that it works as follows:
watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()


# Compact way to get hours, minutes and seconds:
from datetime import timedelta as td

days = td.days
hours, remainder = divmod(td.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
# If you want to take into account fractions of a second
seconds += td.microseconds / 1e6

# Stopwatch - Approach 2
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
 
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
 
    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"
    
# Clock - Approach 1
# Please define a new class named 'Clock' which expands on the capabilities of your 'Stopwatch' class. 
# It should work as follows:
clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)

'''
23:59:55
23:59:56
23:59:57
23:59:58
23:59:59
00:00:00
00:00:01
12:05:00
'''

# As you can see above, the constructor should take initial values for the hours, minutes and seconds as arguments, and set these appropriately. 
# The 'tick' method adds one second to the clock. 
# The 'set' method sets new values for the hours and the minutes, and sets the seconds to zero.

class Clock:
    def __init__(self, hours:int, minutes:int, seconds:int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    
    def tick(self):
        self.seconds += 1
        total_seconds = self.seconds + (self.minutes*60) + (self.hours*60*60)
        days, remainder = divmod(total_seconds, 86400)
        self.hours, remainder = divmod(remainder, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
    
    def set(self, hour:int, minutes:int):
        self.hours = hour
        self.minutes = minutes
        self.seconds = 0
        
    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)

# Clock - Approach 2
class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
 
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
 
    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0
 
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# LunchCard - Approach 1

# At Unicafe, the student cafeteria at the University of Helsinki, students can pay for their lunch with a special debit card.
# In this exercise you will write a class called 'LunchCard', with the purpose of emulating the functions provided by the cafeteria's debit card.

# Part 1: The structure of the new class
# Please create a new class named 'LunchCard'.
# First write the constructor for the class. It should take the initial balance available on the card as an argument, and save it as an attribute. 
# Next, write a '__str__' method, which returns a string containing the balance: "The balance is X euros". 
# The available balance should be printed out with one decimal place precision.
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:0.1f} euros"

card = LunchCard(50)
print(card)

# Part 2: Paying for lunch
# Please implement the following methods in your 'LunchCard' class:
    # 'eat_lunch' subtracts 2.60 euros from the balance on the card
    # 'eat_special' subtracts 4.60 euros from the balance on the card

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
        
    def eat_lunch(self):
        self.balance = self.balance - 2.60 if self.balance >= 2.60 else self.balance
        
    def eat_special(self):
        self.balance = self.balance - 4.60 if self.balance >= 4.60 else self.balance

    def __str__(self):
        return f"The balance is {self.balance:0.1f} euros"

card = LunchCard(50)
print(card)

card.eat_lunch()
print(card)

card.eat_special()
card.eat_lunch()
print(card)

# Make sure the balance is never allowed to reach numbers below zero:
card = LunchCard(4)
print(card)

card.eat_lunch()
print(card)

card.eat_lunch()
print(card)

card.eat_special()
print(card)

# If there is not enough money on the card to pay for the lunch, the price of the lunch should not be subtracted from the balance.

# Part 3: Depositing money on the card
# Implement the 'deposit_money' method in your 'LunchCard' class.
# The method increases the balance on the card by the amount given as an argument.

# The method should account for arguments below zero by raising an exception of type 'ValueError':

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
        
    def deposit_money(self, deposit: float):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        else:
            self.balance += deposit
        
    def eat_lunch(self):
        self.balance = self.balance - 2.60 if self.balance >= 2.60 else self.balance
        
    def eat_special(self):
        self.balance = self.balance - 4.60 if self.balance >= 4.60 else self.balance

    def __str__(self):
        return f"The balance is {self.balance:0.1f} euros"


card = LunchCard(10)
print(card)
card.deposit_money(15)
print(card)
card.deposit_money(10)
print(card)
card.deposit_money(200)
print(card)


card = LunchCard(10)
card.deposit_money(-10)

# Part 4: Multiple cards

# Please write a main function which contains the following sequence of events:
    # Create a lunch card for Peter. The initial balance on the card is 20 euros.
    # Create a lunch card for Grace. The initial balance on the card is 30 euros.
    # Peter eats a special
    # Grace eats a regular lunch
    # Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
    # Peter deposits 20 euros
    # Grace eats the special
    # Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
    # Peter eats a regular lunch
    # Peter eats a regular lunch
    # Grace deposits 50 euros
    # Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
    
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
        
    def deposit_money(self, deposit: float):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        else:
            self.balance += deposit
        
    def eat_lunch(self):
        self.balance = self.balance - 2.60 if self.balance >= 2.60 else self.balance
        
    def eat_special(self):
        self.balance = self.balance - 4.60 if self.balance >= 4.60 else self.balance

    def __str__(self):
        return f"The balance is {self.balance:0.1f} euros"

# Create a lunch card for Peter. The initial balance on the card is 20 euros.
peters_card = LunchCard(20)
# Create a lunch card for Grace. The initial balance on the card is 30 euros.
graces_card = LunchCard(30)
# Peter eats a special
peters_card.eat_special()
# Grace eats a regular lunch
graces_card.eat_lunch()
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
print("Peter:", peters_card)
print("Grace:", graces_card)
# Peter deposits 20 euros
peters_card.deposit_money(20)
# Grace eats the special
graces_card.eat_special()
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
print("Peter:", peters_card)
print("Grace:", graces_card)
# Peter eats a regular lunch
peters_card.eat_lunch()
# Peter eats a regular lunch
peters_card.eat_lunch()
# Grace deposits 50 euros
graces_card.deposit_money(50)
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
print("Peter:", peters_card)
print("Grace:", graces_card)

# Example 2: Task list
tasks = [(10, "Complete project"), (1,"complete email"), (4, "walk dog")]
tasks.sort()
print(tasks)
top_priority = tasks.pop()
top_priority[1]

# The following class 'TaskList' models a list of tasks:
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name: str, priority: int):
        self.tasks.append((priority, name))

    def get_next(self):
        self.tasks.sort()
        # The list method pop removes and returns the last item in a list
        task = self.tasks.pop()
        # Return the name of the task (the second item in the tuple)
        return task[1]

    def number_of_tasks(self):
        return len(self.tasks)

    def clear_tasks(self):
        self.tasks = []
        
    def __str__(self) -> str:
        return f"{self.tasks}"
        
# The method 'add_task' adds a new task to the list. 
# Each task also has a priority attached, which is used for sorting the tasks. 
# The method 'get_next' removes and returns the task with the highest priority on the list. 
# There is also the 'number_of_tasks' method, which returns the number of tasks on the list, and finally the method 'clear_tasks', which clears the task list.

# Within the object, the tasks are stored in a list. 
# Each task is of a tuple containing the priority of the task and its name. 
# The priority value is stored first, so that when the list is sorted, the task with the highest priority is the last item on the list. 
# This is why we can then simply use the pop method to retrieve and remove the highest priority item.

# Please have a look at the following program with the task list in action:
tasks = TaskList()
tasks.add_task("studying", 50)
tasks.add_task("exercise", 60)
tasks.add_task("cleaning", 10)
print(tasks.number_of_tasks())
print(tasks.get_next())
print(tasks.number_of_tasks())
tasks.add_task("date", 100)
print(tasks.number_of_tasks())
print(tasks.get_next())
print(tasks.get_next())
print(tasks.number_of_tasks())
tasks.clear_tasks()
print(tasks.number_of_tasks())

# Series - Approach 1

# Part 1: A class named Series
# Please write a class named Series with the following functionality:
# The constructor should take the title, the number of seasons and a list of genres for the series as its arguments.

dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
print(dexter)

'''
Dexter (8 seasons)
genres: Crime, Drama, Mystery, Thriller
no ratings
'''

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        
    def __str__(self) -> str:
        return f'{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\nno ratings'


# 'join' method
# whenever you need to produce a string from a list containing strings, with a separating character of your choice in between the entries, you can use the 'join' method as follows:
genre_list = ["Crime", "Drama", "Mystery", "Thriller"]
genre_string = ", ".join(genre_list)
print(genre_string)

# Part 2: Adding reviews
# Please implement the method 'rate(rating: int)' which lets you add a rating between 0 and 5 to any series object. 
# You will also need to adjust the '__str__' method so that in case there are ratings, the method prints out the number of ratings added, and their average rounded to one decimal point.

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rates = []
    
    def rate(self, rating: int):
        self.rates.append(rating)
        
    def __str__(self) -> str:
        if len(self.rates) > 0:
            average = sum(self.rates)/len(self.rates)
            rating = f"{len(self.rates)} ratings, average {average:.1f} points"
        else:
            rating = "no ratings"
            
        return f'{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{rating}'

dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)

# Part 3: Searching for series
# Please implement these two functions which allow you to search through a list of series: 
# 'minimum_grade(rating: float, series_list: list)' and 'includes_genre(genre: str, series_list: list)'.

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rates = []
    
    def rate(self, rating: int):
        self.rates.append(rating)
        
    def __str__(self) -> str:
        if len(self.rates) > 0:
            average = sum(self.rates)/len(self.rates)
            rating = f"{len(self.rates)} ratings, average {average:.1f} points"
        else:
            rating = "no ratings"
            
        return f'{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{rating}'

# List comprehension method
def minimum_grade(rating: float, series_list: list):
    return [series for series in series_list if len(series.rates) > 0 and sum(series.rates)/len(series.rates) >= rating]

def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres] 


# Standard method
def minimum_grade(rating: float, series_list: list):
    min_rating_series = []
    for series in series_list:
        if len(series.rates) > 0 and sum(series.rates)/len(series.rates) >= rating:
            min_rating_series.append(series)
    return min_rating_series


def includes_genre(genre: str, series_list: list):
    genre_list = []
    for series in series_list:
        if genre in series.genres:
            genre_list.append(series)
    return genre_list


s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)

# Series - Approach 2
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = [0, 0, 0, 0, 0, 0]
        self.number_of_ratings = 0
 
    def grade(self):
        if self.number_of_ratings == 0:
            return 0
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            return grade_sum / self.number_of_ratings
 
 
    def __str__(self):
        genres = ", ".join(self.genres)
 
        if self.number_of_ratings == 0:
            ratings = "no ratings"
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            ka = grade_sum / self.number_of_ratings
            ratings = f"{self.number_of_ratings} ratings, average {ka:.1f} points"
 
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{ratings}"
 
    def rate(self, grade: int):
        self.number_of_ratings += 1
        self.ratings[grade] += 1
 
def minimum_grade(grade: float, seriest: list):
    result = []
    for series in seriest:
        if series.grade() >= grade:
            result.append(series)
 
    return result
 
def includes_genre(genre: str, seriest: list):
    result = []
    for series in seriest:
        if genre in series.genres:
            result.append(series)
 
    return result
 
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    seriest = [s1, s2, s3]
 
    answer = minimum_grade(4.5, seriest)
    print(answer)