# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, lottery_numbers: list) -> None:
        self.__week = week
        self.__lottery_numbers = lottery_numbers
    
    def number_of_hits(self, numbers: list) -> int:
        return len([number for number in numbers if number in self.__lottery_numbers])
    
    def hits_in_place(self, numbers: list) -> list:
        return [numbers[i] if numbers[i] in self.__lottery_numbers else -1 for i in range(7)]