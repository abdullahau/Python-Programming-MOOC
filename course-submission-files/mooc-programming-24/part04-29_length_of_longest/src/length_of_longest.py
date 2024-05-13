# Write your solution here
def length_of_longest(my_list: list):
    max_len = 0
    for i in my_list:
        if len(i) > max_len:
            max_len = len(i)
    return max_len

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)