# Write your solution here
def invert(my_dict: dict):
    inverted_dict = {}
    for key, value in my_dict.items():
        inverted_dict[value] = key
    my_dict.clear()
    for key, value in inverted_dict.items():
        my_dict[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)