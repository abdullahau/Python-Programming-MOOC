# Write your solution here
def palindromes(string):
    item = ""
    for i in range(-1, -len(string)-1,-1):
        item += string[i]
    return string == item
        
while True:
    string = input("Please type in a palindrome: ")
    if palindromes(string) == True:
        print(f"{string} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
