from unicodedata import decimal
from django.db import models
from django.forms import CharField, DecimalField

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_quantity = models.IntegerField()
    img = models.CharField(max_length=255)
