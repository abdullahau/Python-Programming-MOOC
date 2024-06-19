class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.__name = name
        self.__ingredients = ingredients
        self.__time = time
        self.__instructions = instructions
    
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

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self.__name = name

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

class RecipeBook:

    def __init__(self):
        self.__recipe_book = []
        
    # __str__ method that returns the program's information as shown in the example below.
    def __str__(self) -> str:
        line = "RecipeBook:\n"
        for recipe in self.__recipe_book:
            line += f"{recipe}\n"
        return line
        
    # add_recipe method. The method adds the given Recipe object to the __recipe_book attribute. You can assume that no two recipes with the same name will be added.
    def add_recipe(self, recipe: Recipe):
        self.__recipe_book.append(recipe)
        
    # remove_recipe method. The method removes the given Recipe object from the __recipe_book attribute. You can assume that only existing Recipe objects are attempted to be removed.
    def remove_recipe(self, recipe: Recipe):
        self.__recipe_book.remove(recipe)

    # recipe_by_name method. The method takes a string as an argument. The method returns a Recipe object whose name matches the given string. If no matching recipe object is found, the method should return None.
    def recipe_by_name(self, name: str) -> Recipe:
        for recipe in self.__recipe_book:
            if recipe.name == name:
                return recipe
        return None

    # recipes_containing_ingredients method. The method takes a list of strings as an argument. The method returns a list of Recipe objects, each of which contains all of the specified ingredients in its attributes. If no Recipe objects matching the criteria are found, the method should return an empty list. You can think of this method for example so that you have chicken and salad in your fridge and you are looking to use them and will buy the other required ingredients separately.
    def recipes_containing_ingredients(self, ingredients: list[str]) -> list[Recipe]:
        recipe_list = []
        
        for recipe in self.__recipe_book:
            if all(ingredient in recipe.ingredients for ingredient in ingredients):
                recipe_list.append(recipe)
        
        return recipe_list      

    # recipes_within_time method that takes an integer as an argument. The method returns a list of Recipe objects whose cooking time is at most equal to the given argument. If no recipe objects matching the criteria are found, the method should return an empty list.
    def recipes_within_time(self, time: int) -> list[Recipe]:
        recipe_list = []
        
        for recipe in self.__recipe_book:
            if recipe.time <= time:
                recipe_list.append(recipe)
        
        return recipe_list
    
    # recipes_with_all_ingredients method. The method takes a list of strings as an argument. The method returns a list of all Recipe objects whose ingredients are all found in the list given to the method. If no recipe objects matching the criteria are found, the method should return an empty list. You can think of this method for example so that the given ingredients are all available aleready and you will not buy additional ingredients.
    def recipes_with_all_ingredients(self, ingredients: list[str]) -> list[Recipe]:
        recipe_list = []
        
        for recipe in self.__recipe_book:
            if all(ingredient in ingredients for ingredient in recipe.ingredients):
                recipe_list.append(recipe)
    
        return recipe_list         

    # all_recipes method. The method returns a list containing all the Recipe objects stored in the RecipeBook object. If the list returned by the method is modified, it does not affect the RecipeBook object.
    def all_recipes(self):
        recipe_list = self.__recipe_book[:]
        return recipe_list


r1 = Recipe("Chicken", ["Chicken", "Salt"], 15, "Fry the chicken in a frying pan. Add salt.")
r2 = Recipe("Caesar Salad", ["Lettuce", "Chicken", "Dressing"], 25, "Cook the chicken. Place lettuce on a plate. Add chicken. Add dressing.")
r3 = Recipe("Blueberry Muffins", ["Flour", "Milk", "Sugar", "Blueberries"], 30, "Mix ingredients. Bake muffins at 180 degrees.")

recipe_book = RecipeBook()
recipe_book.add_recipe(r1)
recipe_book.add_recipe(r2)    
recipe_book.add_recipe(r3)
print(recipe_book)
print()

chicken = recipe_book.recipe_by_name("Chicken")
print("Recipe with search 'Chicken':", chicken)
print("Recipe with search 'Risotto':", recipe_book.recipe_by_name("Risotto"))
print()

recipes_with_ingredients = recipe_book.recipes_containing_ingredients(["Chicken", "Dressing"])
print("Recipes that contain the ingredients 'Chicken', 'Dressing':", recipes_with_ingredients)
print()

recipes_can_be_made_with = recipe_book.recipes_with_all_ingredients(["Chicken", "Salt", "Dressing", "Lettuce"])
print("Recipes that can be made with ingredients 'Chicken', 'Salt', 'Dressing', and 'Lettuce':", recipes_can_be_made_with)

print()
within_time = recipe_book.recipes_within_time(20)
print(within_time)
print("Recipes whose only ingredient is water:", recipe_book.recipes_with_all_ingredients(["Water"]))
print("Recipes that can be made in one minute:", recipe_book.recipes_within_time(1))
print()
print("All known recipes:")
print(recipe_book.all_recipes())