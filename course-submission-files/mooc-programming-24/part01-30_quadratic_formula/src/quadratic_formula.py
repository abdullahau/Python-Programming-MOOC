# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(f"The roots are {r1} and {r2}")