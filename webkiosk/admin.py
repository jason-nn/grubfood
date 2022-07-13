from django.contrib import admin

from .models import Food, Customer, Order

admin.site.register([Food, Customer, Order])
