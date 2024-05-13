# Write your solution here
from string import ascii_lowercase, ascii_uppercase, digits

def change_case(orig_string: str) -> str:
    mod_string = ""
    for character in orig_string:
        if character in ascii_lowercase:
            mod_string += character.upper()
        elif character in ascii_uppercase:
            mod_string += character.lower()
        else: 
            mod_string += character
    return mod_string

def split_in_half(orig_string: str) -> tuple[str, str]:
    half = len(orig_string) // 2
    return orig_string[:half], orig_string[half:]

def remove_special_characters(orig_string: str) -> str:
    mod_string = ""
    for character in orig_string:
        if character in ascii_lowercase or character in ascii_uppercase or character in digits or character == " ":
            mod_string += character
    return mod_string