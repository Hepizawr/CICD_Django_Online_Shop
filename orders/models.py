from django.db import models
from users.models import User
from products.models import Product


# Create your models here.

class BasketQuerySet(models.QuerySet):
    def items(self):
        for basket in self:
            return BasketItem.objects.filter(basket_id=basket.id)

    def total_sum(self):
        return sum(basketItem.sum() for basketItem in self.items())

    def total_quantity(self):
        return sum(basketItem.quantity for basketItem in self.items())


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Кошик користувача: {self.user.username}"

    objects = BasketQuerySet.as_manager()


class BasketItem(models.Model):
    basket = models.ForeignKey(to=Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def sum(self):
        return self.product.actual_price() * self.quantity


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    order_status = (
        ("Pr", "Processing"),
        ("Co", "Confirmed"),
        ("Ca", "Canceled"),
        ("Dy", "Delivery"),
        ("Dd", "Delivered"),
    )

    status = models.CharField(max_length=2, choices=order_status, default="Pr")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} | Order #{self.id}"

    def get_status(self):
        order_status = {
            "Pr": "Processing",
            "Co": "Confirmed",
            "Ca": "Canceled",
            "Dy": "Delivery",
            "Dd": "Delivered"
        }
        return order_status[f"{self.status}"]

    def items(self):
        return OrderItem.objects.filter(order_id=self.id)

    def total_sum(self):
        return sum(orderItem.sum() for orderItem in self.items())


class OrderItemQuerySet(models.QuerySet):
    def create_from_basket(self, order: Order, basket: BasketQuerySet):
        for basketItem in basket.items():
            self.create(order=order, product=basketItem.product, quantity=basketItem.quantity)


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    objects = OrderItemQuerySet.as_manager()

    def sum(self):
        return self.product.actual_price() * self.quantity
