# Write your solution here
word = input("Please type in a word: ")
letter = input("Please type in a character: ")

length = len(word)
i = word.find(letter)

while i != -1 and i <= length - 3:
    print(word[i : i +3])
    word = word[i + 1 :]
    i = word.find(letter)
    length = len(word)

