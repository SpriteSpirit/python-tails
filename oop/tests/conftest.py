import pytest

from oop.src.product import Product
from oop.src.category import Category


@pytest.fixture(params=[
    ('Ноутбук', 'Последней модели', 70_000.00, 5),
    ('Смартфон', 'С камерой 100MP', 50_000.00, 10),
    ('Планшет', 'Для рисования', 30_000.00, 0)
])
def new_product(request):
    return Product(*request.param)


@pytest.fixture
def make_product():
    def _make_product(name="Товар", description="Описание", price=100, quantity=1):
        return Product(name, description, price, quantity)
    return _make_product


@pytest.fixture
def new_category(make_product):
    products = [
        make_product(name='Ноутбук', description='Последней модели', price=70_000.00, quantity=5),
        make_product(name='Смартфон', description='С камерой 100MP', price=50_000.00, quantity=10),
        make_product(name='Планшет', description='Для рисования', price=30_000.00, quantity=0)
    ]
    return Category('Техника', 'Описание категории техники', products)
