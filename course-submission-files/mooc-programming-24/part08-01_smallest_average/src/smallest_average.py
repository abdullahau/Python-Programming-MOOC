# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    collection = (person1, person2, person3)
    
    avg_list = []
    for person in collection:
        total = 0
        for i in range(3):
            total += person["result"+str(i+1)]
        avg_list.append(total/3)

    return collection[avg_list.index(min(avg_list))]