# More Loops

# The break command

# 'break' command is used to stop the execution of a loop immediately.
# The same functionality can be achieved without the break command, using a suitable condition. 
# 1st version using the 'break' command
sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    sum += number

print (f"The sum is {sum}")

# 2nd version without the 'break' command
sum = 0
number = 0

while number != -1:
    number = int(input("Please type in a number, -1 to exit: "))
    if number != -1:
        sum += number

print (f"The sum is {sum}")

# The two programs are functionally practically identical. 
# However, the first method is often easier, as the condition 'number == -1' appears only once, and the variable 'number' doesn't have to be initialised outside the loop.

# The 'break' command and a suitable condition can also be used together in a while loop. 

# For example, the following loop is repeated as long as the sum of the numbers is at most 100, but it also stops if the user types in the number -1.
sum = 0

while sum <= 100:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    sum += number

print (f"The sum is {sum}")

# The following program is functionally identical to the above:
sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    sum += number
    if sum > 100:
        break

print (f"The sum is {sum}")

# Continue Command

# The 'continue' causes the execution of the loop to jump straight to the beginning of the loop, where the condition of the loop is. 
# Following the jump to the beginning, the execution continues normally with checking the condition.

# Example 1
sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    if number >= 10:
        continue
    sum += number

print (f"The sum is {sum}")

# Nested Loops

# Example 1
while True:
    number = int(input("Please type in a number: "))
    if number == -1:
        break
    while number > 0:
        print(number)
        number -= 1
        
# When there are nested loops, 'break' and 'continue' commands only affect the innermost loop which they are a part of.
# Example 2
while True:
    number = int(input("Please type in a number: "))
    if number == -1:
        break
    while True:
        if number <= 0:
            break
        print(number)
        number -= 1

# Helper variables 

# Helper variables increase or decrease with every iteration of a loop.
# Example 1 - Print out even numbers up the limit
limit = int(input("Please type in a number: "))
i = 0 # The helper variable i is set to 0 before the loop.
while i < limit:
    print(i)
    i += 2 # The helper variable i is increased by 2 after each iteration of the loop.

# Using nested loops sometimes necessitates a separate helper variable for the inner loop.

# Example 2 - "Number Pyramid" based on a number given by the user
number = int(input("Please type in a number: "))
while number > 0:
    i = 0
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print()
    number -= 1
    
# Example 2 - Number Pyramid with comments
number = int(input("Please type in a number: "))
while number > 0: # The while loop is repeated as long as the number given by the user is greater than 0
    i = 0 # The helper variable i is set to 0 before the loop.
    while i < number: # The while loop is repeated as long as the number given by the user is greater than 0
        print(f"{i} ", end="") # The end="" argument inside the print command prevents the output from being printed on a new line.
        i += 1 # The helper variable i is increased by 1 after each iteration of the loop.
    print() # A new line is printed after each iteration of the loop.
    number -= 1 # The helper variable number is decreased by 1 after each iteration of the loop.

# 1. The user inputs a number. 
# 2. Main Loop: Main loop is initiated which repeats as many times as the number given by the user.
# 3. Main Loop: A helper variable 'i' is set to 0 before the initiation of the nested loop.
# 4. Nested Loop: A nested loop is initiated starting from i = 0 and ending at the number variable given by the user.
# 5. Nested Loop: A print command is executed with the value of 'i' which starts from 0.
# 6. Nested Loop: The helper variable 'i' is increased by 1 at the end of each iteration of the loop.
# 7. Nested Loop: The print command argument 'end=""' appends the new value of 'i' to the output.
# 8. Nested Loop: The nested loop ends as soon as the helper variable 'i' reaches the number given by the user.
# 9. Main Loop: a print() command is executed to add a new line.
# 10. Main Loop: The 'number' given by the user is decreased by 1 at the end of each iteration of the loop.
# 11. Main Loop: The loop returns to the beginning of the loop to assess whether the decreased number variable is still above 0.
# 12. Main Loop: if the number is still greater than zero, the helper variable 'i' is reset to 0. 
# 12. Nested Loop: Reinitiated to the maximum run set by the updated 'number' variable.
# Note: Main loop is repeated as many times as the number given by the user, thus forming the same number of rows.

# In this program the outer loop uses the helper variable 'number', which decreases by 1 with each iteration until it reaches 0. 
# The helper variable 'i' is set to 0 just before the inner loop is entered, each time the outer loop repeats.

# The inner loop uses the helper variable 'i', which increases by 1 with each iteration of the inner loop. 
# The inner loop repeats until i is equal to number, and prints out each value of 'i' on the same line, separated by a space character. 
# When the inner loop finishes, the print command in the outer loop starts a new line.

# Now remember that with each iteration of the outer loop the value of number decreases, so the amount of times the inner loop repeats also decreases. 
# With each repetition the line of numbers gets shorter, and thus we get the pyramid shape.

# Use visualization tool for assessing the code: https://pythontutor.com/visualize.html#mode=edit 

# Multiplication
number = int(input("Please type in a number: "))
i = 1

while i <= number:
    z = 1
    while z <= number:
        print(f"{i} x {z} = {i * z}")
        z += 1
    i += 1

# First letters of words - Approach 1 (Prints the first letter of the sentence, subsequently searches for the index of the first ocurring space character, drops the characters preceeding and including the space character and prints out the first letter of the remaining sentence)
sentence = input("Please type in a sentence: ")

print(sentence[0])

while True:
    i = sentence.find(" ")
    sentence = sentence[i+1:]
    if i == -1:
        break
    print(sentence[0])

# First letters of words - Approach 2 (Complete search through string - prints out character only if the character is preceeded by a space)
sentence = input("Please type in a sentence: ")
 
# Add a space at the start, to make handling sentence easier
sentence = " " + sentence
 
# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1

# Factorial - Approach 1
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    i = number
    z = 1
    while i >= 1:
        z *= i
        i -= 1
    print(f"The factorial of the number {number} is {z}")

print("Thanks and bye!")

# Factorial - Appraoch 2
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
 
    factorial = 1
    new = 1
    while new <= number:
        factorial *= new
        new += 1
 
    print(f"The factorial of the number {number} is {factorial}")
 
print("Thanks and bye!")

# Flip the pairs - Approach 1
number = int(input("Please type in a number: "))
i = 0
z = 2

while i <= number:
    i += 1
    if z * i >= number:
        break
    print(z * i)
    print(z * i - 1)

print(number)
if number % 2 == 0:
    print(number - 1)

# ⭐ Flip the pairs - Approach 2
number = int(input("Please type in a number: "))
 
index = 1
while index+1 <= number:
    print(index+1)
    print(index)
    index += 2
 
if index <= number:
    print(index)

# Taking turns - Approach 1
number = int(input("Please type in a number: "))
i = 0
z = number - 1

while z >= number/2:
    print(number - z)
    print(number - i)
    z -= 1
    i += 1

if number % 2 !=0:
    print(number - z)

# ⭐ Taking turns - Approach 1
number = int(input("Please type in a number: "))
 
left = 1
right = number
 
while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1
 
if left == right:
    print(left)