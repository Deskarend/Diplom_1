import helper

from stellar_burgers.database import Database


class TestDatabase:

    def test_database_buns(self, list_buns_as_class_objects):
        expected_buns = list_buns_as_class_objects

        actual_buns = Database().buns

        helper.Equality.check_equal_two_list_object(expected_buns, actual_buns)

    def test_database_ingredients(self, list_ingredients_as_class_objects):
        expected_ingredients = list_ingredients_as_class_objects

        actual_ingredients = Database().ingredients

        helper.Equality.check_equal_two_list_object(expected_ingredients, actual_ingredients)

    def test_database_available_buns(self, list_buns_as_class_objects):
        expected_buns = list_buns_as_class_objects

        actual_buns = Database().available_buns()

        helper.Equality.check_equal_two_list_object(expected_buns, actual_buns)

    def test_database_available_ingredients(self, list_ingredients_as_class_objects):
        expected_ingredients = list_ingredients_as_class_objects

        actual_ingredients = Database().available_ingredients()

        helper.Equality.check_equal_two_list_object(expected_ingredients, actual_ingredients)
