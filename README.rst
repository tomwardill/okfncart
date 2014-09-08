Shopping Cart Emulator
----------------------

This is a code based shopping cart emulator, it has no UI and can only be interacted with via the python REPL or other form of script.


General Use
===========
Loading Data
~~~~~~~~~~~~

Small sample data is provided, and is loaded by default::

    from okfncart.data_handler import DataHandler
    
    handler = DataHandler()

    product_data = handler.LoadProductData()
    # or provide a path to a different data csv file
    product_data = handler.LoadProductData('/tmp/new_data.csv')

Creating a cart
~~~~~~~~~~~~~~~

A cart object can be created with the loaded data::

    from okfncart.cart import Cart
    from okfncart.data_handler import DataHandler
   
    handler = DataHandler()
    product_data = handler.LoadProductData()

    cart = Cart(product_data)

Loading Promotions
~~~~~~~~~~~~~~~~~~

Promotions are stored as python files and loaded via a plugin system (Refer to later in the documentation for creating a new promotion)::

    from okfncart.cart import Cart
    from okfncart.data_handler import DataHandler
    from okfncart.promotions.promotion_loader import PromotionLoader

    handler = DataHandler()
    product_data = handler.LoadProductData()

    loader = PromotionLoader()

    cart = Cart(product_data)

    # load from the default directory
    promotions = loader.LoadPromotions()
    # load from a different directory
    promotions = loader.LoadPromotions('/tmp/promotions/')

Interacting with the cart
~~~~~~~~~~~~~~~~~~~~~~~~~

The cart has a method for adding to the cart and one for calculating the total. Promotions are optional and are passed in during calculating the cart total::

    from okfncart.cart import Cart
    from okfncart.data_handler import DataHandler
    from okfncart.promotions.promotion_loader import PromotionLoader

    handler = DataHandler()
    product_data = handler.LoadProductData()

    loader = PromotionLoader()

    cart = Cart(product_data)

    # load from the default directory
    promotions = loader.LoadPromotions()

    # default is quantity=1
    cart.AddToCart('ice cream', quantity=1)
    cart.AddToCart('strawberries', quantity=2)
    cart.AddToCart('mars bar')
    cart.AddToCart('snickers bar')

    # promotions parameter is optional here
    total = cart.CalculateTotal(
        promotions=promotions
    )

Promotions
==========

Promotions are implemented as a basic python plugin system using callbacks. Some sample implementations are provided.

Creating a promotion based on an existing sample
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample promotions are available in `promotions/__init__.py`. To use one of them, create a new file with the name of the promotion (`IceCreamBOGOF.py`), inherit the correct promotion with the same name and implement the required variables::

    from okfncart.promotions import BuyOneGetOneFreePromotion

    class IceCreamBOGOF(BuyOneGetOneFreePromotion):
        target_object = 'ice cream'

Creating a new promotion
~~~~~~~~~~~~~~~~~~~~~~~~

To create a new promotion, add a new class to the __init__.py (or alter the `ignore_files` parameter in the BasePromotion class to include your new file) and then implement the `check_promotion` callback method::

    class BuyOneGetOneFreePromotion(BasePromotion):
        target_object = None
        
        def check_promotion(self, current_total, product_data):
            if self.target_object in current_total['products']:
                current_quantity = current_total['products'][self.target_object]
                current_quantity = current_quantity * 2
                current_total['products'][self.target_object] = current_quantity

The implement the promotion by following the procedure above.

Testing
=======

There are unit tests for most of the implementation. The easiest way to test these is to checkout out the repo and run::

    python setup.py test

