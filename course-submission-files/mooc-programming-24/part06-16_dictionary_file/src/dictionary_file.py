# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish};{english}\n")
            print("Dictionary entry added")
        continue
    if function == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                parts = line.strip()
                part = parts.split(";")
                if search in part[0] or search in part[1]:
                    print(f"{part[0]} - {part[1]}")
        continue
    else:
        print("Bye!")
        break