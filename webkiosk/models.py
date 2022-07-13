from django.db import models
from datetime import datetime


class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'[{self.pk}] {self.name}, {self.description}, {self.price}'


class Customer(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f'[{self.pk}] {self.firstname} {self.lastname}, {self.address}, {self.city}'

    def orders(self):
        return self.order_set.all()


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]

    orderdatetime = models.DateTimeField(default=datetime.now())
    paymentmode = models.CharField(max_length=4, choices=PAYMENT_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}] {self.customer.firstname} {self.customer.lastname}, {self.food.name}, {self.quantity}, {self.orderdatetime}'

    def totalprice(self):
        return self.quantity * self.food.price
