from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import FoodForm, CustomerForm, OrderForm
from .models import Food, Customer, Order


def index(request):
    return render(request, 'webkiosk/index.html')


def foods_index(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'webkiosk/foods/index.html', context)


def foods_show(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    context = {'food': food}
    return render(request, 'webkiosk/foods/show.html', context)


def foods_new(request):
    form = FoodForm()
    context = {'form': form}
    return render(request, 'webkiosk/foods/new.html', context)


def foods_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:foods_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:foods_new'))


def customers_index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'webkiosk/customers/index.html', context)


def customers_show(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    return render(request, 'webkiosk/customers/show.html', context)


def customers_new(request):
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'webkiosk/customers/new.html', context)


def customers_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:customers_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:customers_new'))


def orders_index(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'webkiosk/orders/index.html', context)


def orders_show(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {'order': order}
    return render(request, 'webkiosk/orders/show.html', context)
