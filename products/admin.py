from django.contrib import admin
from .models import Product, ImageProduct, Discount


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock")
    list_editable = ("price", "stock",)


admin.site.register(Product, ProductAdmin)
admin.site.register(ImageProduct)
admin.site.register(Discount)
