# Write your solution here

word = input("Please type in a word: ")
letter = input("Please type in a character: ")

i = word.find(letter)

if i >= 0 and i+3 <= len(word):
    print(word[i:i+3])
