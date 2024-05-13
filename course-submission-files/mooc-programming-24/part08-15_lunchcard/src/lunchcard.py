# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
        
    def deposit_money(self, deposit: float):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        else:
            self.balance += deposit
        
    def eat_lunch(self):
        self.balance = self.balance - 2.60 if self.balance >= 2.60 else self.balance
        
    def eat_special(self):
        self.balance = self.balance - 4.60 if self.balance >= 4.60 else self.balance

    def __str__(self):
        return f"The balance is {self.balance:0.1f} euros"

# Create a lunch card for Peter. The initial balance on the card is 20 euros.
peters_card = LunchCard(20)
# Create a lunch card for Grace. The initial balance on the card is 30 euros.
graces_card = LunchCard(30)
# Peter eats a special
peters_card.eat_special()
# Grace eats a regular lunch
graces_card.eat_lunch()
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
print("Peter:", peters_card)
print("Grace:", graces_card)
# Peter deposits 20 euros
peters_card.deposit_money(20)
# Grace eats the special
graces_card.eat_special()
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
print("Peter:", peters_card)
print("Grace:", graces_card)
# Peter eats a regular lunch
peters_card.eat_lunch()
# Peter eats a regular lunch
peters_card.eat_lunch()
# Grace deposits 50 euros
graces_card.deposit_money(50)
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
print("Peter:", peters_card)
print("Grace:", graces_card)