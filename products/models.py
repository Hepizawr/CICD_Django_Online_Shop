from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="product_images")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f"Продукт: {self.name} |Категорія: {self.category.name}"

    def discount(self):
        try:
            return Discount.objects.get(product=self)
        except Exception:
            return None

    def actual_price(self):
        if self.discount():
            return self.price - ((self.discount().value * self.price) / 100)
        else:
            return self.price


class Discount(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    value = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Продукт: {self.product.name} |Знижка: {self.value}%"
