# Write your solution here
def no_vowels(my_string: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        my_string = my_string.replace(i, "")
    return my_string

if __name__ == '__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))