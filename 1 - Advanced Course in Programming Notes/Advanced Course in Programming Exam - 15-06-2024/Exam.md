# Advanced Course Exam, Summer 2024 (15/06/2024)

## Exercise 1

Complete this in exercise template `exercise1.py`

Copy the code below into the exercise template. Do not modify the given attributes or the `__repr__` method.

```python
class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.__name = name
        self.__ingredients = ingredients
        self.__time = time
        self.__instructions = instructions

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"
```

Program the following functionality for the `Recipe` class:

-   Getter method for all encapsulated attributes as shown in the example below.
-   Setter method for the `__name` attribute. The setter method should only set a new value if the new string is at least 3 characters long. **Do not create setter methods for other attributes.**
-   Comparison operators for comparing the cooking time of two recipes, i.e., the operators `<=`, `>=` and `==`.
    
    -   The `<=` operator should return `True` if the `__time` attribute of the first object is smaller or equal to the second objects `__time`\-attribute. Similarly, the operator should return `False` if the `__time` attribute of the first object is greater than that of the second object.
    -   The `>=` operator should return `True` if the `__time` attribute of the first object is greater or equal to the second objects `__time`\-attribute. Similarly, the operator should return `False` if the `__time` attribute of the first object is smaller than that of the second object.
    -   The `==`\-operator should retrun `True` if the objects `__time`\-attrributes are exactly the same, otherwise it should return `False`.
    

Example of using the getter and setter methods:

```python
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
```

The program will output:

```python
Chicken
Name changed
New name: Delicious Chicken
Name changed
Name did not change, still: Delicious Chicken
Name can't be changed to other than string, so it's still: Delicious Chicken
Time cannot be changed
Ingredients cannot be changed
Instructions cannot be changed
```

Example of using comparison operators:

```python
r1 = Recipe("Chicken", ["Chicken", "Salt"], 15, "Fry the chicken in a pan. Add salt.")
r2 = Recipe("Caesar Salad", ["Lettuce", "Chicken", "Dressing"], 25, "Cook the chicken. Put the lettuce on a plate. Add chicken. Add dressing.")

print("r1 > r2:", r1 > r2)
print("r1 < r2:", r1 < r2)
```

The program will output:

```python
r1 > r2: False 
r1 < r2: True
```

## Exercise 2

Complete this in exercise template `exercise2.py`

You can use the Recipe class you programmed in the first exercise or the given Recipe class below. If you use your own Recipe class, copy the RecipeBook class template and your own Recipe class to the exercise template. Otherwise, copy both classes below into the exercise template.

```python
class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"

class RecipeBook:

    def __init__(self):
        self.__recipe_book = []
```

Write the following functionality for the RecipeBook class:

-   `__str__` method that returns the program's information as shown in the example below.
-   `add_recipe` method. The method adds the given Recipe object to the \_\_recipe\_book attribute. You can assume that no two recipes with the same name will be added.
-   `remove_recipe` method. The method removes the given **Recipe object** from the `__recipe_book` attribute. You can assume that only existing Recipe objects are attempted to be removed.
-   `recipe_by_name` method. The method takes a **string** as an argument. The method returns a **Recipe object** whose name matches the given string. If no matching recipe object is found, the method should return None.
-   `recipes_containing_ingredients` method. The method takes a list of strings as an argument. The method returns a list of **Recipe objects**, each of which contains all of the specified ingredients in its attributes. If no Recipe objects matching the criteria are found, the method should return an empty list. You can think of this method for example so that you have chicken and salad in your fridge and you are looking to use them and will buy the other required ingredients separately.
-   `recipes_within_time` method that takes an **integer** as an argument. The method returns a **list** of **Recipe objects** whose cooking time is at most equal to the given argument. If no recipe objects matching the criteria are found, the method should return an empty list.
-   `recipes_with_all_ingredients` method. The method takes a **list of strings** as an argument. The method returns a **list** of all **`Recipe` objects** whose ingredients are all found in the list given to the method. If no recipe objects matching the criteria are found, the method should return an empty list. You can think of this method for example so that the given ingredients are all available aleready and you will not buy additional ingredients.
-   `all_recipes` method. The method returns a list containing all the Recipe objects stored in the RecipeBook object. If the list returned by the method is modified, it does not affect the `RecipeBook` object.

Example of how to use the classes:

```python
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
```

Output of the program:

```python
RecipeBook:
Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the chicken in a frying pan. Add salt.')
Recipe(name='Caesar Salad', ingredients=['Lettuce', 'Chicken', 'Dressing'], time=25, instructions='Cook the chicken. Place lettuce on a plate. Add chicken. Add dressing.')
Recipe(name='Blueberry Muffins', ingredients=['Flour', 'Milk', 'Sugar', 'Blueberries'], time=30, instructions='Mix ingredients. Bake muffins at 180 degrees.')

Recipe with search 'Chicken': Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the chicken in a frying pan. Add salt.')
Recipe with search 'Risotto': None

Recipes that contain the ingredients 'Chicken', 'Dressing': [Recipe(name='Caesar Salad', ingredients=['Lettuce', 'Chicken', 'Dressing'], time=25, instructions='Cook the chicken. Place lettuce on a plate. Add chicken. Add dressing.')]

Recipes that can be made with ingredients 'Chicken', 'Salt', 'Dressing', and 'Lettuce': [Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the chicken in a frying pan. Add salt.'), Recipe(name='Caesar Salad', ingredients=['Lettuce', 'Chicken', 'Dressing'], time=25, instructions='Cook the chicken. Place lettuce on a plate. Add chicken. Add dressing.')]

[Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the chicken in a frying pan. Add salt.')]
Recipes whose only ingredient is water: []
Recipes that can be made in one minute: []

All known recipes:
[Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the chicken in a frying pan. Add salt.'), Recipe(name='Caesar Salad', ingredients=['Lettuce', 'Chicken', 'Dressing'], time=25, instructions='Cook the chicken. Place lettuce on a plate. Add chicken. Add dressing.'), Recipe(name='Blueberry Muffins', ingredients=['Flour', 'Milk', 'Sugar', 'Blueberries'], time=30, instructions='Mix ingredients. Bake muffins at 180 degrees.')]
```

## Exercise 3

Complete this in exercise template `exercise3.py`

In this exercise, a user interface and persistent storage for a recipe management program are programmed. You can use the classes you programmed in exercises 1 and 2 as helpers for solving this exercise.

The user interface should have the following functionality:

-   When the program starts, it should print "Recipe book program" and instructions for the user interface. See the example below.
-   The program asks the user to make a selection.
-   Selection 0: `Exit`. End the program execution.
-   Selection 1: `Add recipe.` The program asks the user for the recipe name, cooking time, ingredients, and instructions, and saves the information. If a recipe with the same name already exists, the program will not ask for additional information and the recipe is not saved. The program prints the information to the user as shown in the example below.
-   Selection 2: `Remove recipe`. The program asks the user for the name of the recipe and based on that, it deletes the recipe if it exists. The program prints the information about the event to the user. If the recipe to be deleted is found, the program prints "Removed recipe <recipe\_name>". Otherwise, the program prints "No recipe found with name <recipe\_name>".
-   Selection 3: `Search recipe by name`. The program asks the user for a name of a recipe and prints the recipe if found. If the recipe is not found, the program prints "No recipe found with name <searched\_name>". Otherwise, the program prints the details of the recipe according to the example below:
-   Selection 4: `Search recipe by ingredients`. The program asks the user for the ingredients that should be found in the recipe. The ingredients are entered separated by commas. The program prints a list of all the recipes that meet the criteria, as shown in the example below.
-   Selection 5: `Search recipe by preparation time`. The program asks the user for an integer, which is the maximum acceptable cooking time for a recipe. The program prints a list containing all the recipes with a cooking time equal to or less than the given time.
-   Selection 6: `Search recipe by available ingredients`. The program asks the user for the ingredients that can be used in a recipe. The ingredients are entered separated by commas. The program prints a list of all the recipes that meet the criteria, as shown in the example below.
-   Selection 7: `Return all recipes`. The program prints all the recipes as shown in the example below. If no recipes are found, the program prints "No recipes found".
-   Selection 8: `Clear memory`. The program removes all known recipes, including the recipes saved in the file.
-   For any other input, the program prints the instructions again.

Also implement a permanent storage for the program. The properties of the storage are the following:

-   Implement the storage in file named `recipes.txt`
-   If the file does not exist, the program will create it.
-   The program saves the data to the file every time a recipe is added or removed.
-   The storage format in the file should be as follows: `<recipe name>;<ingredient1>,<ingredient2>,<etc>;<cooking time>;<instructions>`

Example line of a saved recipe in the file:

```txt
Chicken;Chicken,Salt;15;Fry the chicken. Add salt.
```

Example of how the user interface works when adding and removing recipes:

```python
Recipe book program
Commands:
0 - Exit
1 - Add recipe
2 - Remove recipe
3 - Search recipe by name
4 - Search recipe by ingredients
5 - Search recipe by preparation time
6 - Search recipe by available ingredients
7 - Return all recipes
8 - Clear memory
Enter command: 1
Enter recipe name: Chicken
Enter recipe ingredients separated by comma: Chicken,Salt
Enter recipe cooktime (min): 15
Enter recipe instructions: Fry the chicken. Add salt.
Added recipe Chicken
Enter command: 1
Enter recipe name: Fish
Enter recipe ingredients separated by comma: Fish,Salt,Dill
Enter recipe cooktime (min): 35                                      
Enter recipe instructions: Add salt and dill to the fish. Fry the fish.
Added recipe Fish
Enter command: 1
Enter recipe name: Chicken
Recipe already exists
Enter command: 2
Enter name of recipe to remove: Fish
Removed recipe Fish
Enter command: 1
Enter recipe name: Blueberry muffins
Enter recipe ingredients separated by comma: Flour,Milk,Sugar,Blueberries
Enter recipe cooktime (min): 30
Enter recipe instructions: Mix the ingredients. Bake at 180 degrees.
Added recipe Blueberry muffins
Enter command: 7
Found recipes:
Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the chicken. Add salt.')
Recipe(name='Blueberry muffins', ingredients=['Flour', 'Milk', 'Sugar', 'Blueberries'], time=30, instructions='Mix the ingredients. Bake at 180 degrees.')
Enter command: 0
```

Example of recipe search when the program starts with chicken, fish, and blueberry muffin recipes already in memory:

```python
Recipe book program
Commands:
0 - exit
1 - add recipe
2 - remove recipe
3 - search recipe by name
4 - search recipe by ingredients
5 - search recipe by preparation time
6 - search recipe by available ingredients
7 - return all recipes
8 - clear memory
Enter command: 3  
Enter recipe name to search: Pizza
No recipe found with name Pizza
Enter command: 3
Enter recipe name to search: Blueberry muffins
Found recipe: Recipe(name='Blueberry muffins', ingredients=['Flour', 'Milk', 'Sugar', 'Blueberries'], time=30, instructions='Mix the ingredients. Bake at 180 degrees.')
Enter command: 4
Enter the ingredients of the recipe you're looking for, separated by commas: Salt
Found recipes with ingredients ['Salt']:
Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the fhicken. Add salt.')
Recipe(name='Fish', ingredients=['Fish', 'Salt', 'Dill'], time=35, instructions='Add salt and dill to the fish. Fry the fish.')
Enter command: 4
Enter the ingredients of the recipe you're looking for, separated by commas: Chicken,Salt
Found recipes with ingredients ['Chicken', 'Salt']:
Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the fhicken. Add salt.')
Enter command: 4
Enter the ingredients of the recipe you're looking for, separated by commas: Water
No recipe found with ingredients ['Water']
Enter command: 5
Enter the preparation time of the recipe you're looking for (min): 25
Found recipes with preparation time 25 min:
Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the fhicken. Add salt.')
Enter command: 5
Enter the preparation time of the recipe you're looking for (min): 5
No recipe found with preparation time 5 min
Enter command: 6
Enter the ingredients of the recipe you're looking for, separated by commas: Salt,Fish,Chicken,Dill,Blueberries
Found recipes with ingredients ['Salt', 'Fish', 'Chicken', 'Dill', 'Blueberries']:
Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the fhicken. Add salt.')
Recipe(name='Fish', ingredients=['Fish', 'Salt', 'Dill'], time=35, instructions='Add salt and dill to the fish. Fry the fish.')
Enter command: 7
Found recipes:
Recipe(name='Chicken', ingredients=['Chicken', 'Salt'], time=15, instructions='Fry the fhicken. Add salt.')
Recipe(name='Blueberry muffins', ingredients=['Flour', 'Milk', 'Sugar', 'Blueberries'], time=30, instructions='Mix the ingredients. Bake at 180 degrees.')
Recipe(name='Fish', ingredients=['Fish', 'Salt', 'Dill'], time=35, instructions='Add salt and dill to the fish. Fry the fish.')
Enter command: 0
```

And finally an example of how the program functions with undefined commands and clearing memory:

```python
Recipe book program
Commands:
0 - Exit
1 - Add recipe
2 - Remove recipe
3 - Search recipe by name
4 - Search recipe by ingredients
5 - Search recipe by preparation time
6 - Search recipe by available ingredients
7 - Return all recipes
8 - Clear memory
Enter command: 8
Memory cleared
Enter command: 7
No recipes found
Enter command: X
Commands:
0 - Exit
1 - Add recipe
2 - Remove recipe
3 - Search recipe by name
4 - Search recipe by ingredients
5 - Search recipe by preparation time
6 - Search recipe by available ingredients
7 - Return all recipes
8 - Clear memory
Enter command: GIVE ME A RECIPE
Commands:
0 - Exit
1 - Add recipe
2 - Remove recipe
3 - Search recipe by name
4 - Search recipe by ingredients
5 - Search recipe by preparation time
6 - Search recipe by available ingredients
7 - Return all recipes
8 - Clear memory
Enter command: 0
```