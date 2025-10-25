from django.db import models
from .status import Status
from django.conf import settings  
from django.utils import timezone 


class Main_table(models.Model):
    order_id = models.AutoField(primary_key=True)  # Automatically generated, unique ID
    userid = models.IntegerField(default=1)
    user_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=255)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    price = models.IntegerField(default = 100)
    hello=models.CharField(max_length=10,default=1)
     
   
   