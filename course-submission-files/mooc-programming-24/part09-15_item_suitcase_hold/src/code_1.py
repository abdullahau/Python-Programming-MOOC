# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
        
    def weight(self):
        return self.__weight
    
    def name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
    
    def weight(self):
        total_weight = sum(item.weight() for item in self.__items)
        return total_weight
    
    def add_item(self, item: Item):
        prior_weight = self.weight()
        if prior_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)
    
    def heaviest_item(self):
        heaviest_item = None
        heaviest_weight = 0 
        for item in self.__items:
            if heaviest_item == None or item.weight() > heaviest_weight:
                heaviest_item = item
                heaviest_weight = item.weight()
        return heaviest_item
    
    def print_items(self):
        line = ""
        for item in self.__items:
            line += f"{item.name()} ({item.weight()} kg)\n"
        print(line[:-1])
    
    def __str__(self):
        total_weight = self.weight()
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({total_weight} kg)"
        return f"{len(self.__items)} items ({total_weight} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        prior_weight = sum(suitcase.weight() for suitcase in self.__suitcases)
        if prior_weight + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()
    
    def __str__(self):
        total_weight = sum(suitcase.weight() for suitcase in self.__suitcases)
        if len(self.__suitcases) == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - total_weight} kg"
        return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - total_weight} kg"