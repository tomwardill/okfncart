import imp
import os

class PromotionLoader(object):

    default_promotion_directory = os.path.dirname(__file__)
    ignore_files = ['__init__.py', 'promotion_loader.py']

    def load_promotions(self, promotion_folder=None):
        """Load the promotions so they can be used in a cart

        :param promotion_folder: Folder to search for promotions, defaults to '.'
        :type promotion_folder: str
        """

        if not promotion_folder:
            promotion_folder = self.default_promotion_directory
        self.promotion_folder = promotion_folder

        promotions = []
        possible_promotions = os.listdir(self.promotion_folder)

        # Iterate the files in the target dir
        for possible_promotion in possible_promotions:

            # Ignore certain files
            if '.pyc' in possible_promotion:
                continue
            if possible_promotion in self.ignore_files:
                continue
            if not possible_promotion.endswith('.py'):
                continue

            # trim the .py from the filename
            promotion_name = possible_promotion[:-3]

            # Load the module
            promotion = imp.load_source(
                promotion_name,
                os.path.abspath(
                    os.path.join(
                        self.default_promotion_directory,
                        possible_promotion,
                    ))
            )

            # Use the name of the file to get the right class
            target = getattr(promotion, promotion_name)

            # Instantiate the class and add it to the list
            promotions.append(target())

        return promotions
