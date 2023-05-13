from django.urls import path
from orders.views import basket_add, basket_remove, order_create, orders, order

app_name = 'orders'

urlpatterns = [
    path('basket/add/<int:product_id>', basket_add, name="basket_add"),
    path('basket/remove/<basket_item_id>', basket_remove, name="basket_remove"),
    path('create/', order_create, name="order_create"),
    path('orders/', orders, name="orders"),
    path('order/<int:order_id>', order, name="order"),

]
