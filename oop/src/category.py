from oop.src.product import Product
from typing import List, Set


class Category:
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

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__products = goods if goods is not None else []
        self.unique_products = set(self.products)
        Category.total_categories += 1

    def add_product(self, product: object):
        """
        Добавление нового товара в категорию
        """
        self.__products.append(product)

    @property
    def products(self):
        """
        Список товаров
        """
        return [f'{product}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products]
