from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from orders.models import Basket, BasketItem


# Create your views here.
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user)
    basket_item = BasketItem.objects.filter(basket=basket.first(), product=product)

    if not basket.exists():
        basket = Basket.objects.create(user=request.user)

    if not basket_item.exists():
        BasketItem.objects.create(basket=basket.first(), product=product, quantity=1)
    else:
        basket_item = basket_item.first()
        basket_item.quantity += 1
        basket_item.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_remove(request, basket_item_id):
    basket_item = BasketItem.objects.get(id=basket_item_id)
    basket_item.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
