import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, encoding="utf-8") as file:
            menu_data_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = menu_data_reader

        for dish_name, dish_price, ingredient_name, recipe_amount in data:
            new_dish = Dish(dish_name, float(dish_price))
            ingredient = Ingredient(ingredient_name)

            for dish in self.dishes:
                if dish.name == dish_name:
                    dish.add_ingredient_dependency(
                        ingredient, int(recipe_amount)
                    )
            else:
                new_dish.add_ingredient_dependency(
                    ingredient, int(recipe_amount)
                )
            self.dishes.add(new_dish)

    def get_dishes(self):
        return self.dishes


# menu_data = MenuData("tests/mocks/menu_base_data.csv")
# print(menu_data.get_dishes())
