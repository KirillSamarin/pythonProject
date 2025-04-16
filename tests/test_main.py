import pytest
from main import Product, Category

Category.category_count = 0
Category.product_count = 0


@pytest.fixture
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def product2():
    return Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )


@pytest.fixture
def product3():
    return Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )


@pytest.fixture
def category1(product1, product2, product3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )


def test_product(product1, product2):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_category(category1):
    assert category1.name == "Смартфоны"
    assert (
        category1.description ==
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_product_price_setter(product1):
    product1.price = 200000.0
    assert product1.price == 200000.0
    product1.price = -100
    assert product1.price == 200000.0


def test_new_product():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 1000.0,
        "quantity": 10
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 1000.0
    assert product.quantity == 10


def test_add_product(category1):
    initial_products = category1.products.split('\n')  # Разделяем строку по переносам
    initial_count = len(initial_products)
    new_product = Product("New Product", "New Description", 500.0, 20)
    category1.add_product(new_product)
    updated_products = category1.products.split('\n')
    updated_count = len(updated_products)
    assert updated_count == initial_count + 1


def test_products(category1):
    products_info = category1.products
    assert "Samsung Galaxy S23 Ultra" in products_info
    assert "180000.0" in products_info
    assert "Остаток: 5" in products_info