# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return "".join([character for character in string if character not in forbidden])