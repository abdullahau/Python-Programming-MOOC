# Write your solution here
def openfile(filename: str):
    with open(filename) as new_file:
        prep_time = {}
        recipe = {}
        ingredients = []
        recipe_name = ""
        counter = 0
        for line in new_file:
            line = line.strip()
            if line.isnumeric():
                prep_time[recipe_name] = int(line)
                counter = 1
            elif counter == 1:
                if line == '':
                    recipe[recipe_name] = ingredients
                    ingredients = []
                    counter = 0
                    continue
                ingredients.append(line)
            else:
                recipe_name = line
                counter = 0 
        recipe[recipe_name] = ingredients
        return prep_time , recipe

def search_by_name(filename: str, word: str):
    prep_time, recipe = openfile(filename)
    recipe_list = []
    for recipe_name, ingredients in recipe.items():
        if word.lower() in recipe_name.lower():
            recipe_list.append(recipe_name)
    return recipe_list

def search_by_time(filename: str, prep_duration: int):
    prep_time, recipe = openfile(filename)
    recipe_list = []
    for recipe_name, duration in prep_time.items():
        if duration <= prep_duration:
            recipe_list.append(f"{recipe_name}, preparation time {duration} min")
    return recipe_list

def search_by_ingredient(filename: str, ingredient: str):
    prep_time, recipe = openfile(filename)
    recipe_list = []
    for recipe_name, ingredients in recipe.items():
        if ingredient in ingredients:
            recipe_list.append(f"{recipe_name}, preparation time {prep_time[recipe_name]} min")
    return recipe_list
        
            
if __name__ == "__main__":
    if True:
        search_by_name("recipes1.txt", "milk")
    else:
        search_by_time("recipes1.txt", 30)
        search_by_ingredient("recipes1.txt", "eggs")