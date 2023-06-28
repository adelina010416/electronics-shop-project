import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def laptop():
    return Item('Laptop', 50000, 3)


def test_repr(laptop):
    assert repr(laptop) == "Item('Laptop', 50000, 3)"


def test_str(laptop):
    assert str(laptop) == 'Laptop'


def test_calculate_total_price(laptop):
    assert laptop.calculate_total_price() == 150000


def test_apply_discount(laptop):
    Item.pay_rate = 0.8
    laptop.apply_discount()
    assert laptop.price == 40000


def test_name(laptop):
    assert laptop.name == 'Laptop'
    laptop.name = 'Computer'
    assert laptop.name == 'Computer'
    laptop.name = 'СуперСмартфон'
    assert laptop.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 10
    assert Item.all[0].name == 'Laptop'


@pytest.mark.parametrize('nums', [('5', 5), ('5.0', 5), ('5.5', 5)])
def test_string_to_number(nums):
    assert Item.string_to_number(nums[0]) == nums[1]
    assert Item.string_to_number('a') == "Недопустимый ввод"


def test_add(laptop):
    table = Item('table', 15000.0, 3)
    phone = Phone('POCO M5', 15000.0, 4, 2)
    assert laptop + table == 6
    assert laptop + phone == 7
    with pytest.raises(ValueError):
        print(laptop + 30)
