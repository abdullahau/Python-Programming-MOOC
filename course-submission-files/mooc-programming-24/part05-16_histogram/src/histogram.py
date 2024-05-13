# Write your solution here
def histogram(my_string: str):
    my_dictionary = {}
    for letter in my_string:
        if letter not in my_dictionary:
            my_dictionary[letter] = 0
        my_dictionary[letter] += 1
    for key, value in my_dictionary.items():
        print(f"{key} {'*' * value}")

if __name__ == "__main__":
    histogram("statistically")
    histogram("abba")