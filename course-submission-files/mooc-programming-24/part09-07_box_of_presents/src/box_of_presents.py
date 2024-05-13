# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight
        
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self) -> None:
        self.box = []
        
    def add_present(self, present: Present) -> None:
        self.box.append(present)
    
    def total_weight(self) -> int:
        return sum(item.weight for item in self.box) 