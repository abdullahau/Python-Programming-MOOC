class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.__name = name
        self.__ingredients = ingredients
        self.__time = time
        self.__instructions = instructions
    
    # Getter method for all encapsulated attributes as shown in the example below.
    @property
    def name(self):
        return self.__name
    
    @property
    def ingredients(self):
        return self.__ingredients
    
    @property
    def time(self):
        return self.__time
    
    @property
    def instructions(self):
        return self.__instructions

    # Setter method for the __name attribute. The setter method should only set a new value if the new string is at least 3 characters long.
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self.__name = name

    # Comparison operators for comparing the cooking time of two recipes, i.e., the operators <=, >= and ==.
    # The <= operator should return True if the __time attribute of the first object is smaller or equal to the second objects __time-attribute. 
    # Similarly, the operator should return False if the __time attribute of the first object is greater than that of the second object.

    # The >= operator should return True if the __time attribute of the first object is greater or equal to the second objects __time-attribute. 
    # Similarly, the operator should return False if the __time attribute of the first object is smaller than that of the second object.
    # The ==-operator should retrun True if the objects __time-attrributes are exactly the same, otherwise it should return False.
    def __eq__(self, another_recipe: 'Recipe') -> bool:
        return self.__time == another_recipe.__time

    def __lt__(self, another_recipe: 'Recipe') -> bool:
        return self.__time < another_recipe.__time

    def __le__(self, another_recipe: 'Recipe') -> bool:
        return self.__time <= another_recipe.__time

    def __gt__(self, another_recipe: 'Recipe') -> bool:
        return self.__time > another_recipe.__time    

    def __ge__(self, another_recipe: 'Recipe') -> bool:
        return self.__time >= another_recipe.__time

    def __ne__(self, another_recipe: 'Recipe') -> bool:
        return self.__time != another_recipe.__time

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"
    


r1 = Recipe("Chicken", ["Chicken", "Salt"], 15, "Fry the chicken. Add salt.")
print(r1.name)

r1.name = "Delicious Chicken"
print("Name changed")
print("New name:", r1.name)

r1.name = "DC"
print("Name changed")
print("Name did not change, still:", r1.name)
r1.name = 123
print("Name can't be changed to other than string, so it's still:", r1.name)

try:
    r1.time = 5
except AttributeError:
    print("Time cannot be changed")

try:
    r1.ingredients = ["Chicken", "Salt", "Pepper"]
except AttributeError:
    print("Ingredients cannot be changed")

try:
    r1.instructions = "Fry the chicken. Add salt and pepper." 
except AttributeError:
    print("Instructions cannot be changed")
  
# OUTPUT:  
# Chicken
# Name changed
# New name: Delicious Chicken
# Name changed
# Name did not change, still: Delicious Chicken
# Name can't be changed to other than string, so it's still: Delicious Chicken
# Time cannot be changed
# Ingredients cannot be changed
# Instructions cannot be changed

r1 = Recipe("Chicken", ["Chicken", "Salt"], 15, "Fry the chicken in a pan. Add salt.")
r2 = Recipe("Caesar Salad", ["Lettuce", "Chicken", "Dressing"], 25, "Cook the chicken. Put the lettuce on a plate. Add chicken. Add dressing.")

print("r1 > r2:", r1 > r2)
print("r1 < r2:", r1 < r2)

# OUTPUT:
# r1 > r2: False
# r1 < r2: True