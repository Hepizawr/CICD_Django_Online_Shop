from django.shortcuts import render
from products.models import Product, ProductCategory, Discount


# Create your views here.
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
