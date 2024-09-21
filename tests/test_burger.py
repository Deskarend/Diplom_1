import random
from unittest.mock import Mock

import pytest

import data
from stellar_burgers.burger import Burger


class TestBurger:
    def test_default_bun_and_ingredient_values_burger(self):
        burger = Burger()

        assert burger.bun is None, (f"Ожидаемое значение булочки нового(пустого) бургера {None}, "
                                    f"фактическое {burger.bun}")
        assert burger.ingredients == [], (f"Ожидаемое значение ингредиентов нового(пустого) бургера {[]}, "
                                          f"фактическое {burger.ingredients}")

    @pytest.mark.parametrize('name, price', data.buns)
    def test_burger_set_buns(self, name, price):
        mock_bun = Mock()
        mock_bun.name = name
        mock_bun.price = price

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun, f"Ожидаемая булочка {mock_bun}, фактическая {burger.bun}"

    @pytest.mark.parametrize('type, name, price', data.ingredients)
    def test_burger_add_ingredient(self, type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.type = type
        mock_ingredient.name = name
        mock_ingredient.price = price

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient], (f"Ожидаемые ингредиенты {[mock_ingredient]}, "
                                                         f"фактические {burger.ingredients}")

    def test_burger_add_some_ingredients(self):
        ingredients = []
        burger = Burger()
        for ingredient in data.ingredients:
            mock_ingredient = Mock()
            mock_ingredient.type = ingredient[0]
            mock_ingredient.name = ingredient[1]
            mock_ingredient.price = ingredient[2]

            ingredients.append(mock_ingredient)
            burger.add_ingredient(mock_ingredient)

            assert burger.ingredients[-1] == mock_ingredient, (f"Ожидаемый добавленный ингредиент {mock_ingredient}, "
                                                               f"фактический {burger.ingredients[-1]}")
            assert burger.ingredients == ingredients, (f"Ожидаемые ингредиенты {ingredients}, "
                                                       f"фактические {burger.ingredients}")

    def test_burger_remove_ingredient(self):
        mock_ingredients = data.get_mock_ingredient()

        burger = Burger()
        burger.ingredients = mock_ingredients.copy()

        for _ in burger.ingredients:
            random_ind = random.randrange(len(burger.ingredients))
            burger.remove_ingredient(random_ind)
            del mock_ingredients[random_ind]

            assert burger.ingredients == mock_ingredients, (f"Ожидаемые ингредиенты после удаления {mock_ingredients},"
                                                            f"фактические {burger.ingredients}")

    def test_burger_move_ingredient(self):
        mock_ingredients = data.get_mock_ingredient()

        burger = Burger()
        burger.ingredients = mock_ingredients.copy()

        for _ in burger.ingredients:
            index = random.randrange(len(burger.ingredients))
            new_index = random.randrange(len(burger.ingredients))
            new_index = random.randrange(len(burger.ingredients)) if index == new_index else new_index

            burger.move_ingredient(index, new_index)
            mock_ingredients.insert(new_index, mock_ingredients.pop(index))

            assert burger.ingredients == mock_ingredients, (
                f"Ожидаемые ингредиенты после перемешивания {mock_ingredients},"
                f"фактические {burger.ingredients}")

    @pytest.mark.parametrize('bun', data.buns)
    def test_burger_get_price(self, bun):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun[1]
        mock_ingredients = data.get_mock_ingredient()

        total_price = bun[1] * 2
        for ingredient in mock_ingredients:
            total_price += ingredient.price

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = mock_ingredients

        assert burger.get_price() == total_price, (f"Ожидаемая цена бургера {total_price}, "
                                                   f"фактическая {burger.get_price()}")

    @pytest.mark.parametrize('name, price', data.buns)
    def test_burger_get_receipt(self, name, price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price
        mock_ingredients = data.get_mock_ingredient()

        total_price = price * 2
        for ingredient in mock_ingredients:
            total_price += ingredient.price

        receipt = [f'(==== {mock_bun.get_name()} ====)']
        for ingredient in mock_ingredients:
            receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')
        receipt.append(f'(==== {mock_bun.get_name()} ====)\n')
        receipt.append(f'Price: {total_price}')
        receipt = '\n'.join(receipt)

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = mock_ingredients

        assert burger.get_receipt() == receipt, (f'Ожидаемый рецепт бургера {receipt},'
                                                 f'фактический {burger.get_receipt()}')
