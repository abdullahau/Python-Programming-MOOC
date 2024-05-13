# WRITE YOUR SOLUTION HERE:
def remove_smaller_than(numbers: list, limit: int) -> list:
    return [number for number in numbers if number >= limit]