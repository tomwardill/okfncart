import unittest

from okfncart.cart import Cart
from okfncart.promotions import (
    BuyOneGetOneFreePromotion,
    BuyTwoGetOneFree
)

class TestCart(unittest.TestCase):

    fixture = {
        'test_product_1': 0.1,
        'test_product_2': 0.4,
        'test_product_3': 3.5,
    }

    def setUp(self):
        self.cart = Cart(self.fixture)

    def test_cart_init(self):
        cart = Cart(self.fixture)

    def test_cart_init_empty(self):
        cart = Cart({})

    def test_add_to_cart(self):
        self.cart.add_to_cart('test_product_1')

        self.assertTrue('test_product_1' in self.cart.current_products)
        self.assertEqual(
            1,
            self.cart.current_products['test_product_1']['quantity']
        )

    def test_add_to_cart_with_quantity(self):
        self.cart.add_to_cart('test_product_2', quantity=4)

        self.assertEqual(
            4,
            self.cart.current_products['test_product_2']['quantity']
        )

    def test_add_to_cart_already_exists(self):
        self.cart.add_to_cart('test_product_1')

        self.assertTrue('test_product_1' in self.cart.current_products)
        self.assertEqual(
            2,
            self.cart.current_products['test_product_1']['quantity']
        )

    def test_add_to_cart_already_exists(self):
        self.cart.add_to_cart('test_product_3', quantity=5)
        self.cart.add_to_cart('test_product_3', quantity=2)

        self.assertTrue('test_product_3' in self.cart.current_products)
        self.assertEqual(
            7,
            self.cart.current_products['test_product_3']['quantity']
        )

    def test_add_to_cart_multiple_products(self):
        self.cart.add_to_cart('test_product_1')
        self.cart.add_to_cart('test_product_2')

        self.assertTrue('test_product_1' in self.cart.current_products)
        self.assertTrue('test_product_2' in self.cart.current_products)

        self.assertEqual(
            1,
            self.cart.current_products['test_product_1']['quantity']
        )
        self.assertEqual(
            1,
            self.cart.current_products['test_product_2']['quantity']
        )

    def test_add_to_cart_multiple_products_with_quantity(self):
        self.cart.add_to_cart('test_product_1', quantity=2)
        self.cart.add_to_cart('test_product_2', quantity=4)

        self.assertTrue('test_product_1' in self.cart.current_products)
        self.assertTrue('test_product_2' in self.cart.current_products)

        self.assertEqual(
            2,
            self.cart.current_products['test_product_1']['quantity']
        )
        self.assertEqual(
            4,
            self.cart.current_products['test_product_2']['quantity']
        )

    def test_calculate_total(self):
        self.cart.add_to_cart('test_product_1')

        total = self.cart.calculate_total()

        self.assertTrue('total_price' in total)
        self.assertEqual(
            0.1,
            total['total_price']
        )

    def test_calculate_total_product_list(self):
        self.cart.add_to_cart('test_product_1')
        total = self.cart.calculate_total()

        self.assertTrue('products' in total)
        self.assertTrue('test_product_1' in total['products'])
        self.assertEqual(
            1,
            total['products']['test_product_1']
        )

    def test_calculate_total_multiple_products(self):
        for product in self.fixture.iterkeys():
            self.cart.add_to_cart(product)

        total = self.cart.calculate_total()

        for product in self.fixture.iterkeys():
            self.assertTrue(product in total['products'])
            self.assertEqual(
                1,
                total['products'][product]
            )

    def test_calculate_total_quantity(self):
        self.cart.add_to_cart('test_product_1', quantity=4)
        total = self.cart.calculate_total()

        self.assertTrue('products' in total)
        self.assertTrue('test_product_1' in total['products'])
        self.assertEqual(
            4,
            total['products']['test_product_1']
        )

    def test_calculate_total_multiple_products(self):
        for quantity, product in enumerate(self.fixture.iterkeys()):
            self.cart.add_to_cart(product, quantity=quantity)

        total = self.cart.calculate_total()

        for quantity, product in enumerate(self.fixture.iterkeys()):
            self.assertTrue(product in total['products'])
            self.assertEqual(
                quantity,
                total['products'][product]
            )

    def test_calculate_total_with_single_promotion(self):

        promotions = [
            BuyOneGetOneFreePromotion('test_product_1')
        ]

        self.cart.add_to_cart('test_product_1')
        total = self.cart.calculate_total(promotions=promotions)

        self.assertEqual(
            2,
            total['products']['test_product_1']
        )

    def test_calculate_total_with_multiple_promotions(self):

        promotions = [
            BuyOneGetOneFreePromotion('test_product_1'),
            BuyTwoGetOneFree('test_product_2')
        ]

        self.cart.add_to_cart('test_product_1')
        self.cart.add_to_cart('test_product_2', quantity=2)
        total = self.cart.calculate_total(promotions=promotions)

        self.assertEqual(
            2,
            total['products']['test_product_1']
        )

        self.assertEqual(
            3,
            total['products']['test_product_2']
        )