class BasePromotion(object):

    def check_promotion(self, current_total):
        """Base method for promotions to calculate with.
        Should be implemented in the promotion class

        :param current_total: The current basket state
        :type current_total: dict
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

    def check_promotion(self, current_total):
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

    def check_promotion(self, current_total):
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
