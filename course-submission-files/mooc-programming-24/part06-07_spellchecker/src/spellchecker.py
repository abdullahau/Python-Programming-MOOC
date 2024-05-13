# write your solution here
text = input("Write text: ")
text = text.split(" ")

with open("wordlist.txt") as wordlist:
    words = []
    for line in wordlist:
        word = line.strip()
        words.append(word)

sentence = ""
for texts in text:
    if texts.lower() in words:
        sentence += texts + " "
    else:
        sentence += "*" + texts + "* "

print(sentence.strip())