import pytest


def test_product_name(new_product):
    """
    Тестирование названия продукта.
    Проверяет, что название продукта не пустое, содержит только буквы и начинается с заглавной буквы.
    """
    assert new_product.name != ''
    assert new_product.name.isalpha()
    assert new_product.name.istitle()


def test_product_description(new_product):
    """
    Тестирование описания продукта.
    Проверяет, что описание продукта не пустое, содержит только буквы и не длиннее 500 символов.
    """
    assert new_product.description != ''
    assert len(new_product.description) <= 500


def test_product_positive_value(new_product):
    """
    Тестирование числового значения цены и кол-ва.
    Проверяет, что числовое значение положительное.
    """
    assert new_product.price >= 0
    assert new_product.quantity >= 0


def test_product_types(new_product):
    """
    Тестирование принадлежности товара к определенным категориям.
    Проверяет, что товар принадлежит одной из категорий (book, clothing, electronics).
    """
    assert isinstance(new_product.name, str)
    assert isinstance(new_product.description, str)
    assert isinstance(new_product.price, float)
    assert isinstance(new_product.quantity, int)


@pytest.mark.parametrize("price, expected_price", [
    (-100, 100),
    (0, 0),
    (100, 100)
])
def test_product_price_boundary(make_product, price, expected_price):
    """
    Проверка граничных значений стоимости.
    Проверяет, что стоимость товара является положительной или равной 0.
    """
    product = make_product(price=price)
    assert product.price == expected_price



