# write your solution here
def matrix_sum():
    with open("matrix.txt") as matrix:
        sum = 0
        
        for row in matrix:
            row = row.replace("\n", "")
            row = row.split(",")
            for num in row:
                element = int(num)
                sum += element 
        return sum


def matrix_max():
    with open("matrix.txt") as matrix:
        max = 0
        
        for row in matrix:
            row = row.replace("\n", "")
            row = row.split(",")
            for num in row:
                element = int(num)
                if element > max:
                    max = element
        return max


def row_sums():
    with open("matrix.txt") as matrix:
        sums = []
        
        for row in matrix:
            row = row.replace("\n", "")
            row = row.split(",")
            sum = 0
            for num in row:
                element = int(num)
                sum += element
            sums.append(sum)
        return sums
    
if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()