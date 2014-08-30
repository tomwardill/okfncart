class BasePromotion(object):

    def check_promotion(self, current_total):
        """Base method for promotions to calculate with.
        Should be implemented in the promotion class
        """

        raise NotImplementedError(
            "Promotion has not implemented check_promotion"
        )