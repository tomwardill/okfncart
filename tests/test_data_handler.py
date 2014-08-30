import unittest

from data_handler import DataHandler

class TestDataHandler(unittest.TestCase):

    def setUp(self):
        self.handler = DataHandler()

    def test_load_data(self):
        product_data = self.handler.LoadProductData()

        # check we've loaded the expected amount of data
        self.assertEqual(
            4,
            len(product_data.keys())
        )

        # sample some rows to check the values
        self.assertEqual(
            3.49,
            product_data['ice cream']
        )

    def test_load_data_fails(self):
        with self.assertRaises(IOError):
            self.handler.LoadProductData('./thisdoesnotexist.csv')