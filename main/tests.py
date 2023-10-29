from django.test import TestCase

class ProductTests(TestCase):

    def test1(self):
        from main.models import Product

        assert Product.objects.count() == 0
        Product.objects.create(
            title="title 1"
        )
        assert Product.objects.count() == 1