# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning if beginning % 2 == 0 else beginning + 1 
    while number <= maximum:
        yield number
        number += 2