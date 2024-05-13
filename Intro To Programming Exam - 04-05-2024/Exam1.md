## Exercise 1
Complete this in exercise template `exercise1.py`

Please write a program, which ask user to type in numbers one by one. When the user inputs number zero, program outputs:

- smallest number
- biggest number
- amount of the numbers
- sum of the numbers
- most repeated number

After this, the execution of the program ends.

The example run of the program:
```python
Type in a number: 5
Type in a number: 10
Type in a number: -3
Type in a number: 5
Type in a number: 14
Type in a number: 0
Biggest: 14
Smallest: -3
Number of numbers: 5
Sum: 31
Most repeated: 5
```
You can make an assumption, that the user inputs at least one number and that the user inputs only valid strings (numbers).

## Exercise 2
Complete this in exercise template `exercise2.py`

The task is to create three functions: `copy(matrix: list)`, `flip(matrix: list)`, and `flip_and_copy(matrix: list)`.

The function `copy(matrix: list)` should have the following properties:

- The function takes a matrix as input, which is a list of lists. Each of the inner lists contain 2 elements.
- The function returns a copy of the matrix. It's important to note that changes made to the original matrix do not affect the copy or its elements.

The function `flip(matrix: list)` should have the following properties:

- The function takes a matrix as input, which is a list of lists. Each of the inner lists contain 2 elements.
- The function flips the elements of the lists contained in the matrix in the opposite order. In practice, this means that each row's first element becomes the second and the second element becomes the first.
- This function should not return anything, but it should directly modify the original matrix. So, the return value of the function is the default None.

The function `flip_and_copy(matrix: list)` should have the following features:

- The function takes a matrix as input, which is a list of lists. Each of the inner lists contain 2 elements.
- The function makes a copy of the original matrix and flips its element order.
- The function should perform the matrix modification by calling the previously defined functions, i.e., the function flip and the function copy.
- The function returns the flipped copy of the original matrix.

Here's an example code that you can use to test your function:

```python
matrix = [
    ["Donald Duck", 80],
    ["Mickey Mouse", 60],
    ["Moomintroll", 120],
    ["Snoopy", 40],
    ["Goofy Goof", 100]
]

first_element_beginning = matrix[0]
first_value_beginning = matrix[0].copy()
flipped_copy = flip_and_copy(matrix)

copy_of_original = copy(matrix)
return_value_of_flip_function = flip(matrix)

print("Copy:")
for row in copy_of_original:
    print(row)

print()

print("Flipped:")
for row in matrix:
    print(row)

print()
print("return_value_of_flip_function:", return_value_of_flip_function)
print()

# '==' compares the values of elements, 'is' checks if the elements are the same
print("first_value_beginning == matrix[0]:", first_value_beginning == matrix[0]) #False
print("first_element_beginning is matrix[0]:", first_element_beginning is matrix[0]) #True
print()
print("first_value_beginning == copy_of_original[0]:", first_value_beginning == copy_of_original[0]) #True
print("first_element_beginning is copy_of_original[0]:", first_element_beginning is copy_of_original[0]) #False
print()
print("matrix[0] == flipped_copy[0]:", matrix[0] == flipped_copy[0]) #True
print("matrix[0] is flipped_copy[0]:", matrix[0] is flipped_copy[0]) #False
print()
print("first_value_beginning == flipped_copy[0]:", first_value_beginning == flipped_copy[0]) #False
print("first_value_beginning is flipped_copy[0]:", first_value_beginning is flipped_copy[0]) #False
```

Output of the program:
```python
Copy:
['Donald Duck', 80]
['Mickey Mouse', 60]
['Moomintroll', 120]
['Snoopy', 40]
['Goofy Goof', 100]

Flipped:
[80, 'Donald Duck']
[60, 'Mickey Mouse']
[120, 'Moomintroll']
[40, 'Snoopy']
[100, 'Goofy Goof']

return_value_of_flip_function: None

first_value_beginning == matrix[0]: False
first_element_beginning is matrix[0]: True

first_value_beginning == copy_of_original[0]: True
first_element_beginning is copy_of_original[0]: False

matrix[0] == flipped_copy[0]: True
matrix[0] is flipped_copy[0]: False

first_value_beginning == flipped_copy[0]: False
first_value_beginning is flipped_copy[0]: False
```

## Exercise 3

Complete this in exercise template `exercise3.py`

Create a function called `read_points()` that reads the statistics of ice hockey teams from the file `statistics.txt`.

The file is read from the same folder as `exercise3.py`

Lines in the file represent the statistics of an ice hockey team, formatted as: [team]:[wins]-[losses]-[ties]

For example, the string: "Kumpula Intelligence:0-8-1" describes a team called `Kumpula Intelligence` with `0 wins`, `8 losses` and `1 tie`.

For example, a line in the file: "Kumpula Intelligence:0-8-1" describes a team called `Kumpula Intelligence` with `0 wins`, `8 losses`, and `1 tie`.

The function `read_points()` calculates the total points from each line as follows: three points for a win, one point for a tie, and no points for a loss. Finally, the function returns a list containing the results in the form (team_name, points), that is, a list of tuples.

If the number of wins, losses, or ties found on a line cannot be read as integers, the function raises a ValueError with the message "Invalid format in file: [file line]", where [file line] is the line from which the exception was found.

You can assume that the file format is otherwise correct, meaning it has the appropriate number of colons and dashes, and that the integers are positive.

You can copy the following lines and add them exactly as they are to your test file `statistics.txt` for testing your program:

```txt
Heba hawks:5-6-1
Brewsters:3-12-10
Sleepers:0-0-0
KBC:6-2-1
Navy jerries:7-0-1
Loosisters:8-5-0
```
You may want to add or modify some lines that contain incorrect data to test your program's exception handling mechanism. Below are examples of lines that include deliberate errors:

```txt
KBC:AAA-1-ll
Loosisters:7-4.5-1
```
These example lines intentionally contain incorrect information (such as letters instead of numbers) to allow you to verify that your program identifies invalid inputs and handles them correctly with ValueError exceptions.