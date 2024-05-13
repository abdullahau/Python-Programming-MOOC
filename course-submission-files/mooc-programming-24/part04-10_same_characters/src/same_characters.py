# Write your solution here
def same_chars(string, index, index2):
    if index > len(string) - 1 or index2 > len(string) - 1:
        return False
    elif string[index] == string[index2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))