# Write your solution here
from random import sample

def words(n: int, beginning: str) -> list:
    with open("words.txt") as words:
        match = []
        for word in words:
            word = word.strip()
            if word.startswith(beginning):
                match.append(word)
    
    if len(match) < n:
        raise ValueError(f"n sample size of {n} is larger than the matched list of length {len(match)}")
    else:
        return sample(match, k = n)
    
if __name__ == "__main__":
    word_list = words(15, "xeno")
    for word in word_list:
        print(word)