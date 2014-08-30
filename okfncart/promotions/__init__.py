class BasePromotion(object):

    def check_promotion(self, current_total, product_data):
        """Base method for promotions to calculate with.
        Should be implemented in the promotion class

        :param current_total: The current basket state
        :type current_total: dict
        :param product_data: The product information (prices, etc)
        :type: product_data: dict
        """

        raise NotImplementedError(
            "Promotion has not implemented check_promotion"
        )

class BuyOneGetOneFreePromotion(BasePromotion):
    """Implementation of a Buy One Get On Free promotion
    Adds doubles the quantity of `target_object`

    Can either pass the target_object at init time,
    or inherit the class and set target_object at class level
    """

    target_object = None

    def __init__(self, target_object=None):
        """Initalise the promotion

        :param target_object: Set the target object
        :type target_object: str
        """
        if target_object:
            self.target_object = target_object

    def check_promotion(self, current_total, product_data):
        """Add 1 to the quantity of the target
        without increasing the base price

        :param current_total: The current basket state
        :type current_total: dict
        """

        if self.target_object in current_total['products']:
            current_quantity = current_total['products'][self.target_object]
            current_quantity = current_quantity * 2
            current_total['products'][self.target_object] = current_quantity

class BuyTwoGetOneFree(BuyOneGetOneFreePromotion):
    """Implementation of buy two, get one free promotion
    Basic Operation:
    Adds 1 to the quantity of `target_object` if the quantity is 2.
    Complex Operation:
    Adds appropriate quanities if multiples of 2 are bought
    (buy 4, get 6)
    """

    def check_promotion(self, current_total, product_data):
        """Basic Operation:
        Adds 1 to the quantity of `target_object` if the quantity is 2.
        Complex Operation:
        Adds appropriate quanities if multiples of 2 are bought
        (buy 4, get 6)
        """

        if self.target_object in current_total['products']:
            current_quantity = current_total['products'][self.target_object]

            # we explicitly want int maths here
            # as we want number of times 2 goes into the total,
            # as an int
            number_to_add = int(current_quantity) / 2
            current_total['products'][self.target_object] += number_to_add

class DiscountOneProductWithAnother(BasePromotion):
    """Implementation of getting discount on one product
    if another is bought at the same time
    """

    buy_product = None
    discount_product = None
    discount_amount = 0

    def __init__(self, buy_product, discount_product, discount_amount):
        """Initalise the promotion

        :param buy_product: The product that must be bought
        :type buy_product: str
        :param discount_product: The product that will be discounted if also bought
        :type discount_product: str
        :param discount_amount: The amount to discount by
        :type discount_amount: float
        """

        self.buy_product = buy_product
        self.discount_product = discount_product
        self.discount_amount = discount_amount

    def check_promotion(self, current_total, product_data):
        """Discount by the given amount if one product is bought
        at the same time as another
        """

        if (self.buy_product in current_total['products']
            and self.discount_product in current_total['products']):

            # get the price of the discount_product
            normal_price = product_data[self.discount_product]
            quantity = current_total['products'][self.discount_product]
            # reduce the total by that * quantity
            current_total['total_price'] -= normal_price * quantity

            # calculate the discount_price
            discount_price = normal_price * (1 - self.discount_amount)
            new_total_price = discount_price * quantity

            # add it together
            current_total['total_price'] += new_total_price