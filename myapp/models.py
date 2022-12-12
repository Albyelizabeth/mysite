# from unittest.util import max_length
# from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images')
    seller_name = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    
    
class Cart(models.Model):
    name = models.CharField(max_length=100,unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=200)


    
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    