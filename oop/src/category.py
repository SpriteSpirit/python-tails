from oop.src.product import Product
from typing import List, Set


class Category:
    """
    Класс категории товара.
    Attributes:
        name (str): Название товара
        description (str): Описание товара
        goods (list): Список товаров
        unique_products(Set[Product]): Уникальные товары
        total_categories(int): Общее кол-во категорий)
    """
    name: str
    description: str
    goods: List[Product]
    unique_products: Set[Product]
    total_categories: int = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods if goods is not None else []
        self.unique_products = set(self.goods)
        Category.total_categories += 1
