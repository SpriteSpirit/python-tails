from product import Product


class Smartphone(Product):
    """
    Класс смартфона.
    """
    name: str
    description: str
    price: float
    quantity: int
    performance: str
    model: str

    def __init__(self, name: str, description: str, price: float, quantity: int, performance: str, model: str,
                 memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{super().__str__()} | Производительность: {self.performance}, Модель: {self.model}, "
                f"Память: {self.memory}, Цвет: {self.color}")
