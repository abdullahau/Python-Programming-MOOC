class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__total = self.__euros + (self.__cents / 100)

    def __str__(self) -> str:
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, another: 'Money') -> bool:
        return self.__total == another.__total
    
    def __lt__(self, another: 'Money') -> bool:
        return self.__total < another.__total
    
    def __gt__(self, another: 'Money') -> bool:
        return self.__total > another.__total
    
    def __ne__(self, another: 'Money') -> bool:
        return self.__total != another.__total
    
    def __add__(self, another: 'Money') -> 'Money':
        total_cents = self.__cents + another.__cents
        total_euros = self.__euros + another.__euros
        if total_cents >= 100:
            total_euros += 1
            total_cents -= 100
        return Money(total_euros, total_cents)
    
    def __sub__(self, another: 'Money') -> 'Money':
        total_euros = self.__euros - another.__euros
        total_cents = self.__cents - another.__cents
        if (total_cents < 0 and total_euros == 0) or total_euros < 0:
            raise ValueError("a negative result is not allowed")
        else:
            if total_cents < 0:
                total_cents += 100
                total_euros -= 1
            return Money(total_euros, total_cents)