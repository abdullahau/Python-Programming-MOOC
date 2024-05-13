# Write your solution here
def spruce(size):
    i = size - 1
    row = "*"
    print("a spruce!")
    while i >= 0:
        print(" " * i + row)
        row += "**"
        i -= 1  
    print(" " * (size - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)