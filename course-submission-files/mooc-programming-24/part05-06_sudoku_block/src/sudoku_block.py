# Write your solution here
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

if __name__ == "__main__":
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