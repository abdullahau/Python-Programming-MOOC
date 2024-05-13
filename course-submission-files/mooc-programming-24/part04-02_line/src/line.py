# Write your solution here
def line(number, string):
    if string == "":
        string = "*"
    string = " " + string
    print(string[1] * number)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")