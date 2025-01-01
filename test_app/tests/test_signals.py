from django.test import TestCase
from test_app.models import Product


class ProductModelSignalTest(TestCase):
    # test update_negative_price signal
    def test_update_negative_price_signal(self):
        # create a product with negative price
        product = Product.objects.create(name="test_product", price=-10)

        # check if the price is updated to 0
        self.assertEqual(0, product.price)
