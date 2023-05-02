from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "updated", "status")
    list_editable = ("status",)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
