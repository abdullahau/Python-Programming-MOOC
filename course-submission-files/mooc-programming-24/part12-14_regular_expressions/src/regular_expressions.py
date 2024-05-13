# Write your solution here
import re

def is_dotw(my_string: str):
    dotw = "(Mon)|(Tue)|(Wed)|(Thu)|(Fri)|(Sat)|(Sun)"
    return True if re.search(dotw, my_string) else False


def all_vowels(my_string: str):
    vowels = '^[aeiou]*$'
    return True if re.search(vowels, my_string) else False

def time_of_day(my_string: str):
    return True if re.search("^([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", my_string) else False