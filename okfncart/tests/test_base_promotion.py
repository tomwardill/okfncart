import unittest

from okfncart.promotions import (
    BasePromotion,
    BuyOneGetOneFreePromotion
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