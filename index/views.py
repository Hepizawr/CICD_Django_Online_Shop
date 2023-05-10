from django.shortcuts import render
from products.models import Product, Discount


# Create your views here.
def index(request):
    context = {
        'title': "Famms",
        'products': Product.objects.all()[:8],
        'discounts': Discount.objects.all()[:2]
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
