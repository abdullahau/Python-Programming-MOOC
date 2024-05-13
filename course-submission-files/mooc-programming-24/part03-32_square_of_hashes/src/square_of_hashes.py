# Write your solution here
def hash_square(length):
    i = length
    while i > 0:
        print("#" * length)
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)