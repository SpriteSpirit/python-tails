from oop.src.abc_base import AbstractOrder


class Order(AbstractOrder):
    """
    Класс заказа
    """
    def __init__(self, name, description, product, quantity):
        super().__init__(name, description)
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def get_info(self):
        return f"Заказ: {self.name}, Описание: {self.description}, Продукт: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price}"
