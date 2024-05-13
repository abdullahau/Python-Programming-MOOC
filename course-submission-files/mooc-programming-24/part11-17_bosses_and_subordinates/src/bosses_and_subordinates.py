# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)



def count_subordinates(employee: Employee):
    total_subordinates = 0
    
    if len(employee.subordinates) > 0:
        total_subordinates += len(employee.subordinates)
        
        for i in employee.subordinates:  
            total_subordinates += count_subordinates(i)

    return total_subordinates