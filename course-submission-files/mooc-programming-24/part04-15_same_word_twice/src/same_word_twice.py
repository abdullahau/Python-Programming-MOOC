# Write your solution here
list =[]
while True:
    word = input("Word: ")
    if word in list:
        break
    list.append(word)

print(f"You typed in {len(list)} different words")