# Write your solution here
def read_input(input_string: str, lower_bound: int, upper_bound: int):
    while True:
        try:
            number = int(input(input_string))
            if number > lower_bound and number < upper_bound:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_bound} and {upper_bound}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print(f"You typed in: {number}")