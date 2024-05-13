# write your solution here
def largest():
    with open('numbers.txt') as new_file:
        largest_number = 0
        
        for line in new_file:
            number = int(line)
            if number > largest_number:
                largest_number = number
        return largest_number

if __name__ == "__main__":
    largest()