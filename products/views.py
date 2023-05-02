from django.shortcuts import render

# Create your views here.
import random


class Product:

    def __init__(self):
        self.title = 'T-shirt'
        self.category = random.choice(['Male', 'Female', 'Girl', 'Boy'])
        self.price = random.randint(10, 1000)

def main_page(request):

    products = [Product() for _ in range(20)]
    #products = list(range(20))
    return render(request, 'products_list.html', context={"products":products})
