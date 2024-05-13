# Write your solution here
def list_sum(list1, list2):
    new_list = []
    for i in range(len(list1)):
        sum = list1[i] + list2[i]
        new_list.append(sum)
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a,b))
    