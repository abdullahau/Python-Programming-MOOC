# Write your solution here
from string import ascii_lowercase
from random import choices

def generate_password(len: int) -> str:
    password = choices(ascii_lowercase, k=len)
    return "".join(password)