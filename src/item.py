import csv


class InstantiateCSVError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, comment=''):
        self.message = 'Файл item.csv поврежден' + comment

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """
        Складывает количество товара в магазине
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[:10]
        self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        try:
            with open('../src/items.csv', 'r', encoding='windows-1251') as file:
                file_reader = csv.reader(file, delimiter=",")
                count = 0
                for line in file_reader:
                    count += 1
                    if count <= 1:
                        continue
                    if len(line) < 3 or not line[1].isdigit() or not line[2].isdigit():
                        raise InstantiateCSVError(f', ошибка в строке {count}')
                    name = line[0]
                    try:
                        price = float(line[1])
                        quantity = int(line[2])
                    except ValueError as e:
                        break
                    Item(name, price, quantity)
        except FileNotFoundError:
            print("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(string: str):
        """
        Возвращает число из числа-строки.
        """
        try:
            for i in string:
                if not i.isdigit():
                    string = string[:string.find(i)]
            return int(string)
        except ValueError:
            return "Недопустимый ввод"
