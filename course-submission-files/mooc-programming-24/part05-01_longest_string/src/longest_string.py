# Write your solution here
def longest(strings: list):
    length = 1
    for i in strings:
        if len(i) > length:
            length = len(i)
            string = i
    return string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    longest(strings)