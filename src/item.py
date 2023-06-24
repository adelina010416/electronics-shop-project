import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

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
        with open('../src/items.csv', 'r', encoding='windows-1251') as file:
            file_reader = csv.reader(file, delimiter=",")
            count = 0
            for line in file_reader:
                count += 1
                if count <= 1:
                    continue
                name = line[0]
                try:
                    price = float(line[1])
                    quantity = int(line[2])
                except ValueError as e:
                    print(e)
                Item(name, price, quantity)

    @staticmethod
    def string_to_number(string: str):
        try:
            for i in string:
                if not i.isdigit():
                    string = string[:string.find(i)]
            return int(string)
        except ValueError:
            return "Недопустимый ввод"
