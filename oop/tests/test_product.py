import pytest


def test_product_name(new_product):
    """
    Тестирование названия продукта.
    Проверяет, что название продукта не пустое, содержит только буквы и начинается с заглавной буквы.
    """
    assert new_product.name != ''
    assert new_product.name.isalpha()
    assert new_product.name.istitle()



