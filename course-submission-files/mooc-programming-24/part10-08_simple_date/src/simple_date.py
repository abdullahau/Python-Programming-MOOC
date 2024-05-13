# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year
        
    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"
    
    def __date_to_days(self) -> int:
        return ((self.__year - 1) * 360) + ((self.__month - 1) * 30) + (self.__date - 1)
    
    def __days_to_date(self, days: int) -> "SimpleDate":
        year_cal, remainder = divmod(days, 360)
        month_cal, day_cal = divmod(remainder, 30)
        return SimpleDate(day_cal+1, month_cal+1, year_cal+1)     
    
    def __lt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() < another.__date_to_days()
    
    def __gt__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() > another.__date_to_days()
    
    def __eq__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() == another.__date_to_days()
    
    def __ne__(self, another: 'SimpleDate') -> bool:
        return self.__date_to_days() != another.__date_to_days()
    
    def __add__(self, days: int) -> 'SimpleDate':
        return self.__days_to_date(self.__date_to_days() + days)
    
    def __sub__(self, another: 'SimpleDate') -> 'SimpleDate':
        current_date = self.__date_to_days() - another.__date_to_days()
        return abs(current_date)
