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
    Adds 1 to the quanitity of `target_object`

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
            current_total['products'][self.target_object] += 1
