from django.db import models
from users.models import User
from products.models import Product


# Create your models here.

class BasketQuerySet(models.QuerySet):
    def items(self):
        for basket in self:
            return BasketItem.objects.filter(basket_id=basket.id)

    def total_sum(self):
        # for basket in self:
        return sum(basketItem.sum() for basketItem in self.items())

    def total_quantity(self):
        # for basket in self:
        return sum(basketItem.quantity for basketItem in self.items())


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Кошик користувача: {self.user.username}"

    objects = BasketQuerySet.as_manager()

    # def items(self):
    #     return BasketItem.objects.filter(basket_id=self.id)
    #
    # def total_sum(self):
    #     return sum(basketItem.sum() for basketItem in self.items())
    #
    # def total_quantity(self):
    #     return sum(basketItem.quantity for basketItem in self.items())


class BasketItem(models.Model):
    basket = models.ForeignKey(to=Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def sum(self):
        return self.product.actual_price() * self.quantity
