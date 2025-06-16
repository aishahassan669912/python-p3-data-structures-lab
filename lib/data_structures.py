spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# 1. Return a list of names of all the spicy foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. Return a list of foods with heat_level > 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. Print each food in the format: Name (Cuisine) | Heat Level: 🌶 * heat_level
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')

# 4. Return the first food that matches the given cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None

# 5. Print only the spiciest foods using the same format as print_spicy_foods
def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

# 6. Return the average heat level as an integer
def get_average_heat_level(spicy_foods):
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

# 7. Return a new list with the new food added
def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
