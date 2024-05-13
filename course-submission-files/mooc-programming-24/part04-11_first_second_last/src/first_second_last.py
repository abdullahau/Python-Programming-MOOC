# Write your solution here
def first_word(sentence):
    index = sentence.find(" ")
    return sentence[0:index]

def second_word(sentence):
    index = sentence.find(" ")
    sentence = sentence[index + 1: len(sentence)]
    if sentence.find(" ") < 0:
        return sentence
    else:
        return sentence[0:sentence.find(" ")]

def last_word(sentence):
    i = - 1
    reverse = ""
    while i >= -len(sentence):
        reverse += sentence[i]
        i -= 1
    invert_index = - reverse.find(" ")
    return sentence[invert_index:]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))