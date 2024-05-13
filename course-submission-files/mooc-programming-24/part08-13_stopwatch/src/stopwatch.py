# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.counter = 0
    
    def tick(self):
        self.counter += 1
        hours, remainder = divmod(self.counter, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
        
        
    def __str__(self) -> str:
        return f"{self.minutes:02d}:{self.seconds:02d}"