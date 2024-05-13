# Write your solution here
def shortest(my_list: list):
    word = my_list[0]
    for i in my_list:
        if len(i) < len(word):
            word = i
    return word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)