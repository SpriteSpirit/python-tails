from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """
    Абстрактный класс товара.
    """

    name: str
    description: str
    price: float

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self._price = price

    @abstractmethod
    def get_info(self):
        pass


class AbstractOrder(ABC):
    """
    Абстрактный класс заказа.
    """

    name: str
    description: str

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def get_info(self):
        pass
