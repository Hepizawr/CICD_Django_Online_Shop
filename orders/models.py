from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Discount


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # User_account
    order_status = (
        ("Pr", "Processing"),
        ("Co", "Confirmed"),
        ("Ca", "Canceled"),
        ("Dy", "Delivery"),
        ("Dd", "Delivered"),
    )
    status = models.CharField(max_length=2, choices=order_status, default="Pr")  # Enum
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        if self.discount:
            return self.price * self.discount.promo * self.quantity
        else:
            return self.price * self.quantity