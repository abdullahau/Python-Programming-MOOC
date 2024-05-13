# Copy here code of line function from previous exercise
def line(number, string):
    if string == "":
        string = "*"
    print(string[0] * number)

def square_of_hashes(length):
    i = 0
    while i < length:
        line(length, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)