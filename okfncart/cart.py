

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

    def CalculateTotal(self, promotions=None):
        """Calculate the total price and quantities of the cart

        :param promotions: List of promotions that can be applied
        :type promotions: list
        """

        total = {
            'total_price': 0,
            'products': {}
        }
        for product, values in self.current_products.iteritems():
            price = self.product_data[product]
            total_product_price = price * values['quantity']
            total['total_price'] += total_product_price
            total['products'][product] = values['quantity']

        return total
