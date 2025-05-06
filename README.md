# Описание проекта: Управление продуктами и категориями

Проект реализует систему учета продуктов и категорий с базовыми функциями для интернет-магазина.

## Классы

### 0. Класс `BaseProduct`

**Назначение:**  
Абстракный класс с заготовленными методами для Product

### 1. Класс `Mixin`

**Назначение:**  
Класс-миксин для вывода информации об объекте при инициализации при помощи метода __repr__

**Пример использования:**
class Product(BaseProduct, Mixin):
    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

Terminal

Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)



### 2. Класс `Product` - наследник BaseProduct и Mixin

**Назначение:**  
Представляет товар в магазине.

**Атрибуты:**
- `name` (str) - название продукта
- `description` (str) - описание продукта
- `price` (float) - цена продукта
- `quantity` (int) - количество на складе

**Пример использования:**
product = Product(
    name="iPhone 15",
    description="512GB, Space Gray",
    price=210000.0,
    quantity=8
)

### 3. Классы Smarpthone и LawnGrass - наследники Product

**Назначение:**  
Представляют товар конкретного типа в магазине.

**Атрибуты:**
Smartphone
Те же, что и у Product.
- `efficiency` (float) - эффективность(измеряется от 0.0 до 100.0)
- `model` (str) - модель
- `memory` (int) - количество памяти в ГБ
- `color` (str) - цвет

LawnGrass
Те же, что и у Product.
- `country` (str) - страна производства
- `germination_period` (str) - период прорастания
- `color` (str) - цвет

**Пример использования:**
smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
                            95.5, "S23 Ultra", 256, "Серый")

grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


### 4. Класс Category
Назначение:
Группирует товары по категориям и ведет учет количества.

**Атрибуты:**

- `name` (str) - название категории

- `description` (str) - описание категории

- `products` (list[Product]) - список продуктов в категории

Статические атрибуты:

`product_count` - общее количество продуктов во всех категориях

`category_count` - общее количество созданных категорий

Пример использования:

category = Category(
    name="Смартфоны",
    description="Современные мобильные устройства",
    products=[product1, product2]
)

При создании категории автоматически увеличиваются счетчики:

category_count (+1 за каждую новую категорию)

product_count (+N за каждый добавленный продукт)



Покрытие тестами составляет 98%(отчет в папке htmlcov)
