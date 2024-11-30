from oop.src.ZeroQuantityError import ZeroQuantityError
from oop.src.category_iteration import CategoryIteration
from oop.src.order import Order
from oop.src.product import Product
from oop.src.category import Category


def main():
    product1 = Product('Телефон', 'Описание телефона', 20_000, 5)
    product2 = Product('Камера', 'Описание камеры', 10_000, 2)
    product3 = Product('Приставка', 'Описание приставки', 50_000, 3)

    category1 = Category('Электроника', 'Электронные товары', [])

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(product1)
    print(category1)
    print(product1 + product2)

    product_list = CategoryIteration(category1)

    for product in product_list:
        print(product)

    category = Category("Категория 1", "Описание категории", [])
    print(category)

    product1 = Product("Телефон", "Смартфон", 1000.0, 5)
    product2 = Product("Наушники", "Беспроводные", 100.0, 0)  # Продукт с нулевым количеством

    category1 = Category("Электроника", "Различные электронные устройства", [])

    category1.add_product(product1)  # Выведет сообщение об успешном добавлении и завершении обработки
    category1.add_product(product2)  # Выведет сообщение об ошибке ZeroQuantityError и завершении обработки

    product1 = Product("Телефон", "Смартфон", 1000.0, 5)
    try:
        order1 = Order("Заказ 1", "Первый заказ", product1,
                       2)  # Выведет сообщение об успешном добавлении и завершении обработки
        order2 = Order("Заказ 2", "Второй заказ", product1,
                       0)  # Выведет сообщение об ошибке ZeroQuantityError и завершении обработки
    except ZeroQuantityError as e:
        print(f"Глобальная обработка ошибки заказа: {e}")
        print("Обработка заказов завершена")


if __name__ == '__main__':
    main()
