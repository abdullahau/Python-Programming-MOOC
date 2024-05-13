# Write your solution here
items = int(input("How many items: "))
my_list = []
i = 0
while i < items:
    item = int(input(f"Item {i+1}: "))
    my_list.append(item)
    i += 1
print(my_list)