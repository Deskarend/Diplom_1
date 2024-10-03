import pytest

import data
from stellar_burgers.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('type, name, price', data.ingredients)
    def test_create_ingredient(self, type, name, price):
        ingredient_type = type
        ingredient_name = name
        ingredient_price = price

        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        assert ingredient.type == ingredient_type, (f"Ожидаемый тип ингредиента  {ingredient_type}, "
                                                    f"фактический тип ингредиента {ingredient.name}")
        assert ingredient.name == ingredient_name, (f"Ожидаемое название ингредиента {ingredient_name}, "
                                                    f"фактическое название ингредиента {ingredient.name}")
        assert ingredient.price == ingredient_price, (f"Ожидаемая цена ингредиента {ingredient_price}, "
                                                      f"фактическая цена ингредиента {ingredient.name}")

    @pytest.mark.parametrize('type', data.ingredient_types)
    def test_get_type(self, type):
        ingredient_type = type
        ingredient_name = 'hot sauce'
        ingredient_price = 100

        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        assert ingredient.get_type() == ingredient_type, (f"Ожидаемый тип ингредиента  {ingredient_type}, "
                                                          f"фактический тип ингредиента {ingredient.get_type()}")

    @pytest.mark.parametrize('name', data.ingredient_names)
    def test_get_name(self, name):
        ingredient_type = 'SAUCE'
        ingredient_name = name
        ingredient_price = 100

        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        assert ingredient.get_name() == ingredient_name, (f"Ожидаемое название ингредиента {ingredient_name}, "
                                                          f"фактическое название ингредиента {ingredient.get_name()}")

    @pytest.mark.parametrize('price', data.ingredient_prices)
    def test_get_price(self, price):
        ingredient_type = "SAUCE"
        ingredient_name = "dinosaur"
        ingredient_price = price

        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        assert ingredient.get_price() == ingredient_price, (f"Ожидаемая цена ингредиента {ingredient_price}, "
                                                            f"фактическая цена ингредиента {ingredient.get_price()}")
