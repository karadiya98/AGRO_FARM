from django.db import models
from .category import Categories 



class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,default=1) 
    image = models.ImageField(upload_to='uploads/product_images/')

    def getproducts():
        return Products.objects.all()
    
    def getproducts_category(Categories_id):
        if Categories_id:
            return Products.objects.filter(category=Categories_id)
        else:
            return Products.getproducts()

    def __str__(self):
        return self.name
