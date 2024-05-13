# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def __unique_and_frequency(cls, my_list: list):
        list_unique = []
        for item in my_list:
            if item not in list_unique:
                list_unique.append(item)
        
        frequency = []
        for item in list_unique:
            frequency.append(my_list.count(item))
        
        return list_unique, frequency     
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        list_unqiue, frequency = cls.__unique_and_frequency(my_list)
        return list_unqiue[frequency.index(max(frequency))]
    
    @classmethod
    def doubles(cls, my_list: list):
        list_unqiue, frequency = cls.__unique_and_frequency(my_list)
        return len(frequency) - frequency.count(1)