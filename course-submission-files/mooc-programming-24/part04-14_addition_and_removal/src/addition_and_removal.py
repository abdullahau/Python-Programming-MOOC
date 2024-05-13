# Write your solution here
list = []
print(f"The list is now {list}")
i = 0
while True:
    instruction = input("a(d)d, (r)emove or e(x)it: ")
    if instruction == "x":
        print("Bye!")
        break
    elif instruction == "r":
        list.pop(i-1)
        i -= 1
    else:
        list.insert(i, i + 1)
        i += 1
    print(f"The list is now {list}")