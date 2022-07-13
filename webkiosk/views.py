from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate as django_authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


from .forms import FoodForm, CustomerForm, OrderForm
from .models import Food, Customer, Order


def index(request):
    return render(request, 'webkiosk/index.html')


@login_required(login_url='/webkiosk/login')
def foods_index(request):
    foods = Food.objects.order_by('pk')
    context = {'foods': foods}
    return render(request, 'webkiosk/foods/index.html', context)


@login_required(login_url='/webkiosk/login')
def foods_show(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    context = {'food': food}
    return render(request, 'webkiosk/foods/show.html', context)


@login_required(login_url='/webkiosk/login')
def foods_new(request):
    form = FoodForm()
    context = {'form': form}
    return render(request, 'webkiosk/foods/new.html', context)


@login_required(login_url='/webkiosk/login')
def foods_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:foods_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:foods_new'))


@login_required(login_url='/webkiosk/login')
def foods_edit(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    form = FoodForm(instance=food)
    context = {'form': form, 'food_id': food_id}
    return render(request, 'webkiosk/foods/edit.html', context)


@login_required(login_url='/webkiosk/login')
def foods_update(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:foods_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:foods_edit', args=(food_id,)))


@login_required(login_url='/webkiosk/login')
def foods_delete(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    context = {'food': food}
    return render(request, 'webkiosk/foods/delete.html', context)


@login_required(login_url='/webkiosk/login')
def foods_destroy(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        food.delete()
        return HttpResponseRedirect(reverse('webkiosk:foods_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:foods_delete', args=(food_id,)))


@login_required(login_url='/webkiosk/login')
def customers_index(request):
    customers = Customer.objects.order_by('pk')
    context = {'customers': customers}
    return render(request, 'webkiosk/customers/index.html', context)


@login_required(login_url='/webkiosk/login')
def customers_show(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    return render(request, 'webkiosk/customers/show.html', context)


@login_required(login_url='/webkiosk/login')
def customers_new(request):
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'webkiosk/customers/new.html', context)


@login_required(login_url='/webkiosk/login')
def customers_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:customers_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:customers_new'))


@login_required(login_url='/webkiosk/login')
def customers_edit(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    form = CustomerForm(instance=customer)
    context = {'form': form, 'customer_id': customer_id}
    return render(request, 'webkiosk/customers/edit.html', context)


@login_required(login_url='/webkiosk/login')
def customers_update(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:customers_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:customers_edit', args=(customer_id,)))


@login_required(login_url='/webkiosk/login')
def customers_delete(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    return render(request, 'webkiosk/customers/delete.html', context)


@login_required(login_url='/webkiosk/login')
def customers_destroy(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        return HttpResponseRedirect(reverse('webkiosk:customers_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:customers_delete', args=(customer_id,)))


@login_required(login_url='/webkiosk/login')
def orders_index(request):
    orders = Order.objects.order_by('pk')
    context = {'orders': orders}
    return render(request, 'webkiosk/orders/index.html', context)


@login_required(login_url='/webkiosk/login')
def orders_show(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {'order': order}
    return render(request, 'webkiosk/orders/show.html', context)


@login_required(login_url='/webkiosk/login')
def orders_new(request):
    form = OrderForm()
    context = {'form': form}
    return render(request, 'webkiosk/orders/new.html', context)


@login_required(login_url='/webkiosk/login')
def orders_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:orders_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:orders_new'))


@login_required(login_url='/webkiosk/login')
def orders_edit(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    form = OrderForm(instance=order)
    context = {'form': form, 'order_id': order_id}
    return render(request, 'webkiosk/orders/edit.html', context)


@login_required(login_url='/webkiosk/login')
def orders_update(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webkiosk:orders_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:orders_edit', args=(order_id,)))


@login_required(login_url='/webkiosk/login')
def orders_delete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {'order': order}
    return render(request, 'webkiosk/orders/delete.html', context)


@login_required(login_url='/webkiosk/login')
def orders_destroy(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('webkiosk:orders_index'))
    else:
        return HttpResponseRedirect(reverse('webkiosk:orders_delete', args=(order_id,)))


def login(request):
    if request.method == 'GET':
        return render(request, 'webkiosk/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django_authenticate(
            request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect(reverse('webkiosk:foods_index'))
        else:
            return HttpResponseRedirect(reverse('webkiosk:login'))


def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('webkiosk:index'))


def authenticate(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('webkiosk:index'))
