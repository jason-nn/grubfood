from django.shortcuts import render

from django.http import HttpResponse

from .models import Food, Customer, Order


def index(request):
    return render(request, 'webkiosk/index.html')


def foods_index(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'webkiosk/foods/index.html', context)


def customers_index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'webkiosk/customers/index.html', context)


def orders_index(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'webkiosk/orders/index.html', context)
