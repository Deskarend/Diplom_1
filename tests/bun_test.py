import pytest

import data
from stellar_burgers.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', data.Buns)
    def test_create_bun(self, name, price):
        bun_name = name
        bun_price = price

        bun = Bun(bun_name, bun_price)

        assert bun.name == bun_name, (f"Ожидаемое название булочки при создании {bun_name}, "
                                      f"фактическое название булочки {bun.name}")
        assert bun.price == bun_price, (f"Ожидаемая цена булочки при создании {bun_price}, "
                                        f"фактическая цена булочки {bun.name}")

    @pytest.mark.parametrize('name, price', data.Buns)
    def test_bun_get_name(self, name, price):
        bun_name = name
        bun_price = price

        bun = Bun(bun_name, bun_price)

        assert bun.get_name() == bun_name

    @pytest.mark.parametrize('name, price', data.Buns)
    def test_bun_get_price(self, name, price):
        bun_name = name
        bun_price = price

        bun = Bun(bun_name, bun_price)

        assert bun.get_price() == bun.price
