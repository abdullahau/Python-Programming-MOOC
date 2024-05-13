# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i == -1:
        break
    value = int(input("New Value: "))
    my_list[i] = value
    print(my_list)