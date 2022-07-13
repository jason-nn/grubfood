from django.urls import path

from . import views

app_name = 'webkiosk'
urlpatterns = [
    path('', views.index, name='index'),

    path('foods', views.foods_index, name='foods_index'),
    # path('foods/new', views.foods_new, name='foods_new'),
    # path('foods/create', views.foods_create, name='foods_create'),
    path('foods/<int:food_id>', views.foods_show, name='foods_show'),
    # path('foods/<int:food_id>/edit', views.foods_edit, name='foods_edit'),
    # path('foods/<int:food_id>/update', views.foods_edit, name='foods_update'),
    # path('foods/<int:food_id>/destroy',
    #      views.foods_destroy, name='foods_destroy'),

    path('customers', views.customers_index, name='customers_index'),
    # path('customers/new', views.customers_new, name='customers_new'),
    # path('customers/create', views.customers_create, name='customers_create'),
    path('customers/<int:customer_id>',
         views.customers_show, name='customers_show'),
    # path('customers/<int:customer_id>/edit',
    #      views.customers_edit, name='customers_edit'),
    # path('customers/<int:customer_id>/update',
    #      views.customers_edit, name='customers_update'),
    # path('customers/<int:customer_id>/destroy',
    #      views.customers_destroy, name='customers_destroy'),

    path('orders', views.orders_index, name='orders_index'),
    # path('orders/new', views.orders_new, name='orders_new'),
    # path('orders/create', views.orders_create, name='orders_create'),
    path('orders/<int:order_id>', views.orders_show, name='orders_show'),
    # path('orders/<int:order_id>/edit', views.orders_edit, name='orders_edit'),
    # path('orders/<int:order_id>/update',
    #      views.orders_edit, name='orders_update'),
    # path('orders/<int:order_id>/destroy',
    #      views.orders_destroy, name='orders_destroy'),
]
