# Write your solution to exercise 1 here

input_numbers = []


def most_repeated(input_numbers: list[int]) -> int:
    counter = 0
    for i in input_numbers:
        if input_numbers.count(i) > counter:
            counter = input_numbers.count(i)
            common_int = i
    return common_int
    

while True:
    num = int(input("Type in a number: "))
    
    if num == 0:
        print(f"Biggest: {max(input_numbers)}")
        print(f"Smallest: {min(input_numbers)}")
        print(f"Number of numbers: {len(input_numbers)}")
        print(f"Sum: {sum(input_numbers)}")
        print(f"Most repeated: {most_repeated(input_numbers)}")
        break
    else:
        input_numbers.append(num)
        continue
