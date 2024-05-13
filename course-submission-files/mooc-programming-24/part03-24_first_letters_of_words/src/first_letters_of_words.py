# Write your solution here
sentence = input("Please type in a sentence: ")

print(sentence[0])

while True:
    i = sentence.find(" ")
    sentence = sentence[i+1:]
    if i == -1:
        break
    print(sentence[0])