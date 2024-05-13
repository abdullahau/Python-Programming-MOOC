# Write your solution here
string = input("Please type in a string: ")
sub = input("Please type in a substring: ")

i = string.find(sub)

if i != -1:
    string = string[i + len(sub) : ]
    z = string.find(sub)
    if z != -1:
        i += len(sub)
        print(f"The second occurrence of the substring is at index {i + z}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")