from django.shortcuts import render
from products.models import Product, ProductCategory, Discount


# Create your views here.
def index(request):
    context = {
        'title': "Famms",
        'products': Product.objects.all()[:8],
        'discounts': Discount.objects.all()[:2]
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()
    context = {
        'title': "Famms - products",
        'products': products,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
