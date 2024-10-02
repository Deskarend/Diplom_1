import random

import pytest

import data
import helper
from stellar_burgers.burger import Burger


class TestBurger:
    def test_burger_default_bun_and_ingredient_values(self):
        burger = Burger()

        assert burger.bun is None, (f"Ожидаемое значение булочки пустого бургера - {None}, "
                                    f"фактическое - {burger.bun}")
        assert burger.ingredients == [], (f"Ожидаемое значение ингредиентов пустого бургера - {[]}, "
                                          f"фактическое - {burger.ingredients}")

    @pytest.mark.parametrize('mock_bun', data.buns, indirect=True)
    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun, f"Ожидаемая булочка {mock_bun}, фактическая {burger.bun}"

    @pytest.mark.parametrize('mock_ingredient', data.ingredients, indirect=True)
    def test_burger_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient], (f"Ожидаемые ингредиенты {[mock_ingredient]}, "
                                                         f"фактические {burger.ingredients}")

    def test_burger_add_some_ingredients(self):
        ingredients = []
        burger = Burger()

        for ingredient in data.ingredients:
            new_mock_ingredient = helper.IngredientHelper.get_mock_ingredient(ingredient)

            ingredients.append(new_mock_ingredient)
            burger.add_ingredient(new_mock_ingredient)

            assert burger.ingredients[-1] == new_mock_ingredient, \
                (f"Ожидаемый добавленный ингредиент {new_mock_ingredient}, "
                 f"фактический {burger.ingredients[-1]}")
            assert burger.ingredients == ingredients, (f"Ожидаемые ингредиенты {ingredients}, "
                                                       f"фактические {burger.ingredients}")

    def test_burger_remove_ingredient(self, list_mock_ingredients):
        burger = Burger()
        burger.ingredients = list_mock_ingredients.copy()

        for _ in burger.ingredients:
            random_ind = random.randrange(len(burger.ingredients))
            burger.remove_ingredient(random_ind)
            del list_mock_ingredients[random_ind]

            assert burger.ingredients == list_mock_ingredients, \
                (f"Ожидаемые ингредиенты после удаления {list_mock_ingredients},"
                 f"фактические {burger.ingredients}")

    def test_burger_move_ingredient(self, list_mock_ingredients):
        burger = Burger()
        burger.ingredients = list_mock_ingredients.copy()

        for _ in burger.ingredients:
            index = random.randrange(len(burger.ingredients))
            new_index = random.randrange(len(burger.ingredients))
            new_index = random.randrange(len(burger.ingredients)) if index == new_index else new_index

            burger.move_ingredient(index, new_index)
            list_mock_ingredients.insert(new_index, list_mock_ingredients.pop(index))

            assert burger.ingredients == list_mock_ingredients, (
                f"Ожидаемые ингредиенты после перемешивания {list_mock_ingredients},"
                f"фактические {burger.ingredients}")

    @pytest.mark.parametrize('mock_bun', data.buns, indirect=True)
    def test_burger_get_price(self, mock_bun, list_mock_ingredients):
        total_price = mock_bun.price * 2
        for ingredient in list_mock_ingredients:
            total_price += ingredient.price

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = list_mock_ingredients

        assert burger.get_price() == total_price, (f"Ожидаемая цена бургера {total_price}, "
                                                   f"фактическая {burger.get_price()}")

    @pytest.mark.parametrize('mock_bun', data.buns, indirect=True)
    def test_burger_get_receipt(self, mock_bun, list_mock_ingredients):
        total_price = mock_bun.price * 2
        for ingredient in list_mock_ingredients:
            total_price += ingredient.price

        receipt = [f'(==== {mock_bun.get_name()} ====)']
        for ingredient in list_mock_ingredients:
            receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')
        receipt.append(f'(==== {mock_bun.get_name()} ====)\n')
        receipt.append(f'Price: {total_price}')
        receipt = '\n'.join(receipt)

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = list_mock_ingredients

        assert burger.get_receipt() == receipt, (f'Ожидаемый рецепт бургера {receipt},'
                                                 f'фактический {burger.get_receipt()}')
