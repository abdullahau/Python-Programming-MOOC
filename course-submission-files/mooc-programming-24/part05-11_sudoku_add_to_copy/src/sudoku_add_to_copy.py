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
    for row in range(len(sudoku_copy)):
        sudoku_copy[row] = [0] * len(sudoku)
    for row in sudoku:
        for square in row:
            sudoku_copy[row_no][column_no] = square
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__ == "__main__":
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