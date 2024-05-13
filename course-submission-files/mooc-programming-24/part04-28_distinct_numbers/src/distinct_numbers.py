# Write your solution here
def distinct_numbers(my_list):
    new_list = []
    sorted_list = sorted(my_list)
    for i in range(len(sorted_list)):
        if sorted_list[i] in new_list:
            continue
        else:
            new_list.append(sorted_list[i])
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]