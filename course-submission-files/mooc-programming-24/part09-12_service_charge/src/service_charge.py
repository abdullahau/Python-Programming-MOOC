# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, owner: str, acount_number: str, balance: float) -> None:
        self.__owner = owner
        self.__acount = acount_number
        self.__balance = balance
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()
    
    def __service_charge(self):
        self.__balance *= (1 - 0.01)
