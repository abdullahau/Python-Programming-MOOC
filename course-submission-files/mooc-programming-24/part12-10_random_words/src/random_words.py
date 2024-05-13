# Write your solution here:
from random import choices

def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        yield "".join(choices(characters,k=length))