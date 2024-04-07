"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models.cart import Cart
from models.product import Product


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(product.quantity + 1)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(product.quantity - 1)
        assert product.quantity == 1

        product.buy(product.quantity)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, milk, cookie):
        cart = Cart()
        cart.add_product(milk)
        cart.add_product(cookie, 2)
        cart.add_product(cookie, 1)

        assert cart.products == {milk: 1, cookie: 3}

    def test_cart_remove_product(self, filled_cart, milk, cookie, cat_food):
        cat_food_start_quantity = filled_cart.products[cat_food]

        filled_cart.remove_product(milk)
        filled_cart.remove_product(cookie, filled_cart.products[cookie] + 1)
        filled_cart.remove_product(cat_food, 1)

        assert milk not in filled_cart.products
        assert cookie not in filled_cart.products
        assert filled_cart.products[cat_food] == cat_food_start_quantity - 1

    def test_cart_clear(self, filled_cart):
        filled_cart.clear()

        assert not filled_cart.products

    def test_cart_get_total_price(self, filled_cart, milk, cookie, cat_food):
        milk_total_price = milk.price * filled_cart.products[milk]
        cookie_total_price = cookie.price * filled_cart.products[cookie]
        cat_food_total_price = cat_food.price * filled_cart.products[cat_food]

        assert filled_cart.get_total_price() == milk_total_price + cookie_total_price + cat_food_total_price

    def test_cart_get_total_price_without_products(self, filled_cart, milk, cookie, cat_food):
        cart = Cart()

        assert cart.get_total_price() == 0

    def test_cart_buy(self, filled_cart, milk, cookie, cat_food):
        milk_start_total_quantity = milk.quantity
        cookie_start_total_quantity = cookie.quantity
        cat_food_start_total_quantity = cat_food.quantity

        milk_start_cart_quantity = filled_cart.products[milk]
        cookie_start_cart_quantity = filled_cart.products[cookie]
        cat_food_start_cart_quantity = filled_cart.products[cat_food]

        filled_cart.buy()

        assert milk.quantity == milk_start_total_quantity - milk_start_cart_quantity
        assert cookie.quantity == cookie_start_total_quantity - cookie_start_cart_quantity
        assert cat_food.quantity == cat_food_start_total_quantity - cat_food_start_cart_quantity

    def test_cart_buy_not_enough_products(self, milk):
        cart = Cart()
        cart.add_product(milk, milk.quantity + 1)

        with pytest.raises(ValueError):
            cart.buy()
