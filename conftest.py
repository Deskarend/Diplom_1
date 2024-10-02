from unittest.mock import Mock

import pytest

import data
import helper


@pytest.fixture
def mock_bun(request):
    mock_bun = Mock()

    mock_bun.name = request.param[0]
    mock_bun.price = request.param[1]

    mock_bun.get_name.return_value = request.param[0]
    mock_bun.get_price.return_value = request.param[1]

    return mock_bun


@pytest.fixture
def mock_ingredient(request):
    mock_ingredient = Mock()

    mock_ingredient.type = request.param[0]
    mock_ingredient.name = request.param[1]
    mock_ingredient.price = request.param[2]

    return mock_ingredient


@pytest.fixture
def list_mock_ingredients():
    return helper.IngredientHelper.get_list_mock_ingredients(data.ingredients)


@pytest.fixture()
def list_ingredients_as_class_objects():
    return helper.IngredientHelper.get_list_ingredients_as_class_objects(data.ingredients)


@pytest.fixture()
def list_buns_as_class_objects():
    return helper.BunHelper.get_list_buns_as_class_objects(data.buns)
