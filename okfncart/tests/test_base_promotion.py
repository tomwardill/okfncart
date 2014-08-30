import unittest

from okfncart.promotions import BasePromotion


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