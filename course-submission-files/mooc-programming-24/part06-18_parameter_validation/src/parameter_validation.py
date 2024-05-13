# Write your solution here
def new_person(name: str, age: int):
    if name == "" or len(name) > 40 or name.find(" ") == -1 or age < 0 or age > 150:
        return error_function(name, age)
    return (name, age)


def error_function(name: str, age: int):
    if name == "":
        raise ValueError("name is an empty string")
    if len(name) > 40:
        raise ValueError("name is longer than 40 characters")
    if name.find(" ") == -1:
        raise ValueError("name contains less than two words")
    if age < 0:
        raise ValueError("age is a negative number")
    if age > 150:
        raise ValueError("age is greater than 150")