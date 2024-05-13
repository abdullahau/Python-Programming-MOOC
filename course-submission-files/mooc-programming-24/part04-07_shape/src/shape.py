def line(number, string):
    if string == "":
        string = "*"
    print(string[0] * number)
    
def shape(width, triangle, height, rectangle):
    i = 0
    while i < width:
        i += 1
        line(i, triangle)
    i = 0
    while i < height:
        line(width, rectangle)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")