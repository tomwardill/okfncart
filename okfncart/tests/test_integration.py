import unittest

from okfncart.cart import Cart
from okfncart.data_handler import DataHandler
from okfncart.promotions.promotion_loader import PromotionLoader


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.handler = DataHandler()
        self.loader = PromotionLoader()

        product_data = self.handler.load_product_data()
        self.cart = Cart(product_data)

        self.promotions = self.loader.load_promotions()

    def test_full_integration_without_promotions(self):

        expected_total = {
            'products': {
                'ice cream': 1,
                'mars bar': 2,
                'strawberries': 1
                },
            'total_price': 7.19
        }

        self.cart.add_to_cart('ice cream')
        self.cart.add_to_cart('mars bar', quantity=2)
        self.cart.add_to_cart('strawberries')

        total = self.cart.calculate_total()
        self.assertEqual(
            expected_total,
            total
        )

    def test_full_integration_with_promotions(self):

        expected_total = {
            'products': {
                'ice cream': 2,
                'mars bar': 1,
                'snickers bar': 1,
                'strawberries': 3
            },
            'total_price': 8.9
        }

        self.cart.add_to_cart('ice cream', quantity=1)
        self.cart.add_to_cart('strawberries', quantity=2)
        self.cart.add_to_cart('mars bar')
        self.cart.add_to_cart('snickers bar')

        total = self.cart.calculate_total(
            promotions=self.promotions
        )

        self.assertEqual(
            expected_total,
            total
        )