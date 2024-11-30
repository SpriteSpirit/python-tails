from oop.src.product import Product


class Grass(Product):
    """
    Класс травы.
    """
    country: str
    germination_period: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"{super().__str__()} | Страна-производитель: {self.country}, "
                f"Срок прорастания : {self.germination_period}, Цвет: {self.color}")
