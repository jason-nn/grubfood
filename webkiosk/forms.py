from django.forms import ModelForm
from .models import Food, Customer, Order


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
