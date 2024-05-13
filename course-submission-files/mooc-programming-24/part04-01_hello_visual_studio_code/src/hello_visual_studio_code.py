# Write your solution here
while True:
    editor = input("Editor: ")
    lowercase = editor.lower()
    if lowercase == "visual studio code":
        print("an excellent choice!")
        break
    elif lowercase == "word" or lowercase == "notepad":
        print("awful")
    else:
        print("not good")