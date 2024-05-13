# Write your solution here
from string import ascii_lowercase, digits

from random import choices

def generate_strong_password(length: str, nums: bool, specials: bool):
    if nums and specials:
        return nums_specials(length)
    elif nums and not specials:
        return nums_password(length)
    elif not nums and specials:
        return specials_password(length)
    elif not nums and not specials:
        password = choices(ascii_lowercase, k=length)
        password = "".join(password)
        return password

def nums_specials(length):
    special = "!?=+-()#"
    characters = ascii_lowercase + digits + special
    password = choices(characters, k=length)
    if any(i in password for i in ascii_lowercase) and any(i in password for i in digits) and any(i in password for i in special):
        return "".join(password)
    else:
        return nums_specials(length)

def nums_password(length):
    characters = ascii_lowercase + digits
    password = choices(characters, k=length)
    if any(i in password for i in ascii_lowercase) and any(i in password for i in digits):
        return "".join(password)
    else:
        return nums_password(length)

def specials_password(length):
    special = "!?=+-()#"
    characters = ascii_lowercase + special
    password = choices(characters, k=length)
    if any(i in password for i in ascii_lowercase) and any(i in password for i in special):
        return "".join(password)
    else:
        return specials_password(length)