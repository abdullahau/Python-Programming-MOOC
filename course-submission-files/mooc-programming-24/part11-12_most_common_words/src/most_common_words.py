# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        line = " ". join([i for i in f])
        line = line.strip().split()
        line = [word.strip("!#$%&'()*+,-./:;<=>?@[]^_`{|}~") for word in line]
    return {word: line.count(word) for word in line if line.count(word) >= lower_limit}