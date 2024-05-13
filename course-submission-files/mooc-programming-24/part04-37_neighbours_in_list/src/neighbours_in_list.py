# Write your solution here
def longest_series_of_neighbours(my_list: list):
    counter = 0
    counter_max = 1
    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            counter += 1
        else:
            if counter_max < counter:
                counter_max = counter
            counter = 0
    return max(counter, counter_max) + 1
    
if __name__ == '__main__':
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list))