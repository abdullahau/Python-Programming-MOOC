# Write your solution here:
class Clock:
    def __init__(self, hours:int, minutes:int, seconds:int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    
    def tick(self):
        self.seconds += 1
        total_seconds = self.seconds + (self.minutes*60) + (self.hours*60*60)
        days, remainder = divmod(total_seconds, 86400)
        self.hours, remainder = divmod(remainder, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
    
    def set(self, hour:int, minutes:int):
        self.hours = hour
        self.minutes = minutes
        self.seconds = 0
        
    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"