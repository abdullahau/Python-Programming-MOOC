# Write your solution here
story = ""
repeat = ""
while True:
    words = input("Please type in a word: ")
    
    if words == "end":
        break
    
    if repeat == words:
        break
    
    repeat = words
    
    story += words + " "

print(story)