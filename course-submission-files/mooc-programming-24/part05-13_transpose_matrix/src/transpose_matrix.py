# Write your solution here
def transpose(matrix: list):
    t_matrix = []
    for r in matrix:
        t_matrix.append(r[:])

    for row in range(len(matrix)):
        for square in range(len(matrix[row])):
            t_matrix[square][row] = matrix[row][square]    
            
    matrix[:] = t_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]   
    transpose(matrix)
    print(matrix)    