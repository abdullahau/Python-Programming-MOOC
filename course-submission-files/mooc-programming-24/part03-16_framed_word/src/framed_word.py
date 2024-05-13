# Write your solution here

word = input("Word: ")
lenght = len(word)

print("*" * 30)

begspace = int((30 - lenght)/2 - 1)
endspace = 30 - 2 - begspace - lenght

print("*" + " " * begspace + word + " " * endspace + "*")

print("*" * 30)