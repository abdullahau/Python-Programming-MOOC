# Write your solution here
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
    chessboard(3)
