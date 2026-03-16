def check_ingredient_match(recipe, inventory):
    missing_ingredients = []
    percentage = 0.00
    for ingredient in recipe:
        if not ingredient in inventory:
            missing_ingredients.append(ingredient)
    percentage = 100 - (len(missing_ingredients) / len(recipe)) * 100

    return percentage, missing_ingredients
