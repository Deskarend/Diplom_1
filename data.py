from unittest.mock import Mock
from stellar_burgers.bun import Bun
from stellar_burgers.ingredient import Ingredient

buns = [
    ["black bun", 100],
    ["white bun", 200],
    ["red bun", 300]
]


def get_buns_as_list_objects():
    list_buns = []
    for bun in buns:
        list_buns.append(Bun(*bun))
    return list_buns


sauce_type = 'SAUCE'
filling_type = 'FILLING'

ingredients = [
    [sauce_type, "hot sauce", 100],
    [sauce_type, "sour cream", 200],
    [sauce_type, "chili sauce", 300],
    [filling_type, "cutlet", 100],
    [filling_type, "dinosaur", 200],
    [filling_type, "sausage", 300]
]


def get_ingredients_as_list_objects():
    list_ingredients = []
    for ingredient in ingredients:
        list_ingredients.append(Ingredient(*ingredient))
    return list_ingredients


def get_mock_ingredient():
    mock_ingredients = []
    for ingredient in ingredients:
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient[0]
        mock_ingredient.name = ingredient[1]
        mock_ingredient.price = ingredient[2]

        mock_ingredient.get_type.return_value = ingredient[0]
        mock_ingredient.get_name.return_value = ingredient[1]
        mock_ingredient.get_price.return_value = ingredient[2]

        mock_ingredients.append(mock_ingredient)

    return mock_ingredients
