#  Any function definition begins with the keyword 'def', short for define. Then comes the name of the function, followed by parentheses and a colon character. 
# This is called the header of the function. After this, indented just like 'while' and 'if' blocks, comes the body of the function.
# Code in the body of the function is only executed when the function is called.
# Calling a function is as simple as mentioning its name in your code. 

# The "main" program below the function should contain appropriate function calls, so that the program can be tested. 
# Python treats all code that is not within function definitions as part of the "main function", which gets executed when the file itself is evaluated or executed.

# All code not within function definitions is part of
# the main function of the program

# Example
def message():
    print("This is my very own function!")

if __name__ == "__main__":
    message()

# Important: on this course the automatic tests that are run on the exercise files require an empty main function. 
# No commands should be left in the main function of your solution. 
# That is, any code that you yourself use for testing must be contained in a specially defined if block:
# The purpose of this is to make sure that your solution gets tested on a clean slate, as the tests often check what your functions print out. 
# It is worth noting that the tests will not execute any code from within the if __name__ == "__main__" block, so no code that is needed to fulfil the requirements of the exercise should be placed within the block.

# Example 1
def squared(x):
    print(f"The square of the number {x} is {x * x}")

squared(2)
squared(5)

# Example 2
def hello(name):
    if name == "Emily":
        print("Hello", name)
    else:
        print("Hi", name)

hello("Emily")
hello("Mark")

# Example 3
def sum(x, y): # function takes two arguments and assigns them to 'x' and 'y' as parameters to the function
    result = x + y # function includes a helper variable, 'result', used to store the sum of its arguments 
    print(f"The sum of the arguments {x} and {y} is {result}")

sum(1, 2)
sum(5, 24)

# The First Character
def first_character(text):
    print(text[0])
    
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')   
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

# Mean function
def mean(x, y, z):
    answer = (x + y + z)/3
    print(answer)

# Testing the mean function
if __name__ == "__main__":
    mean(1, 2, 3)

# Print many times
def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1

if __name__ == "__main__":
    print_many_times("Hello", 3)
    print_many_times("python", 5)

# A square of hashes
def hash_square(length):
    i = length
    while i > 0:
        print("#" * length)
        i -= 1

if __name__ == "__main__":
    hash_square(5)

# Chessboard - Approach 1
def chessboard(length):
    line = 1
    string = "1"
    while line <= length:
        index = 0
        while index < length - 1:
            if string[index] == "1":
                string = string + "0"
            else:
                string = string + "1"
            index += 1
        print(string)
        line += 1
        if line % 2 == 0:
            string = "0"
        else:
            string = "1"

# Testing the function
if __name__ == "__main__":
    chessboard(5)
    
# Chessboard - Approach 2
def chessboard(length):
    line = 1
    while line <= length:
        if line % 2 != 0:
            print("10" * (length//2), end="")
            if length % 2 != 0:
                print("1")
            else:
                print()
            line += 1
        else: 
            print("01" * (length//2), end="")
            if length % 2 != 0:
                print("0")
            else:
                print()
            line += 1
# Testing the function
if __name__ == "__main__":
    chessboard(6)

# Chessboard - Approach 2 tests
# 01
length = 9

print("01" * (length//2), end="")

if length % 2 != 0:
    print("0")

# 10
length = 9

print("10" * (length//2), end="")

if length % 2 != 0:
    print("1")

# Chessboard - Approach 2 (Redundant counters)
def chessboard(length):
    i = length
    line = 1
    while i > 0:
        if line % 2 != 0:
            print("10" * (length//2), end="")
            if length % 2 != 0:
                print("1")
            else:
                print()
            i -= 1  
            line += 1
        else: 
            print("01" * (length//2), end="")
            if length % 2 != 0:
                print("0")
            else:
                print()
            i -= 1
            line += 1

# Testing the function
if __name__ == "__main__":
    chessboard(5)

# ⭐ ⭐ Chessboard - Approach 3
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(6)

# ⭐ ⭐ A word squared - Approach 1
def squared(string, exp):
    string *= exp**2
    i = 0
    row = 0
    while row < exp:
        print(string[i : exp + i])
        i += exp
        row += 1
        
# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)

# A word squared - Approach 1 Tests
string = "aybabtu"
mult = 5
string *= 5*5

print(string)
print(len(string))

i = 0
row = 0
while row < mult:
    print(string[i:mult + i])
    i += mult
    row += 1

# A word squared - Approach 2
def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)

# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)

# A word squared - Approach 2 Explainer
size = 6
i = 0
while i < size:
    print(i % size) # modulus of 'size' range from 0 to (size - 1)
    i += 1
# Output of modulus of size = 6 are 0, 1, 2, 3, 4, 5 and moves in a circular pattern
# the modulus of size is always equal to 0 for numbers which are divisible by size, or multiples of size

# The main part of the loop inside the 'squared' function is the 'characters' variable indexing through modulus of the string length.
# The modulus of the string length circles the index of the string from 0 to (string length - 1) and ensures that every character of the string input is selected and picked back up from where it was left off.

# 1. The while loop begins with a pre-initiated index at 0 and an empty row string.
# 2. The index follows the individual letters in the square (starting from 0) and thus must be equal to the (size(**2) - 1) of the square at the end of the while loop, i.e. there should be as many index figures (minus 1) as the letters within the square.
# 3. The while loop runs as long as the index value is lower than the size(**2) of the square.  
# 4. Following the test for weather the index value is greater than 0 (meaning that the if-statement should not be executed for the frst letter in the first row) and whether the index mod of the size (length) of the square inside the nested if-statement is not equal to zero (ensuring that the end of the line/row has not been reached), the main part of the while loop is executed.
# 5. The main part of the loop computes the index modulus of the string length to return the index of the characters string. 
# 6. The character letter returned by the index is then appended to the row variable and the index value is increased by 1.
# 7. The while loop iterates and with every loop the character letters corresponding to the increased index and modulus are appended to the row variable. 
# 8. When index value returns a modulus of square size of 0 (signaling the end of the first row, which can be at maximum the size specified), the nested-if statement is triggered to execute the print function for the fully appended row.
# 9. The if-statement then empties the row string and triggers a new line (done at the time of the print function). 
# 10. The main function inside the while loop is repeated, appending letter to the row variable corresponding to the increased index and its modulus of the characters length

# The main part of the while loop keeps appending letters from the character variable to the row variable using the modulus operation. Given the circular characteristic of the modulus operation, the returned index reference to the string variable keeps circling the entire length of the string with every step, covering every letter with every execution.
# The nested if-statement checks wether the row/line length or index number has reached the end of the square, and if so, the print function is executed. The modulus operation inside the if condition checks whether the end of the line has been reached leveraging the modulus operation's circular characteristics and the given square size paramter against the index counter.

# Solution reference image in path: Images\word-square.jpg