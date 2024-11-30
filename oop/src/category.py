from oop.src.mixin import PrintInfoMixin
from oop.src.order import AbstractOrder
from oop.src.product import Product
from typing import List, Set


class Category(AbstractOrder, PrintInfoMixin):
    """
    Класс категории товара.
    Attributes:
        name (str): Название товара
        description (str): Описание товара
        products (list): Список товаров
        unique_products(Set[Product]): Уникальные товары
        total_categories(int): Общее кол-во категорий)
    """
    name: str
    description: str
    products: List[Product]
    unique_products: Set[Product]
    total_categories: int = 0

    def __init__(self, name: str, description: str, products: list):
        super().__init__(name, description)
        self.__products = products if products is not None else []
        self.unique_products = set(products)
        Category.total_categories += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

    def get_info(self):
        """
        Выводит информацию о категории
        """
        return f"Категория: {self.name}, Описание: {self.description}, Количество продуктов: {len(self.products)}"

    def add_product(self, product: object):
        """
        Добавление нового товара в категорию
        """
        if isinstance(product, Product) or issubclass(type(product), Product):
            self.__products.append(product)
        else:
            raise TypeError("В категорию можно добавлять только товары или их подклассы.")

    @property
    def products(self):
        """
        Список товаров
        """
        return [f'{product}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products]
