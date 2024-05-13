# The general structure of the while statement with a condition is as follows:
# while <condition>:
#    <block>

# In the following loop we have the condition number < 10. The block within the loop is executed only if the variable number is less than 10.
number = int(input("Please type in a number: "))

while number < 10:
    print(number)
    number += 1

print("Execution finished.")

# Print even numbers from 2 to 30
even = 2

while even <= 30:
    print(even)
    even += 2
    
# Countdown to 1
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1
print("Now!")

# Count up from 1 to specified number
number = int(input("Upper limit: "))

start = 1

while start < number:
    print(start)
    start += 1

# Count up from 1 to specified number - Approach 2    
number = int(input("Upper limit: "))

diff = number - 1

while diff >= 0:
    print(number - diff)
    diff -= 1
    
# Power of Twos - Approach 1
limit = int(input("Upper limit: "))
number = 1
while number <= limit:
    print(number)
    number *= 2

# Power of Twos - Approach 2
limit = int(input("Upper limit: "))
power = 0
test = 0

while test <= limit:
    result = 2 ** power
    print(result)
    power += 1
    test = 2 ** (power)
    
# Power of base n - Approach 1
limit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 1

while number <= limit:
    print(number)
    number *= base
    
# Power of base n - Approach 1
limit = int(input("Upper limit: "))
base = int(input("Base: "))
power = 0
test = 0

while test <= limit:
    result = base ** power
    print(result)
    power += 1
    test = base ** (power)
    
# The sum of consecutive numbers, version 1

limit = int(input("Limit: "))
start = 1
sums = 1

while sums < limit:
    start += 1
    sums = sums + start

print(sums)

# The sum of consecutive numbers, version 2
# Approach 1
limit = int(input("Limit: "))
number = 1
sum = 1
numbers = "1"
while sum < limit:
    number += 1
    sum += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {sum}")


# Approach 2
limit = int(input("Limit: "))
start = 1
sums = 1
calculation = "The consecutive sum: 1"

while sums < limit:
    start += 1
    calculation += f" + {start}"
    sums = sums + start
 
calculation += f" = {sums}"
print(calculation)