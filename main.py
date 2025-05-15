from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, *args):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args):
        pass


class Mixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, Mixin):
    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        if self.__price == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product: dict):
        return cls(product["name"], product["description"], product["price"], product["quantity"])


class Smartphone(Product):
    def __init__(self, name: str, description: str,
                 price: float, quantity: int,
                 efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str,
                 price: float, quantity: int,
                 country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        product_count = []
        for product in self.__products:
            product_count.append(product.quantity)
        return f"{self.name}, количество продуктов: {sum(product_count)}"

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)

    def middle_price(self):
        summa = 0

        if not self.__products:
            return 0
        else:
            try:
                for product in self.__products:
                    summa += product.price
                return summa // len(self.__products)
            except ZeroDivisionError:
                return 0

    @property
    def products(self):
        products = []
        for product in self.__products:
            products.append(f"{product.name}, {product.price}. Остаток: {product.quantity}")
        return "\n".join(products)


if __name__ == '__main__':  # pragma: no cover
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
