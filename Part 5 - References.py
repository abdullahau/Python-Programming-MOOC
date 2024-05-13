# The function `id` can be used to find out the exact location the variable points to:
a = [1, 2, 3]
print(id(a))
b = "This is a reference, too"
print(id(b))

# Built-in types like 'str', 'int', 'float', 'bool', and 'tuples' are immutable in python
number = 1
number = 2
number += 10

number = 1
print(id(number))
number += 10
print(id(number))
a = 1
print(id(a))

# Built-in types like 'list' and 'dict' are mutable in python
a = [1, 2, 3]
b = a
b[0] = 10

# The assignment `b = a` copies the value stored in variable `a` to the variable `b`. 
# However, the value stored in `a` is not the list _itself_, but a _reference_ to the list.
# So, the assignment `b = a` copies the reference. As a result there are now two references to the same memory location containing the list.

# The list can be accessed through either of the two references:
list1 = [1, 2, 3, 4]
list2 = list1

list1[0] = 10
list2[1] = 20

print(list1)
print(list2)

# If there is more than one reference to the same list, any one of the references can be used to access the list. 
# On the other hand, a change made through any one of the references affects also the other references, as their target is the same.

# Copying a list

# If you want to create an actual separate copy of a list, you can create a new list and add each item from the original list in turn:
my_list = [1, 2, 3, 3, 5]

new_list = []
for item in my_list:
    new_list.append(item)

new_list[0] = 10
new_list.append(6)
print("the original:", my_list)
print("the copy:", new_list)

# An easier way to copy a list is the bracket operator `[]`, which we used for slices previously. 
# The notation `[:]` selects all items in the collection. As a side effect, it creates a copy of the list:
my_list = [1,2,3,4]
new_list = my_list[:]

my_list[0] = 10
new_list[1] = 20

print(my_list)
print(new_list)

# When you pass a list as an argument to a function, you are passing a reference to that list. 
# This means that the function can modify the list directly.
def add_item(my_list: list):
    new_item = 10
    my_list.append(new_item)

a_list = [1,2,3]
print(a_list)
add_item(a_list)
print(a_list)

# Notice the function `add_item` does not have a return value. It only changes the list it takes as an argument.

# Another way to implement this functionality would be to create a new list within the function, and return that:
def add_item(my_list: list) -> list:
    new_item = 10
    my_list_copy = my_list[:]
    my_list_copy.append(new_item)
    return my_list_copy

numbers = [1, 2, 3]
numbers2 = add_item(numbers)

print("original list:", numbers)
print("new list:", numbers2)

# Editing a list given as an argument

# The below funtion is an attempt at augmenting each item in a list:
def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)
    my_list = new_list

numbers = [1, 2, 3]
print("in the beginning:", numbers)
augment_all(numbers)
print("after the function is executed:", numbers)

# However, this is not achieved as the variable inside the funtion simply points to a different list that is lost inside the function.
# This can be amended by assigning new items to the list given as an argument one by one:
def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)

    # copy items from the new list into the old list
    for i in range(len(my_list)):
        my_list[i] = new_list[i]

# Useful shorthand
my_list = [1, 2, 3, 4]
my_list[1:3] = [10, 20]
my_list

# Simplified version of the list modification function
def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)

    my_list[:] = new_list

# Reimplementing the function without creating a new list within the function
def augment_all(my_list: list):
    for i in range(len(my_list)):
        my_list[i] += 10


# Side effects of functions
# The following function sorts the list given as an argument in place.
def second_smallest(my_list: list) -> int:
    # in an ordered list, the second smallest item is at index 1
    my_list.sort()
    return my_list[1]

numbers = [1, 4, 2, 5, 3, 6, 4, 7]
print(second_smallest(numbers))
print(numbers)

# To avoid side effects of sorting the list in place, we can use the 'sorted' function instead of the 'sort' method
def second_smallest(my_list: list) -> int:
    list_copy = sorted(my_list)
    return list_copy[1]

numbers = [1, 4, 2, 5, 3, 6, 4, 7]
print(second_smallest(numbers))
print(numbers)


# Items multiplied by two - Approach 1
def double_items(numbers: list):
    numbers_doubled = []
    for i in numbers:
        numbers_doubled.append(i * 2)
    return numbers_doubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
    
# Items multiplied by two - Approach 2
def double_items(numbers: list):
    double = numbers[:]
    for i in range(len(double)):
        double[i] *= 2
    
    return double

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
    
# Remove the smallest - Approach 1
def remove_smallest(numbers: list):
    min_number = min(numbers)
    min_index = numbers.index(min_number)
    numbers.pop(min_index)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
    
# Remove the smallest - Approach 1  
def remove_smallest(numbers: list):
    smallest = min(numbers)
    numbers.remove(smallest)
 
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
    

# Sudoku: print out the grid and add a number - Approach 1
def print_sudoku(sudoku: list):
    row_counter = 0
    for row in sudoku:
        column_counter = 0
        for square in row:
            if square > 0:
                print(f"{square} ", end="")
            else:
                print("_ ", end="")
            column_counter += 1
            if column_counter % 3 == 0:
                print(" ", end="")
        row_counter += 1
        print()
        if row_counter % 3 == 0:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)

# print_sudoku(sudoku: list)
# add_number(sudoku: list, row_no: int, column_no: int, number:int)

# Sudoku: print out the grid and add a number - Approach 2
def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s%3 == 0 and s < 8:# avoids adding an additional whitespace character after the last column
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8: # avoids adding an additional newline character after the last row
            print()
 
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)

# Sudoku: add number to a copy of the grid - Approach 1
def print_sudoku(sudoku: list):
    row_counter = 0
    for row in sudoku:
        column_counter = 0
        for square in row:
            column_counter += 1
            if square > 0:
                print(f"{square} ", end="")
            else:
                print("_ ", end="")
            if column_counter % 3 == 0 and column_counter < 8:
                print(" ", end="")
        print()
        row_counter += 1
        if row_counter % 3 == 0 and row_counter < 8:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = [0] * len(sudoku)
    for row in range(len(sudoku)):
        sudoku_copy[row] = [0] * len(sudoku)
    for row in sudoku:
        for square in row:
            sudoku_copy[row_no][column_no] = square
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)

# ⭐ ⭐ Sudoku: add number to a copy of the grid - Approach 2
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
 
    new_list[row_no][column_no] = number
    return new_list

# ⭐ ⭐ Creating a copy of a simple 2D list/array/matrix
y = [row[:] for row in sudoku]

# Tic-Tac-Toe - Approach 1
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < len(game_board[0]) and x >= 0 and y < len(game_board) and y >= 0:
        if game_board[y][x] == '':
            game_board[y][x] = piece
            return True
        else:
            return False
    else:
        return False    

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)

# Tic-Tac-Toe - Approach 2
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or y < 0 or x > 2 or y > 2:
        return False
 
    # Note, that y-coordinate is given first
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
 
    return False

# Transpose a matrix - Approach 1
def transpose(matrix: list):
    t_matrix = []
    t_matrix = [0] * len(matrix)
    for row in range(len(matrix)):
        for square in range(len(matrix[row])):
            t_matrix[row] = [0] * len(matrix[0])

    for row in range(len(matrix)):
        for square in range(len(matrix[row])):
            t_matrix[square][row] = matrix[row][square]
    
    matrix[:] = t_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   
transpose(matrix)
print(matrix)

# Transpose a matrix - Approach 2
def transpose(matrix: list):
    t_matrix = []
    for r in matrix:
        t_matrix.append(r[:])

    for row in range(len(matrix)):
        for square in range(len(matrix[row])):
            t_matrix[square][row] = matrix[row][square]    
            
    matrix[:] = t_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   
transpose(matrix)
print(matrix)    

# Transpose a matrix - Approach 3
def transpose(matrix: list):
    for row in range(len(matrix)):
        for square in range(row, len(matrix[row])): # starting the square loop from row to the full length (pushing diagonally down-right) ensures that squares are not reversed once the opposite cells are reached
            temp = matrix[row][square]
            matrix[row][square] = matrix[square][row]    
            matrix[square][row] = temp 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   

transpose(matrix)
print(matrix)

# Transpose a matrix - Approach 4
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

# Transpose a matrix - Approach 5
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
