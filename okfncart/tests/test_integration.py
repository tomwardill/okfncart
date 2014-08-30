import unittest

from okfncart.cart import Cart
from okfncart.data_handler import DataHandler
from okfncart.promotions.promotion_loader import PromotionLoader


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.handler = DataHandler()
        self.loader = PromotionLoader()

        product_data = self.handler.LoadProductData()
        self.cart = Cart(product_data)

        self.promotions = self.loader.LoadPromotions()

    def test_full_integration_without_promotions(self):

        expected_total = {
            'products': {
                'ice cream': 1,
                'mars bar': 2,
                'strawberries': 1
                },
            'total_price': 7.19
        }

        self.cart.AddToCart('ice cream')
        self.cart.AddToCart('mars bar', quantity=2)
        self.cart.AddToCart('strawberries')

        total = self.cart.CalculateTotal()
        self.assertEqual(
            expected_total,
            total
        )