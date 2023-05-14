from django.test import TestCase
from django.urls import reverse
from products.models import ProductCategory, Product, Discount


# Create your tests here.
class ModelProductTests(TestCase):
    def setUp(self) -> None:
        test_category = ProductCategory(name="clothe")
        test_category.save()
        test_product = Product(name="T-shirt", description="Test_description", image="media/products_images/p1.png",
                               price=100, quantity=10, category=test_category)
        test_product.save()
        Discount.objects.create(product=test_product, value=10, description="Test_description", active=True)

    def test_get_product_image(self):
        product = Product.objects.get(name="T-shirt")
        self.assertTrue(product.image)

    def test_get_product_discount(self):
        product = Product.objects.get(name="T-shirt")
        self.assertTrue(product.discount())

    def test_actually_product_price(self):
        product = Product.objects.get(name="T-shirt")
        self.assertEqual(product.actual_price(), 90)

    def test_get_product_at_page(self):
        product = Product.objects.get(name="T-shirt")
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["products"], [product])
