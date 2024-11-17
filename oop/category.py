from product import Product
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

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.goods = []
