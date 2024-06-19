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
        
    def __str__(self) -> str:
        line = "RecipeBook:\n"
        for recipe in self.__recipe_book:
            line += f"{recipe}\n"
        return line
        
    def add_recipe(self, recipe: Recipe):
        self.__recipe_book.append(recipe)
        
    def remove_recipe(self, recipe: Recipe):
        self.__recipe_book.remove(recipe)

    def recipe_by_name(self, name: str) -> Recipe:
        for recipe in self.__recipe_book:
            if recipe.name == name:
                return recipe
        return None

    def recipes_containing_ingredients(self, ingredients: list[str]) -> list[Recipe]:
        recipe_list = []
        
        for recipe in self.__recipe_book:
            if all(ingredient in recipe.ingredients for ingredient in ingredients):
                recipe_list.append(recipe)
        
        return recipe_list      

    def recipes_within_time(self, time: int) -> list[Recipe]:
        recipe_list = []
        
        for recipe in self.__recipe_book:
            if int(recipe.time) <= time:
                recipe_list.append(recipe)
        
        return recipe_list
    
    def recipes_with_all_ingredients(self, ingredients: list[str]) -> list[Recipe]:
        recipe_list = []
        
        for recipe in self.__recipe_book:
            if all(ingredient in ingredients for ingredient in recipe.ingredients):
                recipe_list.append(recipe)
    
        return recipe_list         

    def all_recipes(self):
        recipe_list = self.__recipe_book[:]
        return recipe_list
    
    def clear_book(self):
        self.__recipe_book = []

class RecipeApplication:
    def __init__(self):
        self.__recipebook = RecipeBook()
        self.memory_load()
        
    def memory_load(self):
        try:
            with open("recipes.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    parts = line.split(";")
                    recipe = Recipe(parts[0], parts[1].split(','), parts[2], parts[3])
                    self.__recipebook.add_recipe(recipe)
        except FileNotFoundError:
            open("recipes.txt", "w")

    def write_to_file(self, recipe: Recipe):
        with open("recipes.txt", "a") as f:
            f.write(f"{recipe.name};{recipe.ingredients};{recipe.time};{recipe.instructions}\n")
    
    def help(self):
        print("Commands:")
        print("0 - Exit")
        print("1 - Add recipe")
        print("2 - Remove recipe")
        print("3 - Search recipe by name")
        print("4 - Search recipe by ingredients")
        print("5 - Search recipe by preparation time")
        print("6 - Search recipe by available ingredients")  
        print("7 - Return all recipes")
        print("8 - Clear memory")

    def add_recipe(self):
        name = input("Enter recipe name: ")
        if self.__recipebook.recipe_by_name(name):
            print("Recipe already exists")
        else:
            ingredients = input("Enter recipe ingredients separated by comma: ")
            time = input("Enter recipe cooktime (min): ")
            instructions = input("Enter recipe instructions: ")
            recipe = Recipe(name, ingredients, time, instructions)
            self.__recipebook.add_recipe(recipe)
            self.write_to_file(recipe)
            print(f"Added recipe {name}")
    
    def remove_recipe(self):
        name = input("Enter name of recipe to remove: ")
        if self.__recipebook.recipe_by_name(name):
            with open("recipes.txt", 'r') as file:
                lines = file.readlines()
            lines = [line for line in lines if line.strip().split(";")[0] != name]
            with open("recipes.txt", 'w') as file:
                file.writelines(lines)
            self.__recipebook.remove_recipe(self.__recipebook.recipe_by_name(name))
            print(f"Removed recipe {name}")
        else:
            print(f"No recipe found with name {name}")            
    
    def name_search(self):
        name = input("Enter recipe name to search: ")
        recipe = self.__recipebook.recipe_by_name(name)
        if recipe:
            print(f"Found recipe: {recipe}")
        else:
            print(f"No recipe found with name {name}")
    
    def ingredient_search(self):
        ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas: ")
        ingredients = ingredients.split(",")
        recipes = self.__recipebook.recipes_containing_ingredients(ingredients)
        if len(recipes) > 0:
            print(f"Found recipes with ingredients {ingredients}")
            for item in recipes:
                print(item)
        else:
            print(f"No recipe found with ingredients {ingredients}")
    
    def time_search(self):
        time = int(input("Enter the preparation time of the recipe you're looking for (min): "))
        recipes = self.__recipebook.recipes_within_time(time)
        if len(recipes) > 0:
            print(f"Found recipes with preparation time {time} min:")
            for item in recipes:
                print(item)
        else:
            print(f"No recipe found with preparation time {time} min")
    
    def available_ingredient_search(self):
        ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas: ")
        ingredients = ingredients.split(",")
        recipes = self.__recipebook.recipes_with_all_ingredients(ingredients)
        if len(recipes) > 0:
            print(f"Found recipes with ingredients {ingredients}")
            for item in recipes:
                print(item)
        else:
            print(f"No recipe found with ingredients {ingredients}")
    
    def all_recipe(self):
        recipes = self.__recipebook.all_recipes()
        if len(recipes) > 0:
            print("Found recipes:")
            for recipe in recipes:
                print(recipe)
        else:
            print("No recipes found")
    
    def clear(self):
        open("recipes.txt", "w")
        self.__recipebook.clear_book()
        print("Memory cleared")

    def execute(self):
        print("Recipe book program")
        self.help()
        while True:
            command = input("Enter command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_recipe()
            elif command == "2":
                self.remove_recipe()
            elif command == "3":
                self.name_search()
            elif command == "4":
                self.ingredient_search()
            elif command == "5":
                self.time_search()
            elif command == "6":
                self.available_ingredient_search()
            elif command == "7":
                self.all_recipe()
            elif command == "8":
                self.clear()                
            else:
                self.help()
                continue     

application = RecipeApplication()
application.execute()