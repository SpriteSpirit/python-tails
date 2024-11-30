import pytest

from oop.src.category import Category
from oop.src.product import Product


def test_category_total_categories(new_category):
    """
    Тестирование счетчика категорий.
    Проверяет, что счетчик категорий увеличивается при создании новой категории.
    """
    assert new_category.total_categories == 1
    new_category_2 = Category('Test Category 2', 'Description for Test Category 2', [])
    assert new_category.total_categories == 2
    assert new_category_2.total_categories == 2


def test_category_name(new_category):
    """
    Тестирование названия категории.
    Проверяет, что название категории не пустое и начинается с заглавной буквы.
    """
    assert new_category.name != ''
    assert new_category.name.istitle()


def test_category_description(new_category):
    """
    Тестирование описания категории.
    Проверяет, что описание категории не пустое и не длиннее 500 символов.
    """
    assert new_category.description != ''
    assert len(new_category.description) <= 500


def test_category_product_list(new_category):
    """
    Тестирование списка товаров
    Проверяет, что первый элемент списка является объектом класса Product
    """
    assert new_category.__products is not None
    assert isinstance(new_category.goods[0], Product)


def test_category_types(new_category):
    """
    Тестирование принадлежности атрибутов категории к определенным типам данных.
    """
    assert isinstance(new_category.name, str)
    assert isinstance(new_category.description, str)
    assert isinstance(new_category.unique_products, set)
    assert isinstance(new_category.total_categories, int)


# def test_category_unique_products(new_category):
#     """
#     Тестирование уникальности товаров в категории.
#     Проверяет, что товары уникальны и два множества равны
#     """
#
#     assert set(new_category.__products) == new_category.unique_products
#

def test_add_product_invalid_type(new_category):

    with pytest.raises(TypeError):
        new_category.add_product("Not a product")


def test_add_product_invalid_subclass(new_category):
    class AnotherProduct:
        pass

    with pytest.raises(TypeError):
        new_category.add_product(AnotherProduct())
