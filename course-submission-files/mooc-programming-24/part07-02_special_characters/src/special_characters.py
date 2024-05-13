# Write your solution here
import string

def separate_characters(my_string: str):
    letters = ""
    punctuations = ""
    specials = ""
    for character in my_string:
        if character in string.ascii_letters:
            letters += character
        elif character in string.punctuation:
            punctuations += character
        else:
            specials += character
    return letters, punctuations, specials

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])