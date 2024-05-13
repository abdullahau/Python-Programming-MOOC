# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    while len(numbers) % 5 != 0:
        numbers.append(numbers[-1] + 1)
        add_numbers_to_list(numbers)