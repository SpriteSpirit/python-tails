from typing import Iterator

from oop.src.category import Category
from oop.src.product import Product


class CategoryIteration:
    """
    Класс для итерации по категориям
    """
    category: Category

    def __init__(self, category: "Category"):
        self._index = 0
        self._category = category

    def __iter__(self) -> Iterator[Product]:
        return self

    def __next__(self) -> Product:
        if self._index < len(self._category.products):
            product = self._category.products[self._index]
            self._index += 1
            return product
        raise StopIteration
