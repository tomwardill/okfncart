import imp
import os

class PromotionLoader(object):

    default_promotion_directory = os.path.dirname(__file__)
    ignore_files = ['__init__.py', 'promotion_loader.py']

    def __init__(self, promotion_folder=None):
        """Create a new promotion loader

        :param promotion_folder: Folder to search for promotions, defaults to '.'
        :type promotion_folder: str
        """
        if not promotion_folder:
            promotion_folder = self.default_promotion_directory
        self.promotion_folder = promotion_folder

    def LoadPromotions(self):
        """Load the promotions so they can be used in a cart
        """

        promotions = []
        possible_promotions = os.listdir(self.promotion_folder)
        for possible_promotion in possible_promotions:
            if '.pyc' in possible_promotion:
                continue
            if possible_promotion in self.ignore_files:
                continue
            if not possible_promotion.endswith('.py'):
                continue

            promotion_name = possible_promotion[:-3]
            promotion = imp.load_module(
                promotion_name,
                os.path.abspath(
                    os.path.join(
                        self.default_promotion_directory,
                        possible_promotion
                    ))
            )

            promotions.append(promotion)

        return promotions