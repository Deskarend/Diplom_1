from unittest.mock import Mock

from stellar_burgers.bun import Bun
from stellar_burgers.ingredient import Ingredient


class IngredientHelper:
    @staticmethod
    def get_mock_ingredient(ingredient):
        mock_ingredient = Mock()

        mock_ingredient.type = ingredient[0]
        mock_ingredient.name = ingredient[1]
        mock_ingredient.price = ingredient[2]

        mock_ingredient.get_type.return_value = ingredient[0]
        mock_ingredient.get_name.return_value = ingredient[1]
        mock_ingredient.get_price.return_value = ingredient[2]

        return mock_ingredient

    @staticmethod
    def get_list_mock_ingredients(ingredients):
        list_mock_ingredients = []

        for ingredient in ingredients:
            list_mock_ingredients.append(IngredientHelper.get_mock_ingredient(ingredient))

        return list_mock_ingredients

    @staticmethod
    def get_list_ingredients_as_class_objects(ingredients):
        list_ingredients = []
        for ingredient in ingredients:
            list_ingredients.append(Ingredient(*ingredient))
        return list_ingredients


class BunHelper:
    @staticmethod
    def get_list_buns_as_class_objects(buns):
        list_buns = []
        for bun in buns:
            list_buns.append(Bun(*bun))
        return list_buns


class Equality:
    @staticmethod
    def check_equal_two_list_object(first_list, second_list):
        for i in range(len(first_list)):
            assert first_list[i].__dict__ == second_list[i].__dict__, \
                f'Ожидаемый объект {first_list[i].__dict__}, фактический {second_list[i].__dict__}'
