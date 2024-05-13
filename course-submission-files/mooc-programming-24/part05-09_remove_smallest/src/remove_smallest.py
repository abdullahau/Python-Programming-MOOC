# Write your solution here
def remove_smallest(numbers: list):
    min_number = min(numbers)
    min_index = numbers.index(min_number)
    numbers.pop(min_index)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)