import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone('POCO M5', 15000.0, 3, 2)


def test_init():
    with pytest.raises(ValueError):
        phone2 = Phone('POCO M5', 15000.0, 3, 0)


def test_repr(phone):
    assert repr(phone) == "Phone('POCO M5', 15000.0, 3, 2)"


def test_sim(phone):
    assert phone.number_of_sim == 2
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_add(phone):
    table = Item('table', 15000.0, 3)
    phone1 = Phone('POCO M4', 10000.0, 2, 1)
    assert phone1 + phone == 5
    assert table + phone == 6
    with pytest.raises(ValueError):
        print(phone + 30)
