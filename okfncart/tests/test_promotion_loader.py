import unittest

from okfncart.promotions.promotion_loader import PromotionLoader


class TestPromotionLoader(unittest.TestCase):

    def setUp(self):
        self.loader = PromotionLoader()

    def test_load_promotions_empty(self):
        self.loader.LoadPromotions()