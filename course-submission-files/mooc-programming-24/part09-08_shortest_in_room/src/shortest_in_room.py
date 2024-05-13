# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        
    def add(self, person: Person):
        self.persons.append(person)
        
    def is_empty(self):
        return len(self.persons) == 0
    
    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortest_person = self.persons[0]
            for person in self.persons[1:]:
                if person.height < shortest_person.height:
                    shortest_person = person
            return shortest_person
    
    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            index = self.persons.index(self.shortest())
            return self.persons.pop(index)
    
    def print_contents(self):
        height = sum(person.height for person in self.persons)
        line = f'There are {len(self.persons)} persons in the room, and their combined height is {height} cm\n'
        for person in self.persons:
            line += f"{person} ({person.height} cm)\n"
        print(line)