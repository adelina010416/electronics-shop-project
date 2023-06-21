import pytest
from src.item import Item


@pytest.fixture
def laptop():
    return Item('Laptop', 50000, 3)


def test_calculate_total_price(laptop):
    assert laptop.calculate_total_price() == 150000


def test_apply_discount(laptop):
    Item.pay_rate = 0.8
    laptop.apply_discount()
    assert laptop.price == 40000
