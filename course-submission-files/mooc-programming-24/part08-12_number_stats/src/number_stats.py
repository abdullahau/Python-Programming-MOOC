# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.addcount = 0
        self.evensum = 0
        self.oddsum = 0

    def add_number(self, number:int):
        self.numbers += number
        self.addcount += 1
        self.evensum += number if number % 2 == 0 else 0
        self.oddsum += number if number % 2 != 0 else 0

    def count_numbers(self):
        return self.addcount
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        return (self.numbers / self.addcount) if self.numbers > 0 else 0
    
    def even_number_sum(self):
        return self.evensum
    
    def odd_number_sum(self):
        return self.oddsum

stats = NumberStats()
print("Please type in integer numbers:")
while True:
    number = int(input())
    if number != -1:
        stats.add_number(number)
    else:
        break

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {stats.even_number_sum()}")
print(f"Sum of odd numbers: {stats.odd_number_sum()}")
