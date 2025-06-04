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
    # order_date = models.IntegerField(default=1)# Date and time of order
    # received_date = models.DateTimeField(null=True, blank=True)  # Date and time the order was received by customer
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    # age=models.IntegerField(default=1)
    # Status1=models.ForeignKey(Status,on_delete=models.CASCADE,blank=True) 
     
   
   