from django.urls import path
from orders.views import basket_add, basket_remove

app_name = 'orders'

urlpatterns = [
    path('basket/add/<int:product_id>', basket_add, name="basket_add"),
    path('basket/remove/<basket_item_id>', basket_remove, name="basket_remove"),
]
