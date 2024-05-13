# Write your solution here
def most_common_character(my_string: str):
    count = 0
    for i in my_string:
        if my_string.count(i) > count:
            count = my_string.count(i)
            common_character = i
    return common_character

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))