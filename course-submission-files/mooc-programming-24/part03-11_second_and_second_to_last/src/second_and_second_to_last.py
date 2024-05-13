# Write your solution here
string = input("Please type in a string: ")

second = string[1]
second_last = string[-2]

if second == second_last:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")