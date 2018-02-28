import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=256)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    email= models.EmailField()
    phone = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    number_of_shares = models.IntegerField(default=0)
    purchase_price = models.FloatField()
    date_purchased = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Cryptocurrency(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number_of_coins_tokens = models.IntegerField(default=0)
    purchase_price = models.FloatField()
    date_purchased = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

