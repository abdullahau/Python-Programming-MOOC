# TEE RATKAISUSI TÄHÄN:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < len(self.products):
            item = self.products[self.n]
            self.n += 1
            return item
        else:
            raise StopIteration    
