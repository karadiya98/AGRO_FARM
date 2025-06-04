from django.db import models
from django.conf import settings

class CartItem1(models.Model):
    productid = models.AutoField(primary_key=True)
    userid = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    quantity=models.IntegerField(default=1)
    total=models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/')
   
    
    def getcarts():
        return CartItem1.objects.all()


    def __str__(self):
        return self.name