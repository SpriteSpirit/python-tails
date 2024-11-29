class Product:
    """
    Класс товара.
    Attributes:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара
        quantity (int): Количество товара в наличии
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price if price > 0 else abs(price)
        self.quantity = quantity if quantity > 0 else abs(quantity)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list = None):
        """
        Создает товар и возвращает объект Product.
        Проверяет наличие такого же товара по имени в списке products.
        В случае совпадения имен, суммирует количество и выбирает максимальную цену.
        """

        if products:
            for product in products:
                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    print(f"Товар '{name}' уже существует. Количество и цена обновлены.")
                    return product

        return cls(name, description, price, quantity)
