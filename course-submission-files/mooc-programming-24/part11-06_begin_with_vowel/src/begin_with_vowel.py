# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list) -> list:
    return [word for word in words if word[0].lower() in "aeiou"]