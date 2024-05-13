# Write your solution here
contact = {}

while True:
    user_input = int(input("command (1 search, 2 add, 3 quit): "))
    if user_input == 1:
        name = input("name: ")
        if name in contact:
            for num in contact[name]:
                print(num)
            continue
        else:
            print("no number")
            continue
    if user_input == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in contact:
            contact[name] = []
        contact[name].append(number)
        print("ok!") 
        continue
    else:
        print("quitting...")
        break