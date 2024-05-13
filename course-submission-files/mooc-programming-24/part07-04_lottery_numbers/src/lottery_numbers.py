# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    number_pool = list(range(lower, upper+1))
    lottery_list = sample(number_pool, amount)
    lottery_list.sort()
    return lottery_list