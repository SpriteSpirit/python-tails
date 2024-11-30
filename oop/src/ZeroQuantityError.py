class ZeroQuantityError(Exception):
    """
    Класс исключения для обработки добавления товара с нулевым количеством.
    """
    def __init__(self, message="Нельзя добавлять товар с нулевым количеством."):
        self.message = message
        super().__init__(self.message)
