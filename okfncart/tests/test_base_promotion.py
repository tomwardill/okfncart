import unittest

from okfncart.promotions import (
    BasePromotion,
    BuyOneGetOneFreePromotion,
    BuyTwoGetOneFree
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
            promotion.check_promotion({})

class TestBuyOneGetOneFreePromotion(unittest.TestCase):

    def test_adds_one_to_quantity(self):

        promotion = BuyOneGetOneFreePromotion('test_bogof_1')
        fixture = {
            'products': {
                'test_bogof_1': 1
            }
        }

        promotion.check_promotion(fixture)

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

        promotion.check_promotion(fixture)

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

        promotion.check_promotion(fixture)

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

        promotion.check_promotion(fixture)

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

        promotion.check_promotion(fixture)

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

        promotion.check_promotion(fixture)

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

        promotion.check_promotion(fixture)

        self.assertEqual(
            7,
            fixture['products']['test_btgof_2']
        )