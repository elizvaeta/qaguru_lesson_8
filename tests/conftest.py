import pytest
from models.cart import Cart
from models.product import Product


@pytest.fixture(scope='function')
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture(scope='function')
def milk() -> Product:
    return Product("milk", 100, "Delicious milk", 20)


@pytest.fixture(scope='function')
def cookie() -> Product:
    return Product("cookie", 120, "Delicious cookie", 50)


@pytest.fixture(scope='function')
def cat_food() -> Product:
    return Product("cat_food", 150, "Delicious cat food", 50)


@pytest.fixture(scope='function')
def filled_cart(milk, cookie, cat_food) -> Cart:
    cart = Cart()
    cart.add_product(milk, 2)
    cart.add_product(cookie, 3)
    cart.add_product(cat_food, 14)

    return cart
