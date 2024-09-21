from stellar_burgers.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredientTypes:
    def test_sauce_type(self):
        expected_ingredient_type_sauce = "SAUCE"
        actual_ingredient_type_sauce = INGREDIENT_TYPE_SAUCE
        assert actual_ingredient_type_sauce == expected_ingredient_type_sauce, \
            f'Ожидаемый тип добавки {expected_ingredient_type_sauce}, фактический {actual_ingredient_type_sauce}'

    def test_filling_type(self):
        expected_ingredient_type_filling = "FILLING"
        actual_ingredient_type_filling = INGREDIENT_TYPE_FILLING
        assert actual_ingredient_type_filling == expected_ingredient_type_filling, \
            f'Ожидаемый тип добавки {expected_ingredient_type_filling}, фактический {actual_ingredient_type_filling}'
