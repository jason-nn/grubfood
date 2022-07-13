from django.shortcuts import render

from django.http import HttpResponse

from .models import Food, Customer, Order


def index(request):
    return HttpResponse('Home')


def foods_index(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'webkiosk/foods_index.html', context)


def customers_index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'webkiosk/customers_index.html', context)


def orders_index(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'webkiosk/orders_index.html', context)
