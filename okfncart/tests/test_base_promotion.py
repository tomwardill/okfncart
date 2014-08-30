import unittest

from okfncart.promotions import (
    BasePromotion,
    BuyOneGetOneFreePromotion,
    BuyTwoGetOneFree,
    DiscountOneProductWithAnother
)


class TestBasePromotion(unittest.TestCase):

    def test_instantiation(self):
        promotion = BasePromotion()

    def test_ensure_abstraact(self):
        """The base class method of check_promotion
        should never have a valid implementation
        """

        with self.assertRaises(NotImplementedError):
            promotion = BasePromotion()
            promotion.check_promotion({}, {})

class TestBuyOneGetOneFreePromotion(unittest.TestCase):

    def test_adds_one_to_quantity(self):

        promotion = BuyOneGetOneFreePromotion('test_bogof_1')
        fixture = {
            'products': {
                'test_bogof_1': 1
            }
        }

        promotion.check_promotion(fixture, {})

        self.assertEqual(
            2,
            fixture['products']['test_bogof_1']
        )

    def test_adds_one_to_quantity_multiple_products(self):

        promotion = BuyOneGetOneFreePromotion('test_bogof_1')
        fixture = {
            'products': {
                'test_bogof_1': 1,
                'test_bogof_2': 10
            }
        }

        promotion.check_promotion(fixture, {})

        self.assertEqual(
            2,
            fixture['products']['test_bogof_1']
        )
        self.assertEqual(
            10,
            fixture['products']['test_bogof_2']
        )

    def test_recieve_multiple(self):
        promotion = BuyOneGetOneFreePromotion('test_bogof_1')
        fixture = {
            'products': {
                'test_bogof_1': 5
            }
        }

        promotion.check_promotion(fixture, {})

        self.assertEqual(
            10,
            fixture['products']['test_bogof_1']
        )

class BuyTwoGetOneFreePromotion(unittest.TestCase):

    def test_does_nothing_if_less_than_two(self):

        promotion = BuyTwoGetOneFree('test_btgof_1')
        fixture = {
            'products': {
                'test_btgof_1': 1
            }
        }

        promotion.check_promotion(fixture, {})

        self.assertEqual(
            1,
            fixture['products']['test_btgof_1']
        )

    def test_adds_one_if_buy_two(self):

        promotion = BuyTwoGetOneFree('test_btgof_2')
        fixture = {
            'products': {
                'test_btgof_2': 2
            }
        }

        promotion.check_promotion(fixture, {})

        self.assertEqual(
            3,
            fixture['products']['test_btgof_2']
        )

    def test_adds_two_if_buy_four(self):

        promotion = BuyTwoGetOneFree('test_btgof_2')
        fixture = {
            'products': {
                'test_btgof_2': 4
            }
        }

        promotion.check_promotion(fixture, {})

        self.assertEqual(
            6,
            fixture['products']['test_btgof_2']
        )

    def test_adds_two_if_buy_five(self):

        promotion = BuyTwoGetOneFree('test_btgof_2')
        fixture = {
            'products': {
                'test_btgof_2': 5
            }
        }

        promotion.check_promotion(fixture, {})

        self.assertEqual(
            7,
            fixture['products']['test_btgof_2']
        )

class DiscountOneProductWithAnotherTest(unittest.TestCase):

    def test_does_nothing_correctly(self):

        promotion = DiscountOneProductWithAnother('1', '2', 30)

        fixture = {
            'total_price': 2,
            'products': {
                '5': 5
            }
        }
        result = fixture.copy()

        promotion.check_promotion(fixture, {})

        self.assertEqual(fixture, result)

    def test_reduce_by_discount_quantity_one(self):

        buy_product = 'buy_product'
        discount_product = 'discount_product'
        discount_amount = 0.2

        total_fixture = {
            'total_price': 2,
            'products': {
                buy_product: 1,
                discount_product: 1
            }
        }
        product_fixture = {
            buy_product: 1,
            discount_product: 1
        }

        promotion = DiscountOneProductWithAnother(
            buy_product,
            discount_product,
            discount_amount
        )

        promotion.check_promotion(
            total_fixture,
            product_fixture
        )

        self.assertEqual(
            1.8,
            total_fixture['total_price']
        )

    def test_reduce_by_discount_quantity_five(self):

        buy_product = 'buy_product'
        discount_product = 'discount_product'
        discount_amount = 0.2

        total_fixture = {
            'total_price': 30.8,
            'products': {
                buy_product: 5,
                discount_product: 5
            }
        }
        product_fixture = {
            buy_product: 1.4,
            discount_product: 1.2
        }

        promotion = DiscountOneProductWithAnother(
            buy_product,
            discount_product,
            discount_amount
        )

        promotion.check_promotion(
            total_fixture,
            product_fixture
        )

        self.assertEqual(
            29.6,
            total_fixture['total_price']
        )