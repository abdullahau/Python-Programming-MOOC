# Write your solution here

number = int(input("Number: "))

mod3 = number % 3
mod5 = number % 5

if mod3 == 0 and mod5 ==0:
    print("FizzBuzz")
elif mod3 == 0:
    print("Fizz")
elif mod5 == 0:
    print("Buzz")