from operator import mod
from turtle import mode
from django.db import models
#superuser= username:admin ,password:1234
# Create your models here.
class Menu(models.Model):
    name_item = models.CharField(
        max_length=122,help_text="Name of item", null =True,blank =True)
    image = models.ImageField(
        upload_to='productimg',help_text="Image of item", null =True,blank =True)
    category = models.CharField(
        max_length=22,help_text="Category", null =True,blank =True)
    price =  models.DecimalField(
        decimal_places=2, max_digits=50, help_text="Amount paid for item", null =True,blank =True)
    discounts =  models.DecimalField(
        decimal_places=2, max_digits=50, help_text="Discount prince", null =True,blank =True)
    platesize = models.CharField(
        max_length=50,help_text="Size of item", null =True,blank =True)
    
    def __str__(self):
        return self.name_item

class Order(models.Model):
    choices = (('Received', 'Received'),
        ('Scheduled', 'Scheduled'), 
        ('Shipped', 'Shipped'),
        ('In Progress','In Progress'),
        )
    name = models.CharField(max_length=30)
    date = models.DateField(help_text="Date of order", default=None)
    status = models.CharField(max_length = 100, choices = choices, default="In Progress")
    
    def __str__(self):
        return self.name
    
