

class Cart(object):

    def __init__(self, product_data):
        """Set up a Cart object with the given data

        :param product_data: Product data to use in cart
        :type product_data: dict
        """
        self.product_data = product_data
        self.current_products = {}

    def AddToCart(self, product, quantity=1):
        """Add a product to the cart

        :param product: Name of product to add to cart
        :type product: str
        :param quantity: Quantity of product to add to cart
        :type quantity: int
        """

        if product in self.current_products:
            self.current_products[product]['quantity'] += quantity
        else:
            self.current_products[product] = {
                'quantity': quantity
            }
