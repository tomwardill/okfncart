import unittest
import cart

class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = cart.Cart()

    def test_load_data(self):
        self.cart.LoadProductData()

        # check we've loaded the expected amount of data
        self.assertEqual(
            4,
            len(self.cart.product_data.keys())
        )

        # sample some rows to check the values
        self.assertEqual(
            3.49,
            self.cart.product_data['ice cream']
        )

    def test_load_data_fails(self):
        with self.assertRaises(IOError):
            self.cart.LoadProductData('./thisdoesnotexist.csv')