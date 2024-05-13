# write your solution here
def read_fruits():
    with open('fruits.csv') as new_file:
        my_dict = {}
        
        for line in new_file:
            parts = line.split(";")
            my_dict[parts[0]] = float(parts[1])
    return my_dict

if __name__ == "__main__":
    read_fruits()
