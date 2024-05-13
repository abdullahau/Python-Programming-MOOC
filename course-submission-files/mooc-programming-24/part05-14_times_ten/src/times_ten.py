# Write your solution here
def times_ten(start_index: int, end_index: int):
    new_dictionary = {}
    for i in range(start_index, end_index + 1):
        new_dictionary[i] = i * 10
    return new_dictionary

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)