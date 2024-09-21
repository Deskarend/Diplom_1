import data

from stellar_burgers.database import Database


def check_equal_two_list_object(first_list, second_list):
    for i in range(len(first_list)):
        assert first_list[i].__dict__ == second_list[i].__dict__, \
            f'Ожидаемый объект {first_list[i].__dict__}, фактический {second_list[i].__dict__}'


class TestDatabase:

    def test_database_buns(self):
        expected_buns = data.get_buns_as_list_objects()

        actual_buns = Database().buns

        check_equal_two_list_object(expected_buns, actual_buns)

    def test_database_ingredients(self):
        expected_ingredients = data.get_ingredients_as_list_objects()

        actual_ingredients = Database().ingredients

        check_equal_two_list_object(expected_ingredients, actual_ingredients)

    def test_database_available_buns(self):
        expected_buns = data.get_buns_as_list_objects()

        actual_buns = Database().available_buns()

        check_equal_two_list_object(expected_buns, actual_buns)

    def test_database_available_ingredients(self):
        expected_ingredients = data.get_ingredients_as_list_objects()

        actual_ingredients = Database().available_ingredients()

        check_equal_two_list_object(expected_ingredients, actual_ingredients)
