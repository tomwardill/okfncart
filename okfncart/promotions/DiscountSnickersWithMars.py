from okfncart.promotions import DiscountOneProductWithAnother


class DiscountSnickersWithMars(DiscountOneProductWithAnother):
    buy_product = 'mars bar'
    discount_product = 'snickers bar'
    discount_amount = 0.2