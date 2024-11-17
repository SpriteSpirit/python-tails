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



