# Write your solution here
def find_words(search_term: str) -> list:
    return wildcard(search_term)

# Identify wildcard in search_term
def wildcard(search_term: str) -> list:
    if "." in search_term:
        index = 0
        search_term_dict = {}
        for letter in search_term:
            if letter != ".":
                search_term_dict[index] = letter
            index += 1
        return dot_search(search_term, search_term_dict)
    
    if search_term[0] == "*":
        return end_search(search_term[1:])
    
    if search_term[len(search_term) - 1] == "*":
        return start_search(search_term[:-1])
    
    else:
        return exact_search(search_term)
    
# Conduct search based on wildcard feature 
def dot_search(search_term: str, search_term_dict: dict) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if len(word) == len(search_term):
                z = True
                helper = ""
                for index, letter in search_term_dict.items():
                    if word[index] == letter and z:
                        helper = word
                    else:
                        helper = ""
                        z = False
                if z:
                    match.append(helper)
    return match

def end_search(search_term_suffix: str) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if word.endswith(search_term_suffix):
                match.append(word)
    return match

def start_search(search_term_prefix: str) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if word.startswith(search_term_prefix):
                match.append(word)
    return match

def exact_search(search_term: str) -> list:
    match = []
    with open("words.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            if word == search_term:
                match.append(word)
    return match