from django.contrib import admin
from products.models import Product, ProductCategory, Discount

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Discount)
