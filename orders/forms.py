from django import forms
from orders.models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Thomas",
    }), required=True)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Shelby",
    }), required=True)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "you@example.com",
    }), required=False)

    address = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "25 Kingston St.Superior, WI 54880",
    }), required=True)

    class Meta:
        model = Order
        fields = ("user", "first_name", "last_name", "email", "address")


class OrderItemQuantityForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "min": "0",
    }))

    class Meta:
        model = OrderItem
        fields = ("quantity",)
