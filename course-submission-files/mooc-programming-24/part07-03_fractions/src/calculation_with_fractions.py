# Write your solution here
from fractions import Fraction

def fractionate(amount: int) -> list:
    frac_list = []
    for i in range(amount):
        frac_list.append(Fraction(1, amount))
    return frac_list