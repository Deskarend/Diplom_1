from unittest.mock import Mock

import pytest



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
