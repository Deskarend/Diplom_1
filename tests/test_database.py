import data

from stellar_burgers.database import Database


class TestDatabase:
    def test_database_buns(self):
        expected_buns = data.get_buns_as_list_objects()

        actual_buns = Database().buns

        for i in range(len(actual_buns)):
            assert actual_buns[i].__dict__ == expected_buns[i].__dict__, \
                f'Ожидаемая булочка {expected_buns[i].__dict__}, фактическая булочка {actual_buns[i].__dict__}'

    def test_database_ingredients(self):
        expected_ingredients = data.get_ingredients_as_list_objects()

        actual_ingredients = Database().ingredients

        for i in range(len(actual_ingredients)):
            assert actual_ingredients[i].__dict__ == expected_ingredients[i].__dict__, \
                f'Ожидаемая булочка {expected_ingredients[i].__dict__}, фактическая булочка {actual_ingredients[i].__dict__}'

    def test_database_available_buns(self):
        expected_buns = data.get_buns_as_list_objects()

        actual_buns = Database().available_buns()

        for i in range(len(actual_buns)):
            assert actual_buns[i].__dict__ == expected_buns[i].__dict__, \
                f'Ожидаемая булочка {expected_buns[i].__dict__}, фактическая булочка {actual_buns[i].__dict__}'

    def test_database_available_ingredients(self):
        expected_ingredients = data.get_ingredients_as_list_objects()

        actual_ingredients = Database().available_ingredients()

        for i in range(len(actual_ingredients)):
            assert actual_ingredients[i].__dict__ == expected_ingredients[i].__dict__, \
                f'Ожидаемая булочка {expected_ingredients[i].__dict__}, фактическая булочка {actual_ingredients[i].__dict__}'
