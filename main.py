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


if __name__ == '__main__':
    main()
