# Regular expressions

# We have already established that Python is an excellent environment for processing text. 
# One additional powerful tool for text processing is _regular expressions_, often shortened as _regex_ or _regexp_. 
# They are a way of selecting and searching for strings which follow a certain pattern. 
# This section introduces you to the basics of regular expression, but you will find much more information online, including in the Python [tutorial](https://docs.python.org/3/howto/regex.html).

# What are regular expressions?

# Regular expressions are not just a Python feature. 
# They represent, in a way, a programming language within a programming language. 
# They are, to an extent, compatible across many different programming languages. 
# Regular expressions have their own specific syntax. 
# The idea is to define a collection of strings which follow certain rules.

# Let's begin with a simple example, before diving deeper into the syntax:
import re

words = ["Python", "Pantone", "Pontoon", "Pollute", "Pantheon"]

for word in words:
    # the string should begin with "P" and end with "on"
    if re.search("^P.*on$", word):
        print(word, "found!")
        
# We need to `import` the `re` module in order to use regular expressions in Python. 
# The `re` module contains many functions for working with regular expressions. 
# In the example above, the `search` function takes two string arguments: the pattern string, and the target string where the pattern is looked for.

# This second example looks for any numbers in a string. 
# The `findall` function returns a list of all the instances which match the pattern:
import re

sentence = "First, 2 !#third 44 five 678xyz962"

numbers = re.findall("\d+", sentence)

for number in numbers:
    print(number)
    
# The syntax of regular expressions

# Let's get familiar with the basic syntax of regular expressions. 
# Most of the following examples make use of this testing program:

import re

expression = input("Please type in an expression: ")

while True:
    input_string = input("Please type in a string: ")
    if input_string == "":
        break
    if re.search(expression, input_string):
        print("Found!")
    else:
        print("Not found.")

# Alternate substrings

# The vertical bar `|`, also called the pipe character, allows you to match alternate substrings. 
# Its significance is thus _or_. For example, the expression `911|112` matches strings which include either the substring `911` or the substring `112`.

# An example with the testing program:
'''
Please type in an expression: aa|ee|ii
Please type in a string: aardvark
Found!
Please type in a string: feelings
Found!
Please type in a string: radii
Found!
Please type in a string: smooch
Not found.
Please type in a string: continuum
Not found.
'''

# Groups of characters

# Square brackets are used to signify groups of accepted characters. 
# For example, the expression `[aeio]` would match all strings which contain any of the characters a, e, i, or o. 

# A dash is also allowed for matching ranges of characters. 
# For example, the expression `[0-68a-d]` would match all strings which contain a digit between 0 and 6, or an eight, or a character between a and d. 
# In this notation all ranges are _inclusive_.

# Combining two sets of brackets lets you match two consecutive characters. 
# For example, the expression `[1-3][0-9]` would match any two digit number between 10 and 39, inclusive.

# An example with the testing program:

'''
Please type in an expression: [C-FRSO]
Please type in a string: C
Found!
Please type in a string: E
Found!
Please type in a string: G
Not found.
Please type in a string: R
Found!
Please type in a string: O
Found!
Please type in a string: T
Not found.
'''

# Repeated matches

# Any part of an expression can be repeated with the following operators:
    # `*` repeats for any number of times, including zero
    # `+` repeats for any number of times, but at least once
    # `{m}` repeats for exactly `m` times

# These operators work on the part of the expression immediately preceding the operator. 
# For example, the expression `ba+b` would match the substrings `bab`, `baab` and `baaaaaaaaaaab`, among others. 
# The expression `A[BCDE]*Z` would match the substrings `AZ`, `ADZ` or `ABCDEBCDEBCDEZ`, among others.

# An example with the testing program:
'''
Please type in an expression: 1[234]*5
Please type in a string: 15
Found!
Please type in a string: 125
Found!
Please type in a string: 145
Found!
Please type in a string: 12342345
Found!
Please type in a string: 126
Not found.
Please type in a string: 165
Not found.
'''

# Other special characters

# A dot is a wildcard character which can match any single character. 
# For example, the expression `c...o` would match any five character substring beginning with a `c` and ending with an `o`, such as `c-3po` or `cello`.

# The `^` character specifies that the match must be at the beginning of the string,
# and `$` specifies that the match must be at the end of the string. 
# These can also be used to exclude from the matches any other characters than those specified:

'''
Please type in an expression: ^[123]*$
Please type in a string: 4
Not found.
Please type in a string: 1221
Found!
Please type in a string: 333333333
Found!
'''

# Sometimes you need to match for the special characters reserved for regular expression syntax. 
# The backslash `\` can be used to _escape_ special characters. 
# So, the expression `1+` matches one or more numbers `1`, but the expression `1\+` matches the string `1+`.

'''
Please type in an expression: ^\*
Please type in a string: moi*
Not found.
Please type in a string: m*o*i
Not found.
Please type in a string: *moi
Found!
'''

# Round brackets can be used to group together different parts of the expression. 
# For example, the expression `(ab)+c` would match the substrings `abc`, `ababc` and `ababababababc`, 
# but not the strings `ac` or `bc`, as the entire substring `ab` would have to appear at least once.

'''
Please type in an expression: ^(jabba).*(hut)$
Please type in a string: jabba the hut
Found!
Please type in a string: jabba a hut
Found!
Please type in a string: jarjar the hut
Not found.
Please type in a string: jabba the smut
Not found.
'''

# Regular expressions

# Here are some exercises for familiarizing yourself with regular expression syntax.

# Part 1: Days of the week

# Using a regular expression, please write a function named `is_dotw(my_string: str)`.
# The function should return `True` if the string passed as an argument contains an abbreviation for a day of the week:
# ().

import re

def is_dotw(my_string: str):
    dotw = "(Mon)|(Tue)|(Wed)|(Thu)|(Fri)|(Sat)|(Sun)"
    return True if re.search(dotw, my_string) else False

print(is_dotw("Mon"))
print(is_dotw("Fri"))
print(is_dotw("Tui"))

# Part 2: Check for vowels

# Please write a function named `all_vowels(my_string: str)` which uses a regular expression to check whether all characters in the given string are vowels.

def all_vowels(my_string: str):
    vowels = '[aeiou]*'
    return True if re.fullmatch(vowels, my_string) else False


# Method 2
def all_vowels(my_string: str):
    vowels = '^[aeiou]*$'
    return True if re.search(vowels, my_string) else False


print(all_vowels("eioueioieoieou"))
print(all_vowels("eiouuuuoaieoiaoeiueioieoieou"))
print(all_vowels("eiouuuuoaiceoiaoeiueioieoiecou"))
print(all_vowels("autoooo"))


# Part 3: Time of day

# Please write a function named `time_of_day(my_string: str)` which uses a regular expression to check whether a string in the format `XX:YY:ZZ` is a valid time in the 24-hour format, with two digits each for hours, minutes and seconds.

def time_of_day(my_string: str):
    return True if re.search("^([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", my_string) else False

print(time_of_day("12:43:01"))
print(time_of_day("AB:01:CD"))
print(time_of_day("17:59:59"))
print(time_of_day("33:66:77"))
print(time_of_day("ab:20:20"))
print(time_of_day("23:55:59"))

# Regular Expression - Approach 2
import re
 
def is_dotw(my_string: str):
    return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) is not None
 
def all_vowels(my_string: str):
    return re.search("^[aeiou]*$", my_string) is not None
 
def time_of_day(my_string: str):
    return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None

# RegEx - Approach 3
import re
 
def is_dotw(my_string: str):
    return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) is not None
 
def all_vowels(my_string: str):
    return re.search("^[aeiou]*$", my_string) is not None
 
def time_of_day(my_string: str):
    return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None

# Hockey statistics 

# In this exercise you will build an application for examining hockey league statistics from the NHL in a couple of different ways.

# The entry for a single player is in the following format:

'''
{
    "name": "Patrik Laine",
    "nationality": "FIN",
    "assists": 35,
    "goals": 28,
    "penalties": 22,
    "team": "WPG",
    "games": 68
}
'''

# Part 1: Search and list

# Please write an interactive application which first asks for the name of the file, and then offers the following functions:
    # - search by name for a single player's stats
    # - list all the abbreviations for team names in alphabetical order
    # - list all the abbreviations for countries in alphabetical order

# These functionalities grant you one exercise point. 
# Your application should now work as follows:

'''
file name: partial.json
read the data of 14 players

commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

command: 1
name: Travis Zajac

Travis Zajac         NJD   9 + 16 =  25

command: 2
BUF
CGY
DAL
NJD
NYI
OTT
PIT
WPG
WSH

command: 3
CAN
CHE
CZE
SWE
USA

command: 0
'''

# NB: the printout format for a player must be exactly as follows:
'''
Leon Draisaitl       EDM  43 + 67 = 110
Connor McDavid       EDM  34 + 63 =  97
Travis Zajac         NJD   9 + 16 =  25
Mike Green           EDM   3 +  8 =  11
Markus Granlund      EDM   3 +  1 =   4
123456789012345678901234567890123456789
'''

# The last line in the sample above is there to help you calculate the widths of the different fields in the output; you should not print the numbers line yourself in your final submission.

# The abbreviation for the team is printed from the 22nd character onwards. 
# The `+` sign is the 30th character and the `=` sign is the 35th character. 
# All the fields should be justified to the right edge. All whitespace is space characters.

# F-strings are probably the easiest way to achieve the required printout.

# Part 3: List players by points

# These two functionalities will grant you a second exercise point:
    # - list players in a specific team in the order of points scored, from highest to lowest. Points equals _goals_ + _assists_
    # - list players from a specific country in the order of points scored, from highest to lowest

# Your application should now work as follows:
'''
file name: partial.json
read the data of 14 players

commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

command: 4
team: OTT

Drake Batherson      OTT   3 +  7 =  10
Jonathan Davidsson   OTT   0 +  1 =   1


command: 5
country: CAN

Jared McCann         PIT  14 + 21 =  35
Travis Zajac         NJD   9 + 16 =  25
Taylor Fedun         DAL   2 +  7 =   9
Mark Jankowski       CGY   5 +  2 =   7
Logan Shaw           WPG   3 +  2 =   5


command: 0
'''

# Part 3: Most successful players

# These two functionalities will grant you a third exercise point:
    # - list of `n` players who've scored the most points
        # - if two players have the same score, whoever has scored the higher number of goals comes first
    # - list of `n` players who've scored the most goals
        # - if two players have the same number of goals, whoever has played the lower number of games comes first
        
# Your application should now work as follows:

'''
file name: partial.json
read the data of 14 players

commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

command: 6
how many: 2

Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35


command: 6
how many: 5


Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
John Klingberg       DAL   6 + 26 =  32
Travis Zajac         NJD   9 + 16 =  25
Conor Sheary         BUF  10 + 13 =  23


command: 7
how many: 6


Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
Conor Sheary         BUF  10 + 13 =  23
Travis Zajac         NJD   9 + 16 =  25
John Klingberg       DAL   6 + 26 =  32
Mark Jankowski       CGY   5 +  2 =   7


command: 0
'''

# Approach 1
import json

class Player:
    def __init__(self, player: str, team: str, country: str, goals: int, assists: int, games: int) -> None:
        self.player = player
        self.team = team
        self.country = country
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
        self.games = games
        
    def __repr__(self) -> str:
        return f"{self.player: <21}{self.team: ^3}{self.goals: >4}{'+': ^3}{self.assists: >2}{'=': ^3}{self.points:>3}"


class FileProcessing:
    def __init__(self, filename: str):
        with open(filename, "r") as f:
            self.__jsondata = json.loads(f.read())
        
        self.__data = []
        for entry in self.__jsondata:
            self.__data.append(Player(entry["name"], entry["team"], entry["nationality"], entry["goals"], entry["assists"], entry["games"]))
    
    @property        
    def data(self) -> list:
            return self.__data

class Search:
    def __init__(self, filename) -> None:
        stats = FileProcessing(filename)
        self.data = stats.data
    
    def total_entries(self) -> int:
        return len(self.data)
    
    def player_search(self, name: str):
        player = list(filter(lambda x: x.player == name, self.data))
        return player[0]
    
    def teams(self):
        teams_list = list(set(map(lambda x: x.team, self.data)))
        teams_list.sort()
        return teams_list
    
    def countries(self):
        countries_list = list(set(map(lambda x: x.country, self.data)))
        countries_list.sort()
        return countries_list
    
    def team_search(self, team: str):
        team_list = list(filter(lambda x: x.team == team, self.data))
        team_list.sort(key=lambda x: x.points, reverse=True)
        return team_list
    
    def country_search(self, country: str):
        country_list = list(filter(lambda x: x.country == country, self.data))
        country_list.sort(key=lambda x: x.points, reverse=True)
        return country_list
    
    def most_points(self):
        most_points = sorted(self.data, key=lambda x: (x.points, x.goals), reverse=True)
        return most_points
    
    def most_goals(self):
        most_goals = sorted(self.data, key=lambda x: (x.goals, -x.games), reverse=True)
        return most_goals


class HockeyApplication:
    def __init__(self) -> None:
        pass
    
    def help(self) -> str:
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
        
    def execute(self):
        data = Search(input("file name: "))
        print(f"read the data of {data.total_entries()} players")
        self.help()
        while True:
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                name = input("name: ")
                print(data.player_search(name))
            elif command == 2:
                teams = data.teams()
                for team in teams:
                    print(team)
            elif command == 3:
                countries = data.countries()
                for country in countries:
                    print(country)
            elif command == 4:
                team = input("team: ")
                team = data.team_search(team)
                for player in team:
                    print(player)
            elif command == 5:
                country = input("country: ")
                country = data.country_search(country)
                for player in country:
                    print(player)
            elif command == 6:
                number = int(input("how many: "))
                most_points = data.most_points()
                for i in range(number):
                    print(most_points[i])
            elif command == 7:
                number = int(input("how many: "))
                most_points = data.most_goals()
                for i in range(number):
                    print(most_points[i])

run = HockeyApplication()
run.execute()

# Approach 2
import json
 
class Statistics:
    def __init__(self, players: list):
        self.__players = players
 
    def by_points(self,  p):
        return  p['goals'] + p['assists']
 
    def by_goals(self,  p):
        # if the numbe of goals is equal, less played games is better
        return (p['goals'], -p['games'])
 
    def player_data(self, name: str):
        for player in self.__players:
            if player['name'] == name:
                return player
 
        return None
 
    def countries(self):
        return sorted(list(set(p['nationality'] for p in self.__players )))
 
    def teams(self):
        return sorted(list(set(p['team'] for p in self.__players )))
 
    def players_in_team(self, team: str):
        players = [ p for p in self.__players if p['team'] == team]
        return sorted(players, key=self.by_points, reverse=True)
 
    def players_from_country(self, country: str):
        players = [ p for p in self.__players if p['nationality'] == country]
        return sorted(players, key=self.by_points, reverse=True)
 
    def most_points(self, countryra):
        players = sorted(self.__players, key=self.by_points, reverse=True)
        return players[0: countryra]
 
    def most_goals(self, countryra):
        players = sorted(self.__players, key=self.by_goals, reverse=True)
        return players[0: countryra]
 
class Application:
    def __init__(self):
        self.__statistics = None
 
    def instructions(self):
        instructions = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(instructions)
 
    def f(self, p: dict):
        """
            helper method, which creates a string out of players formatted for output
        """
        points = p['goals'] + p['assists']
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
 
    def read_file(self):
        file_name = input("file: ")
        with open(file_name) as file:
            data = file.read()
 
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.__statistics = Statistics(players)
 
    def get_playes(self):
        name = input("name: ")
        player = self.__statistics.player_data(name)
        if player:
            print(self.f(player))
 
    def get_teams(self):
        for team in self.__statistics.teams():
            print(team)
 
    def get_countries(self):
        for country in self.__statistics.countries():
            print(country)
 
    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(self.f(player)) 
 
    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(self.f(player)) 
 
    def most_points(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_points(number):
            print(self.f(player)) 
 
    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_goals(number):
            print(self.f(player)) 
 
    def execute(self):
        self.read_file()
        self.instructions()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.get_playes()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
 
Application().execute()