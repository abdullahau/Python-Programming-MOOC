# Write your solution here
def all_the_longest(my_list: list):
    max_len = 0
    for i in my_list:
        if len(i) > max_len:
            max_len = len(i)
    result = []
    for i in my_list:
        if len(i) == max_len:
            result.append(i)
    return result

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']