from oop.src.product import Product
from typing import List


class Category:
    """
    Класс категории товара.
    Attributes:
        name (str): Название товара
        description (str): Описание товара
        goods (list): Список товаров
    """
    name: str
    description: str
    goods: List[Product]
    unique_products: set = set()
    total_categories: int = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.goods = []
        self.total_categories += 1

        for good in self.goods:
            self.unique_products.add(good)
