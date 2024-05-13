# Write your solution to exercise 2 here
def copy(matrix: list) -> list:
    copied = [row[:] for row in matrix]
    return copied

def flip(matrix: list) -> None:
    for row in matrix:
        row[1], row[0] = row[0], row[1]

def flip_and_copy(matrix: list) -> list:
    copied = copy(matrix)
    flip(copied)
    return copied


if __name__ == "__main__":
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