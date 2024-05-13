# Write your solution here
from difflib import get_close_matches

if True:
    sentence = input("Write text: ")
else:
    sentence = "We use ptython to make a spell checker"

def words():
    wordlist = []
    with open("wordlist.txt") as wordfile:
        for word in wordfile:
            wordlist.append(word.strip())
    return wordlist

wordlist = words()

marked_sentence = ""
suggestions = {}
for word in sentence.split(" "):
    if word.lower() in wordlist:
        marked_sentence += word + " "
    else:
        marked_sentence += "*" + word + "* "
        suggestions[word] = get_close_matches(word.lower(), wordlist)

print(marked_sentence.strip())
print("suggestions:")
for word, suggestion in suggestions.items():
    print(word + ": "  + ", ".join(suggestions[word]))