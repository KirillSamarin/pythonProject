import pytest
from main import Product, Category, Smartphone, LawnGrass

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


@pytest.fixture
def smartphone():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий"
    )


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )


def test_product(product1):
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


def test_str_product(product1, product2, product3):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_add(product1, product2, product3):
    assert product1 + product2 == 2580000.0
    assert product1 + product3 == 1334000.0
    assert product2 + product3 == 2114000.0


def test_str_category(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27"


def test_smartphone(smartphone):
    assert smartphone.name == "Xiaomi Redmi Note 11"
    assert smartphone.description == "1024GB, Синий"
    assert smartphone.price == 31000.0
    assert smartphone.quantity == 14
    assert smartphone.efficiency == 90.3
    assert smartphone.model == "Note 11"
    assert smartphone.memory == 1024
    assert smartphone.color == "Синий"


def test_lawn_grass(lawn_grass):
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"