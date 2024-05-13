# Lists with different types of data

# List of strings
names = ["Marlyn", "Ruth", "Paul"]
print(names)
names.append("David")
print(names)

print("Number of names on the list:", len(names))
print("Names in alphabetical order:")
names.sort()
for name in names:
  print(name)

# List of floats
measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]

for measure in measurements:
    print(measure)

mean = sum(measurements) / len(measurements)

print("The mean is:", mean)

# Lists within lists
my_list = [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
print(my_list)
print(my_list[1])
print(my_list[1][0])

# Lists within lists - database
persons = [["Betty", 10, 1.37], ["Peter", 7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.78]]

for person in persons:
  name = person[0]
  age = person[1]
  height = person[2]
  print(f"{name}: age {age} years, height {height} meters")
  
# Matrices - Accessing & Changing Items within matrices
my_matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

print(my_matrix[0][1])
my_matrix[1][0] = 10
print(my_matrix)

# Matrices - Traversing with 'for' loops
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_matrix:
    print(row)

# Matrices - Nested Loops for Accessing Individual Items
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_matrix:
    print("a new row")
    for element in row:
        print(element)

# Accessing items in a matrix - Sum of Rows
def sum_of_row(my_matrix, row_no: int):
    # choose the desired row from within the matrix
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item

    return row_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_row(m, 1)
print(my_sum) # prints out 33 (which equals 9 + 1 + 12 + 11)


# Accessing items in a matrix - Sum of Columns
def sum_of_column(my_matrix, column_no: int):
    # go through each row and select the item at the chosen position
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]

    return column_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_column(m, 2)
print(my_sum) # prints out 39 (which equals 3 + 12 + 9 + 15)

# Changing value of a single element within the matrix:
def change_value(my_matrix, row_no: int, column_no: int, new_value: int):
    # choose the desired row
    row = my_matrix[row_no]
    # select the correct item within the row
    row[column_no] = new_value 

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

print(m)
change_value(m, 2, 3, 1000)
print(m)

# If we want to change the contents of the matrix, we have to access the elements by their indexes. This means that we can't use a simple 'for item in list' loop to traverse the matrix if we want to change the contents of the matrix.
# Instead, we will have to keep track of the indexes of the elements, for example with a while loop, or a for loop using the range function.
# The following code increases the value of each element in the matrix by one:

# Changing value of all elements within the matrix:
m = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(m)): # using the number of rows in the matrix
    for j in range(len(m[i])): # using the number of items on each row 
        m[i][j] += 1 

print(m)

# The outer loop goes through indexes from zero to the length of the matrix, that is, the number of rows in the matrix. 
# The inner loop goes through indexes from zero to the length of each row within the matrix (column).


# A two-dimensional array as a data structure in a game
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

def print_grid(sudoku):
    for row in sudoku:
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")
        print() # Newline character to move to the next row.

print_grid(sudoku)

# Any common game with a gameboard layout can be modelled in a similar fashion. 
# Among others, chess, Minesweeper, Battleship or Mastermind are all based on a two-dimensional grid. 
# For sudoku, it is natural to use numbers to represent the game state, but for other games, different methods may be better.

# The longest string - Approach 1
def longest(strings: list):
    length = 1
    for i in strings:
        if len(i) > length:
            length = len(i)
            string = i
    return string

strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
longest(strings)

# The longest string - Approach 2
def longest(strings: list):
    """ Function returns most longest of the strings """
    longest = ""
    for item in strings:
        if len(item) > len(longest):
            longest = item
 
    return longest

# Number of matching elements
def count_matching_elements(my_matrix: list, element: int):
    counter = 0
    for row in my_matrix:
        for i in row:
            if i == element:
                counter += 1
    return counter

m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))

# Go - Who Won - Approach 1
def who_won(game_board: list):
    empty = 0
    player1 = 0
    player2 = 0
    for row in game_board:
        for i in row:
            if i == 2:
                player2 += 1
            elif i == 1:
                player1 += 1
            else:
                empty += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 3
                
go_board = [
  [1, 0, 0, 0, 1, 0, 2, 0, 0],
  [0, 0, 0, 1, 2, 0, 1, 0, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 4],
  [0, 2, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 2, 1, 0],
  [1, 0, 1, 0, 1, 0, 2, 0, 0],
  [0, 0, 1, 1, 0, 1, 2, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1]
]

go_board = [[0, 2, 1, 1, 0, 1], [1, 2, 1, 1, 2, 0], [2, 1, 1, 2, 0, 0], [1, 0, 1, 2, 1, 2], [1, 1, 2, 2, 1, 0], [0, 0, 2, 1, 1, 2]]
who_won(go_board)

# Go: Who Won - Approach 2
def who_won(game_board: list):
    points1 = 0
    points2 = 0
 
    for row in game_board:
        for square in row:
            if square == 1:
                points1 += 1
            elif square == 2:
                points2 += 1
    
    if points1 > points2:
        return 1
    elif points2 > points1:
        return 2
    else:
        return 0

# Sudoku: check row - Approach 1

def row_correct(sudoku: list, row_no: int):
    short_list = []
    for i in sudoku[row_no]:
        if i != 0:
            short_list.append(i)
    if len(short_list) != len(set(short_list)):
        return False
    else:
        return True  

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 6, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

row_no = 5

row_correct(sudoku, row_no)

# Sudoku: check row - Approach 2
def row_correct(sudoku: list, row_no: int):
    short_list = []
    for item in sudoku[row_no]:
        if item!= 0:
            short_list.append(item)
    checked = []
    for item in short_list:
        if item in checked:
            return False
        checked.append(item)
    return True

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 6, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

row_no = 5

row_correct(sudoku, row_no)


# Sudoku: check row - Approach 3
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True


# Sudoku: check column - Approach 1
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    return True

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 6, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

column_correct(sudoku, 5)

# Sudoku: check column - Approach 2
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True

# Sudoku: check block - Approach 1
def block_correct(sudoku: list, row_no: int, column_no: int):
    column_range = range(column_no, column_no + 3)
    row_range = range(row_no, row_no + 3)
    numbers = []
    for i in row_range:
        for z in column_range:
            if sudoku[i][z] > 0 and sudoku[i][z] in numbers:
                return False 
            numbers.append(sudoku[i][z])
    return True

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 6, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))
print(block_correct(sudoku, 6, 3))


# Sudoku: check block - Approach 2
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True


# Sudoku: check grid - Approach 1
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(9):
        if not row_correct(sudoku, row):
            return False
    for column in range(9):
        if not column_correct(sudoku, column):
            return False
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
    return True

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))


# Sudoku: check grid - Approach 2
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True
 
def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
 
    return True

# Duplicates in a list - General Example
def duplicates(lst):
	checked = []
	for item in lst:
		if item in checked:
			return True
		checked.append(item)
	return False