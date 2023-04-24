from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class ImageProduct(models.Model):
    product_id = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    priority = models.IntegerField(default=1)

    class Meta:
        ordering = ('priority',)

    def __str__(self):
        return f"{self.product_id.name}.image: {self.priority}"


class Discount(models.Model):
    product_id = models.ForeignKey(Product, related_name='discounts', on_delete=models.CASCADE)
    promo = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return f"{self.product_id.name}.discount: -{self.promo}%"
