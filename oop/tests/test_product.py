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



