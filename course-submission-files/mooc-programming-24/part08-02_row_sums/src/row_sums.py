# Write your solution here
def row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        total = 0
        for num in my_matrix[i]:
            total += num
        my_matrix[i].append(total)