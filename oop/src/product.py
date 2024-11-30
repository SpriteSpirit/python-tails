from oop.src.abc_base import AbstractProduct
from oop.src.mixin import PrintInfoMixin


class Product(AbstractProduct, PrintInfoMixin):
    """
    Класс товара.
    Attributes:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара
        quantity (int): Количество товара в наличии
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price)
        self.quantity = quantity if quantity > 0 else abs(quantity)
        self.__price = price  # Защищенное поле для цены

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):

        if not isinstance(other, Product):
            raise TypeError('Объекты должны быть экземплярами класса Product.')

        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        """
        Возвращает текущую цену товара.
        """

        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: Цена должна быть больше нуля.")
        elif new_price < self.__price:
            confirm = input(f"Цена товара '{self.name}' понижается. Подтвердить (y/n)? ")

            if confirm.lower() == 'y':
                self.__price = new_price
                print("Цена успешно обновлена.")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = new_price
            print("Цена успешно обновлена.")

    def get_info(self):
        return f"Продукт: {self.name}, Описание: {self.description}, Цена: {self.price}, Количество: {self.quantity}"

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list = None):
        """
        Создает товар и возвращает объект Product.
        Проверяет наличие такого же товара по имени в списке products.
        В случае совпадения имен, суммирует количество и выбирает максимальную цену.
        """

        if products:
            for product in products:
                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    print(f"Товар '{name}' уже существует. Количество и цена обновлены.")
                    return product

        return cls(name, description, price, quantity)
