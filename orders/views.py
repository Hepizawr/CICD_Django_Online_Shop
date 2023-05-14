from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.urls import reverse
from orders.models import Basket, BasketItem, Order, OrderItem
from orders.forms import OrderCreateForm


# Create your views here.
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user)
    basket_item = BasketItem.objects.filter(basket=basket.first(), product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user)
        basket = Basket.objects.filter(user=request.user)

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


@login_required
def order_create(request):
    basket = Basket.objects.filter(user=request.user)

    if request.method == "POST":
        form = OrderCreateForm(data=request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()
            OrderItem.objects.create_from_basket(order, basket)
            basket.first().delete()
            return HttpResponseRedirect(reverse('index:index'))
    else:
        form = OrderCreateForm(instance=request.user)

    context = {
        'title': 'Famms - order create',
        'basket': basket,
        'form': form,
    }
    return render(request, "orders/order-create.html", context)


@login_required
def orders(request):
    context = {
        'title': "Famms - orders",
        'orders': Order.objects.filter(user=request.user).order_by("-id")
    }
    return render(request, "orders/orders.html", context)


@login_required
def order(request, order_id):
    context = {
        'title': "Famms - order",
        'order': Order.objects.get(id=order_id)
    }
    return render(request, "orders/order.html", context)
