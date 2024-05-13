class RealProperty:
    def __init__(self, rooms: int , square_meters: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to):
        # Function abs returns absolute value
        difference = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return difference

    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return difference > 0


    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, ' + 
            f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')

# WRITE YOUR SOLUTION HERE:
def cheaper_properties(properties: list, reference: RealProperty):
    return [(prop, prop.price_difference(reference)) for prop in properties if not prop.more_expensive(reference) and prop != reference]