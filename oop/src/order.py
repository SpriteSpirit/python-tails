from oop.src.ZeroQuantityError import ZeroQuantityError
from oop.src.abc_base import AbstractOrder


class Order(AbstractOrder):
    """
    Класс заказа
    """
    def __init__(self, name, description, product, quantity):
        super().__init__(name, description)
        try:
            if quantity == 0:
                raise ZeroQuantityError()
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity
            print("Товар успешно добавлен в заказ.")
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка добавления товара в заказ завершена.")

    def get_info(self):
        return f"Заказ: {self.name}, Описание: {self.description}, Продукт: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price}"
